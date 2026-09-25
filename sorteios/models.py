"""
Módulo responsável por definir as classes e lógica de cada tipo de sorteio.
"""

import random
from typing import List, Union, Dict, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class ResultadoSorteio:
    """Classe para padronizar o retorno dos sorteios"""
    tipo: str
    resultado: Any
    detalhes: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.detalhes is None:
            self.detalhes = {}


class SorteioBase(ABC):
    """Classe abstrata base para todos os tipos de sorteio"""
    
    @abstractmethod
    def realizar_sorteio(self) -> ResultadoSorteio:
        """Método abstrato que deve ser implementado por cada tipo de sorteio"""
        pass


class SorteioNumero(SorteioBase):
    """Classe para sorteio de números em um intervalo específico."""
    
    def __init__(self, minimo: int = 1, maximo: int = 100, 
                 quantidade: int = 1, permitir_repeticao: bool = True):
        self.minimo = minimo
        self.maximo = maximo
        self.quantidade = quantidade
        self.permitir_repeticao = permitir_repeticao
        
        if minimo >= maximo:
            raise ValueError("O valor mínimo deve ser menor que o máximo")
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero")
        if not permitir_repeticao:
            intervalo_disponivel = maximo - minimo + 1
            if quantidade > intervalo_disponivel:
                raise ValueError(f"Não é possível sortear {quantidade} números únicos no intervalo [{minimo}, {maximo}]")
    
    def realizar_sorteio(self) -> ResultadoSorteio:
        if self.permitir_repeticao:
            numeros = [random.randint(self.minimo, self.maximo) for _ in range(self.quantidade)]
        else:
            numeros = random.sample(range(self.minimo, self.maximo + 1), self.quantidade)
        
        return ResultadoSorteio(
            tipo="numero",
            resultado=numeros if len(numeros) > 1 else numeros[0],
            detalhes={"intervalo": [self.minimo, self.maximo], "quantidade": self.quantidade, "permitir_repeticao": self.permitir_repeticao}
        )


class SorteioNomes(SorteioBase):
    """Classe para sorteio de nomes com telefone opcional."""
    
    def __init__(self, participantes: List[Dict[str, str]], quantidade: int = 1, permitir_repeticao: bool = False):
        if not participantes:
            raise ValueError("A lista de participantes não pode estar vazia")
        self.participantes = participantes
        self.quantidade = quantidade
        self.permitir_repeticao = permitir_repeticao
        
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero")
        if not permitir_repeticao and quantidade > len(self.participantes):
            raise ValueError(f"Não é possível sortear {quantidade} nomes únicos de uma lista com {len(self.participantes)} participantes")
    
    def realizar_sorteio(self) -> ResultadoSorteio:
        if self.permitir_repeticao:
            sorteados = [random.choice(self.participantes) for _ in range(self.quantidade)]
        else:
            sorteados = random.sample(self.participantes, self.quantidade)
        
        return ResultadoSorteio(
            tipo="nomes",
            resultado=sorteados if len(sorteados) > 1 else sorteados[0],
            detalhes={"total_participantes": len(self.participantes), "quantidade": self.quantidade, "permitir_repeticao": self.permitir_repeticao}
        )


