"""
Testes da aplicação Flask - Rotas e endpoints
"""
import pytest
import json


class TestRotasPrincipais:
    """Testes das rotas principais da aplicação"""
    
    def test_index(self, client):
        """Testa se a página inicial carrega corretamente"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Sistema de Sorteios' in response.data
    
    def test_index_contem_abas(self, client):
        """Testa se a página inicial contém todas as abas"""
        response = client.get('/')
        # Decodifica para UTF-8 para suportar caracteres acentuados
        html = response.data.decode('utf-8')
        assert 'Números' in html
        assert 'Nomes' in html
        assert 'Cores' in html
        assert 'Dados' in html
        assert 'Bingo' in html
    
    def test_api_version(self, client):
        """Testa o endpoint de versão"""
        response = client.get('/api/version')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'app_version' in data
        assert isinstance(data['app_version'], str)
        assert len(data['app_version'].split('.')) == 3


class TestSorteioNumeros:
    """Testes do sorteio de números"""
    
    def test_sortear_numero_simples(self, client):
        """Testa sorteio de um número"""
        response = client.post('/sortear/numero', 
            json={'minimo': 1, 'maximo': 100, 'quantidade': 1, 'permitir_repeticao': False})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['sucesso'] is True
        assert 1 <= data['resultado'] <= 100
    
    def test_sortear_multiplos_numeros(self, client):
        """Testa sorteio de múltiplos números"""
        response = client.post('/sortear/numero',
            json={'minimo': 1, 'maximo': 10, 'quantidade': 5, 'permitir_repeticao': False})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data['resultado']) == 5
        assert len(set(data['resultado'])) == 5  # Todos únicos
    
    def test_sortear_com_repeticao(self, client):
        """Testa sorteio com repetição permitida"""
        response = client.post('/sortear/numero',
            json={'minimo': 1, 'maximo': 5, 'quantidade': 10, 'permitir_repeticao': True})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data['resultado']) == 10
    
    def test_minimo_maior_que_maximo(self, client):
        """Testa validação: mínimo maior que máximo"""
        response = client.post('/sortear/numero',
            json={'minimo': 100, 'maximo': 1, 'quantidade': 1})
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'erro' in data
    
    def test_quantidade_zero(self, client):
        """Testa validação: quantidade zero"""
        response = client.post('/sortear/numero',
            json={'minimo': 1, 'maximo': 100, 'quantidade': 0})
        
        assert response.status_code == 200


class TestSorteioNomes:
    """Testes do sorteio de nomes"""
    
    def test_sortear_nome_simples(self, client):
        """Testa sorteio de um nome"""
        response = client.post('/sortear/nomes',
            json={'nomes': 'João\nMaria\nPedro', 'quantidade': 1, 'permitir_repeticao': False})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['sucesso'] is True
        assert data['resultado']['nome'] in ['João', 'Maria', 'Pedro']
    
    def test_sortear_nome_com_telefone(self, client):
        """Testa sorteio com telefone"""
        response = client.post('/sortear/nomes',
            json={'nomes': 'João - (11) 99999-9999\nMaria - (11) 88888-8888', 
                  'quantidade': 1, 'permitir_repeticao': False})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'telefone' in data['resultado']
    
    def test_lista_vazia(self, client):
        """Testa validação: lista vazia"""
        response = client.post('/sortear/nomes',
            json={'nomes': '', 'quantidade': 1})
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'erro' in data
    
    def test_multiplos_vencedores(self, client):
        """Testa sorteio de múltiplos vencedores"""
        response = client.post('/sortear/nomes',
            json={'nomes': 'João\nMaria\nPedro\nAna', 'quantidade': 2, 'permitir_repeticao': False})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data['resultado']) == 2


class TestSorteioCores:
    """Testes do sorteio de cores"""
    
    def test_cor_predefinida(self, client):
        """Testa sorteio de cor predefinida"""
        response = client.post('/sortear/cores',
            json={'modo': 'predefinidas', 'quantidade': 1})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'nome' in data['resultado']
        assert 'hex' in data['resultado']
    
    def test_cor_rgb(self, client):
        """Testa sorteio de cor RGB aleatória"""
        response = client.post('/sortear/cores',
            json={'modo': 'rgb', 'quantidade': 1})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['resultado']['hex'].startswith('#')
        assert len(data['resultado']['hex']) == 7
    
    def test_cor_customizada(self, client):
        """Testa sorteio de cor customizada"""
        response = client.post('/sortear/cores',
            json={'modo': 'custom', 'quantidade': 1, 'cores_custom': ['#FF0000', '#00FF00']})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['resultado']['hex'] in ['#FF0000', '#00FF00']


class TestSorteioDados:
    """Testes do sorteio de dados"""
    
    def test_dado_d6(self, client):
        """Testa dado de 6 faces"""
        response = client.post('/sortear/dados',
            json={'tipo_dado': 'd6', 'quantidade': 1})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 1 <= data['resultado']['valores'][0] <= 6
    
    def test_dado_d20(self, client):
        """Testa dado de 20 faces"""
        response = client.post('/sortear/dados',
            json={'tipo_dado': 'd20', 'quantidade': 1})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 1 <= data['resultado']['valores'][0] <= 20
    
    def test_multiplos_dados(self, client):
        """Testa múltiplos dados com soma"""
        response = client.post('/sortear/dados',
            json={'tipo_dado': 'd6', 'quantidade': 3})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data['resultado']['valores']) == 3
        assert data['resultado']['soma'] == sum(data['resultado']['valores'])
    
    def test_tipo_invalido(self, client):
        """Testa validação: tipo de dado inválido"""
        response = client.post('/sortear/dados',
            json={'tipo_dado': 'd99', 'quantidade': 1})
        
        assert response.status_code == 400


class TestBingo:
    """Testes do sistema de Bingo"""
    
    def test_iniciar_bingo(self, client):
        """Testa iniciar um novo jogo de bingo"""
        response = client.post('/bingo/iniciar')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['sucesso'] is True
    
    def test_sortear_numero_bingo(self, client):
        """Testa sortear número no bingo"""
        client.post('/bingo/iniciar')
        
        response = client.post('/bingo/sortear')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'numero' in data['resultado']
        assert 'letra' in data['resultado']
        assert data['resultado']['letra'] in ['B', 'I', 'N', 'G', 'O']
    
    def test_gerar_cartelas(self, client):
        """Testa geração de cartelas"""
        response = client.post('/bingo/gerar-cartelas',
            json={'quantidade': 2})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data['cartelas']) == 2
        
        cartela = data['cartelas'][0]
        assert 'B' in cartela
        assert 'I' in cartela
        assert 'N' in cartela
        assert 'G' in cartela
        assert 'O' in cartela
        
        assert all(1 <= n <= 15 for n in cartela['B'])
        assert all(16 <= n <= 30 for n in cartela['I'])
        assert all(31 <= n <= 45 for n in cartela['N'])
        assert all(46 <= n <= 60 for n in cartela['G'])
        assert all(61 <= n <= 75 for n in cartela['O'])
    
    def test_quantidade_cartelas_invalida(self, client):
        """Testa validação: quantidade de cartelas inválida"""
        response = client.post('/bingo/gerar-cartelas',
            json={'quantidade': 15})
        
        assert response.status_code == 400
