# app.py
"""
Aplicação Flask principal que serve a interface web e gerencia as rotas.
"""

from flask import Flask, render_template, request, jsonify
from sorteios.models import (
    SorteioNumero,
    SorteioNomes,
    SorteioCores,
    SorteioDados,
    SorteioBingo
)
from sorteios.utils import validar_parametros_numero, validar_parametros_nomes

app = Flask(__name__)

jogo_bingo_atual = None


@app.route("/")
def index():
    """Rota principal que renderiza a página inicial"""
    return render_template("index.html")


@app.route("/sortear/numero", methods=["POST"])
def sortear_numero():
    """Endpoint para sorteio de números."""
    try:
        dados = request.get_json()
        
        minimo = dados.get("minimo", 1)
        maximo = dados.get("maximo", 100)
        quantidade = dados.get("quantidade", 1)
        permitir_repeticao = dados.get("permitir_repeticao", True)
        
        validacao = validar_parametros_numero(minimo, maximo, quantidade)
        if not validacao["valido"]:
            return jsonify({"erro": validacao["erro"]}), 400
        
        sorteio = SorteioNumero(minimo, maximo, quantidade, permitir_repeticao)
        resultado = sorteio.realizar_sorteio()
        
        return jsonify({
            "sucesso": True,
            "tipo": resultado.tipo,
            "resultado": resultado.resultado,
            "detalhes": resultado.detalhes
        })
        
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route("/sortear/nomes", methods=["POST"])
def sortear_nomes():
    """Endpoint para sorteio de nomes com telefone opcional."""
    try:
        dados = request.get_json()
        
        nomes_str = dados.get("nomes", "")
        quantidade = dados.get("quantidade", 1)
        permitir_repeticao = dados.get("permitir_repeticao", False)
        
        participantes = []
        for linha in nomes_str.split('\n'):
            linha = linha.strip()
            if not linha:
                continue
            
            if ' - ' in linha:
                partes = linha.split(' - ', 1)
                nome = partes[0].strip()
                telefone = partes[1].strip() if len(partes) > 1 else ""
                participantes.append({"nome": nome, "telefone": telefone})
            else:
                participantes.append({"nome": linha, "telefone": ""})
        
        if not participantes:
            return jsonify({"erro": "Lista de participantes está vazia"}), 400
        
        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError()
        except:
            return jsonify({"erro": "Quantidade inválida"}), 400
        
        if not permitir_repeticao and quantidade > len(participantes):
            return jsonify({
                "erro": f"Quantidade ({quantidade}) maior que número de participantes ({len(participantes)})"
            }), 400
        
        sorteio = SorteioNomes(participantes, quantidade, permitir_repeticao)
        resultado = sorteio.realizar_sorteio()
        
        return jsonify({
            "sucesso": True,
            "tipo": resultado.tipo,
            "resultado": resultado.resultado,
            "detalhes": resultado.detalhes
        })
        
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route("/sortear/cores", methods=["POST"])
def sortear_cores():
    """Endpoint para sorteio de cores."""
    try:
        dados = request.get_json()
        
        modo = dados.get("modo", "predefinidas")
        quantidade = dados.get("quantidade", 1)
        cores_custom = dados.get("cores_custom", None)
        
        sorteio = SorteioCores(modo, cores_custom, quantidade)
        resultado = sorteio.realizar_sorteio()
        
        return jsonify({
            "sucesso": True,
            "tipo": resultado.tipo,
            "resultado": resultado.resultado,
            "detalhes": resultado.detalhes
        })
        
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route("/sortear/dados", methods=["POST"])
def sortear_dados():
    """Endpoint para sorteio de dados."""
    try:
        dados = request.get_json()
        
        tipo_dado = dados.get("tipo_dado", "d6")
        quantidade = dados.get("quantidade", 1)
        
        sorteio = SorteioDados(tipo_dado, quantidade)
        resultado = sorteio.realizar_sorteio()
        
        return jsonify({
            "sucesso": True,
            "tipo": resultado.tipo,
            "resultado": resultado.resultado,
            "detalhes": resultado.detalhes
        })
        
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route("/bingo/gerar-cartelas", methods=["POST"])
def gerar_cartelas_bingo():
    """Gera múltiplas cartelas de bingo (4 por folha A4)."""
    try:
        dados = request.get_json()
        quantidade_folhas = dados.get("quantidade", 1)
        
        if quantidade_folhas < 1 or quantidade_folhas > 10:
            return jsonify({"erro": "Quantidade deve ser entre 1 e 10"}), 400
        
        total_cartelas = quantidade_folhas * 4
        sorteio = SorteioBingo()
        cartelas = [sorteio.gerar_cartela() for _ in range(total_cartelas)]
        
        return jsonify({
            "sucesso": True,
            "cartelas": cartelas,
            "total_folhas": quantidade_folhas
        })
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route("/bingo/iniciar", methods=["POST"])
def iniciar_bingo():
    """Inicia um novo jogo de bingo."""
    global jogo_bingo_atual
    try:
        jogo_bingo_atual = SorteioBingo()
        
        return jsonify({
            "sucesso": True,
            "mensagem": "Bingo iniciado!"
        })
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route("/bingo/sortear", methods=["POST"])
def sortear_numero_bingo():
    """Sorteia um número de bingo."""
    global jogo_bingo_atual
    try:
        if jogo_bingo_atual is None:
            return jsonify({"erro": "Bingo não foi iniciado. Clique em 'Iniciar Bingo' primeiro."}), 400
        
        resultado = jogo_bingo_atual.realizar_sorteio()
        
        return jsonify({
            "sucesso": True,
            "resultado": resultado.resultado,
            "detalhes": resultado.detalhes
        })
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)