class SorteioCores(SorteioBase):
    """Classe para sorteio de cores."""
    
    CORES_PREDEFINIDAS = {
        "Vermelho": "#FF0000", "Verde": "#00FF00", "Azul": "#0000FF", "Amarelo": "#FFFF00",
        "Roxo": "#800080", "Laranja": "#FFA500", "Rosa": "#FFC0CB", "Ciano": "#00FFFF",
        "Magenta": "#FF00FF", "Marrom": "#A52A2A", "Preto": "#000000", "Branco": "#FFFFFF",
        "Cinza": "#808080", "Verde-oliva": "#808000", "Azul-marinho": "#000080"
    }
    
    def __init__(self, modo: str = "predefinidas", cores_custom: List[str] = None, quantidade: int = 1):
        self.modo = modo
        self.quantidade = quantidade
        
        if modo == "predefinidas":
            self.cores = list(self.CORES_PREDEFINIDAS.keys())
        elif modo == "custom":
            if not cores_custom:
                raise ValueError("Lista de cores customizadas não pode estar vazia")
            self.cores = cores_custom
        elif modo == "rgb":
            self.cores = None
        else:
            raise ValueError("Modo inválido. Use 'predefinidas', 'rgb' ou 'custom'")
        
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero")
    
    def _gerar_cor_rgb(self) -> dict:
        hex_cor = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return {"nome": "RGB Aleatório", "hex": hex_cor}
    
    def _obter_hex_cor(self, cor: str) -> str:
        if cor.startswith("#"):
            return cor.upper()
        return self.CORES_PREDEFINIDAS.get(cor, "#000000")
    
    def realizar_sorteio(self) -> ResultadoSorteio:
        cores_sorteadas = []
        for _ in range(self.quantidade):
            if self.modo == "rgb":
                cores_sorteadas.append(self._gerar_cor_rgb())
            else:
                nome_cor = random.choice(self.cores)
                hex_cor = self._obter_hex_cor(nome_cor)
                cores_sorteadas.append({"nome": nome_cor, "hex": hex_cor})
        
        return ResultadoSorteio(
            tipo="cores",
            resultado=cores_sorteadas if len(cores_sorteadas) > 1 else cores_sorteadas[0],
            detalhes={"modo": self.modo, "quantidade": self.quantidade}
        )


class SorteioDados(SorteioBase):
    """Classe para sorteio de dados."""
    
    TIPOS_DADOS = {"d4": 4, "d6": 6, "d8": 8, "d10": 10, "d12": 12, "d20": 20, "d100": 100}
    
    def __init__(self, tipo_dado: str = "d6", quantidade: int = 1):
        if tipo_dado not in self.TIPOS_DADOS:
            raise ValueError(f"Tipo de dado inválido. Use: {', '.join(self.TIPOS_DADOS.keys())}")
        self.tipo_dado = tipo_dado
        self.quantidade = quantidade
        self.faces = self.TIPOS_DADOS[tipo_dado]
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero")
    
    def realizar_sorteio(self) -> ResultadoSorteio:
        valores = [random.randint(1, self.faces) for _ in range(self.quantidade)]
        return ResultadoSorteio(
            tipo="dados",
            resultado={"valores": valores, "soma": sum(valores)},
            detalhes={"tipo_dado": self.tipo_dado, "faces": self.faces, "quantidade": self.quantidade}
        )


class SorteioBingo(SorteioBase):
    """Classe para sorteio de Bingo."""
    
    def __init__(self):
        self.todos_numeros = list(range(1, 76))
        self.numeros_sorteados = []
    
    def gerar_cartela(self) -> Dict[str, List[int]]:
        """Gera uma cartela de bingo aleatória."""
        return {
            'B': sorted(random.sample(range(1, 16), 5)),
            'I': sorted(random.sample(range(16, 31), 5)),
            'N': sorted(random.sample(range(31, 46), 4)),
            'G': sorted(random.sample(range(46, 61), 5)),
            'O': sorted(random.sample(range(61, 76), 5))
        }
    
    def sortear_numero(self) -> Dict[str, Any]:
        """Sorteia um número do bingo."""
        numeros_disponiveis = [n for n in self.todos_numeros if n not in self.numeros_sorteados]
        if not numeros_disponiveis:
            return {"numero": None, "letra": None, "fim": True}
        
        numero = random.choice(numeros_disponiveis)
        self.numeros_sorteados.append(numero)
        
        if 1 <= numero <= 15: letra = 'B'
        elif 16 <= numero <= 30: letra = 'I'
        elif 31 <= numero <= 45: letra = 'N'
        elif 46 <= numero <= 60: letra = 'G'
        else: letra = 'O'
        
        return {"numero": numero, "letra": letra, "total_sorteados": len(self.numeros_sorteados), "fim": False}
    
    def realizar_sorteio(self) -> ResultadoSorteio:
        resultado = self.sortear_numero()
        return ResultadoSorteio(
            tipo="bingo",
            resultado=resultado,
            detalhes={"total_numeros": 75, "numeros_sorteados": len(self.numeros_sorteados), "restantes": 75 - len(self.numeros_sorteados)}
        )