"""
Testes da lógica de sorteios - Validações e edge cases
"""
import pytest
import json


class TestValidacoesNumeros:
    """Testes de validação do sorteio de números"""
    
    def test_intervalo_valido(self, client):
        """Testa intervalo válido"""
        response = client.post('/sortear/numero',
            json={'minimo': 1, 'maximo': 100, 'quantidade': 1})
        assert response.status_code == 200
    
    def test_intervalo_invalido(self, client):
        """Testa intervalo inválido (min > max)"""
        response = client.post('/sortear/numero',
            json={'minimo': 100, 'maximo': 1, 'quantidade': 1})
        assert response.status_code == 400
    
    def test_quantidade_excede_intervalo(self, client):
        """Testa quantidade maior que o intervalo sem repetição"""
        response = client.post('/sortear/numero',
            json={'minimo': 1, 'maximo': 5, 'quantidade': 10, 'permitir_repeticao': False})
        # Deve retornar erro ou lista com menos elementos
        data = json.loads(response.data)
        if 'erro' in data:
            assert response.status_code == 400
        else:
            assert len(data['resultado']) <= 5


class TestValidacoesNomes:
    """Testes de validação do sorteio de nomes"""
    
    def test_nomes_com_espacos(self, client):
        """Testa nomes com espaços em branco"""
        response = client.post('/sortear/nomes',
            json={'nomes': '  João  \n  Maria  \n  Pedro  ', 'quantidade': 1})
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['resultado']['nome'].strip() in ['João', 'Maria', 'Pedro']
    
    def test_linhas_vazias_ignoradas(self, client):
        """Testa que linhas vazias são ignoradas"""
        response = client.post('/sortear/nomes',
            json={'nomes': 'João\n\n\nMaria\n\n', 'quantidade': 1})
        assert response.status_code == 200


class TestValidacoesDados:
    """Testes de validação do sorteio de dados"""
    
    def test_todos_os_tipos_de_dados(self, client):
        """Testa todos os tipos de dados disponíveis"""
        tipos = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']
        
        for tipo in tipos:
            response = client.post('/sortear/dados',
                json={'tipo_dado': tipo, 'quantidade': 1})
            assert response.status_code == 200, f"Falha para {tipo}"
            
            data = json.loads(response.data)
            assert 1 <= data['resultado']['valores'][0] <= int(tipo[1:])
    
    def test_quantidade_maxima(self, client):
        """Testa quantidade máxima de dados (10)"""
        response = client.post('/sortear/dados',
            json={'tipo_dado': 'd6', 'quantidade': 10})
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data['resultado']['valores']) == 10
    
    def test_quantidade_acima_do_limite(self, client):
        """Testa quantidade acima do limite (10)"""
        response = client.post('/sortear/dados',
            json={'tipo_dado': 'd6', 'quantidade': 11})
        assert response.status_code == 400
