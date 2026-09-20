"""
Módulo com funções auxiliares para o sistema de sorteios.
"""

from typing import Dict, Any


def validar_parametros_numero(minimo: int, maximo: int, 
                              quantidade: int) -> Dict[str, Any]:
    """Valida os parâmetros para sorteio de números."""
    try:
        minimo = int(minimo)
        maximo = int(maximo)
        quantidade = int(quantidade)
        
        if minimo >= maximo:
            return {"valido": False, "erro": "Mínimo deve ser menor que máximo"}
        
        if quantidade <= 0:
            return {"valido": False, "erro": "Quantidade deve ser maior que zero"}
        
        return {"valido": True}
    except (ValueError, TypeError) as e:
        return {"valido": False, "erro": f"Parâmetros inválidos: {str(e)}"}


def validar_parametros_nomes(nomes: str, quantidade: int) -> Dict[str, Any]:
    """Valida os parâmetros para sorteio de nomes."""
    try:
        if "," in nomes:
            lista_nomes = [nome.strip() for nome in nomes.split(",")]
        else:
            lista_nomes = [nome.strip() for nome in nomes.split("\n")]
        
        lista_nomes = [nome for nome in lista_nomes if nome]
        
        if not lista_nomes:
            return {"valido": False, "erro": "Lista de nomes está vazia"}
        
        quantidade = int(quantidade)
        if quantidade <= 0:
            return {"valido": False, "erro": "Quantidade deve ser maior que zero"}
        
        if quantidade > len(lista_nomes):
            return {
                "valido": False, 
                "erro": f"Quantidade ({quantidade}) maior que número de nomes ({len(lista_nomes)})"
            }
        
        return {"valido": True, "nomes": lista_nomes}
    except (ValueError, TypeError) as e:
        return {"valido": False, "erro": f"Parâmetros inválidos: {str(e)}"}