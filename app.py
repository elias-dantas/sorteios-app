"""
Sistema de Sorteios - Aplicação Flask
Versão: Lida do arquivo VERSION
"""
import os
import random
from datetime import datetime
from flask import Flask, render_template, request, jsonify

# ========== INICIALIZAÇÃO ==========
app = Flask(__name__)

# ========== VERSIONAMENTO ==========
def get_version_file_path():
    """Retorna o caminho absoluto do arquivo VERSION"""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'VERSION')

def get_version():
    """Lê a versão do arquivo VERSION"""
    try:
        with open(get_version_file_path(), 'r') as f:
            version = f.read().strip()
            # Valida formato MAJOR.MINOR.PATCH
            if len(version.split('.')) == 3:
                return version
            return '0.0.0'
    except FileNotFoundError:
        return '0.0.0'

def get_build_info():
    """Retorna informações completas de build"""
    return {
        'app_version': get_version(),
        'build_date': datetime.now().strftime('%d/%m/%Y %H:%M'),
        'environment': os.environ.get('FLASK_ENV', 'production'),
        'python_version': os.sys.version.split()[0]
    }

@app.context_processor
def inject_build_info():
    """Disponibiliza informações de build para todos os templates"""
    return get_build_info()

# ========== ESTADO DO BINGO ==========
jogo_bingo_atual = None

def iniciar_novo_bingo():
    global jogo_bingo_atual
    jogo_bingo_atual = {
        'numeros_sorteados': [],
        'ativo': True
    }

# Inicializa o jogo ao iniciar a aplicação
iniciar_novo_bingo()

# ========== ROTAS PRINCIPAIS ==========
@app.route('/')
def index():
    return render_template('index.html')

# ========== API DE SORTEIOS ==========

@app.route('/sortear/numero', methods=['POST'])
def sortear_numero():
    try:
        dados = request.json
        minimo = int(dados.get('minimo', 1))
        maximo = int(dados.get('maximo', 100))
        quantidade = int(dados.get('quantidade', 1))
        permitir_repeticao = dados.get('permitir_repeticao', False)
        
        if minimo >= maximo:
            return jsonify({'erro': 'Valor mínimo deve ser menor que o máximo'}), 400
        
        if quantidade < 1:
            return jsonify({'erro': 'Quantidade deve ser pelo menos 1'}), 400
        
        if not permitir_repeticao and quantidade > (maximo - minimo + 1):
            return jsonify({'erro': 'Quantidade maior que o intervalo disponível'}), 400
        
        resultados = []
        numeros_disponiveis = list(range(minimo, maximo + 1))
        
        for _ in range(quantidade):
            if not numeros_disponiveis:
                break
            numero = random.choice(numeros_disponiveis)
            resultados.append(numero)
            if not permitir_repeticao:
                numeros_disponiveis.remove(numero)
        
        if quantidade == 1:
            return jsonify({
                'sucesso': True,
                'tipo': 'numero',
                'resultado': resultados[0],
                'detalhes': {
                    'intervalo': [minimo, maximo],
                    'quantidade': quantidade,
                    'permitir_repeticao': permitir_repeticao
                }
            })
        
        return jsonify({
            'sucesso': True,
            'tipo': 'numero',
            'resultado': resultados,
            'detalhes': {
                'intervalo': [minimo, maximo],
                'quantidade': quantidade,
                'permitir_repeticao': permitir_repeticao
            }
        })
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/sortear/nomes', methods=['POST'])
def sortear_nomes():
    try:
        dados = request.json
        nomes_str = dados.get('nomes', '')
        quantidade = int(dados.get('quantidade', 1))
        permitir_repeticao = dados.get('permitir_repeticao', False)
        
        nomes = [n.strip() for n in nomes_str.split('\n') if n.strip()]
        
        if not nomes:
            return jsonify({'erro': 'Lista de nomes vazia'}), 400
        
        if quantidade > len(nomes) and not permitir_repeticao:
            return jsonify({'erro': 'Quantidade maior que o número de participantes'}), 400
        
        resultados = []
        nomes_disponiveis = nomes.copy()
        
        for _ in range(quantidade):
            if not nomes_disponiveis:
                break
            nome_escolhido = random.choice(nomes_disponiveis)
            
            # Parse nome e telefone
            if ' - ' in nome_escolhido:
                partes = nome_escolhido.split(' - ', 1)
                nome = partes[0].strip()
                telefone = partes[1].strip()
            else:
                nome = nome_escolhido
                telefone = None
            
            resultados.append({'nome': nome, 'telefone': telefone})
            
            if not permitir_repeticao:
                nomes_disponiveis.remove(nome_escolhido)
        
        return jsonify({
            'sucesso': True,
            'tipo': 'nomes',
            'resultado': resultados if quantidade > 1 else resultados[0],
            'detalhes': {
                'total_participantes': len(nomes),
                'quantidade': quantidade,
                'permitir_repeticao': permitir_repeticao
            }
        })
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/sortear/cores', methods=['POST'])
def sortear_cores():
    try:
        dados = request.json
        modo = dados.get('modo', 'predefinidas')
        quantidade = int(dados.get('quantidade', 1))
        cores_custom = dados.get('cores_custom', [])
        
        cores_predefinidas = [
            {'nome': 'Vermelho', 'hex': '#FF0000'},
            {'nome': 'Verde', 'hex': '#00FF00'},
            {'nome': 'Azul', 'hex': '#0000FF'},
            {'nome': 'Amarelo', 'hex': '#FFFF00'},
            {'nome': 'Roxo', 'hex': '#800080'},
            {'nome': 'Laranja', 'hex': '#FFA500'},
            {'nome': 'Rosa', 'hex': '#FFC0CB'},
            {'nome': 'Ciano', 'hex': '#00FFFF'},
            {'nome': 'Magenta', 'hex': '#FF00FF'},
            {'nome': 'Marrom', 'hex': '#A52A2A'},
            {'nome': 'Preto', 'hex': '#000000'},
            {'nome': 'Branco', 'hex': '#FFFFFF'},
            {'nome': 'Cinza', 'hex': '#808080'},
            {'nome': 'Dourado', 'hex': '#FFD700'},
            {'nome': 'Prata', 'hex': '#C0C0C0'}
        ]
        
        resultados = []
        
        for _ in range(quantidade):
            if modo == 'predefinidas':
                cor = random.choice(cores_predefinidas)
                resultados.append(cor)
            elif modo == 'rgb':
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                hex_cor = f'#{r:02x}{g:02x}{b:02x}'.upper()
                resultados.append({'nome': 'RGB Aleatório', 'hex': hex_cor})
            elif modo == 'custom' and cores_custom:
                cor_hex = random.choice(cores_custom)
                resultados.append({'nome': cor_hex, 'hex': cor_hex})
            else:
                cor = random.choice(cores_predefinidas)
                resultados.append(cor)
        
        return jsonify({
            'sucesso': True,
            'tipo': 'cores',
            'resultado': resultados if quantidade > 1 else resultados[0],
            'detalhes': {
                'modo': modo,
                'quantidade': quantidade
            }
        })
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/sortear/dados', methods=['POST'])
def sortear_dados():
    try:
        dados = request.json
        tipo_dado = dados.get('tipo_dado', 'd6')
        quantidade = int(dados.get('quantidade', 1))
        
        faces = {
            'd4': 4, 'd6': 6, 'd8': 8, 'd10': 10,
            'd12': 12, 'd20': 20, 'd100': 100
        }
        
        if tipo_dado not in faces:
            return jsonify({'erro': 'Tipo de dado inválido'}), 400
        
        if quantidade < 1 or quantidade > 10:
            return jsonify({'erro': 'Quantidade deve ser entre 1 e 10'}), 400
        
        num_faces = faces[tipo_dado]
        valores = [random.randint(1, num_faces) for _ in range(quantidade)]
        soma = sum(valores)
        
        return jsonify({
            'sucesso': True,
            'tipo': 'dados',
            'resultado': {
                'tipo': tipo_dado,
                'faces': num_faces,
                'valores': valores,
                'soma': soma
            },
            'detalhes': {
                'quantidade': quantidade
            }
        })
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# ========== API DO BINGO ==========

@app.route('/bingo/iniciar', methods=['POST'])
def bingo_iniciar():
    global jogo_bingo_atual
    iniciar_novo_bingo()
    return jsonify({
        'sucesso': True,
        'mensagem': 'Bingo iniciado!'
    })

@app.route('/bingo/sortear', methods=['POST'])
def bingo_sortear():
    global jogo_bingo_atual
    
    if not jogo_bingo_atual or not jogo_bingo_atual.get('ativo'):
        return jsonify({'erro': 'Bingo não está ativo. Inicie um novo jogo.'}), 400
    
    numeros_sorteados = jogo_bingo_atual['numeros_sorteados']
    
    if len(numeros_sorteados) >= 75:
        jogo_bingo_atual['ativo'] = False
        return jsonify({'erro': 'Todos os 75 números já foram sorteados!'}), 400
    
    # Sortear número não repetido
    numeros_disponiveis = [n for n in range(1, 76) if n not in numeros_sorteados]
    numero_sorteado = random.choice(numeros_disponiveis)
    numeros_sorteados.append(numero_sorteado)
    
    # Determinar letra
    if numero_sorteado <= 15:
        letra = 'B'
    elif numero_sorteado <= 30:
        letra = 'I'
    elif numero_sorteado <= 45:
        letra = 'N'
    elif numero_sorteado <= 60:
        letra = 'G'
    else:
        letra = 'O'
    
    return jsonify({
        'sucesso': True,
        'resultado': {
            'numero': numero_sorteado,
            'letra': letra,
            'total_sorteados': len(numeros_sorteados),
            'fim': len(numeros_sorteados) >= 75
        },
        'detalhes': {
            'total_numeros': 75,
            'numeros_sorteados': len(numeros_sorteados),
            'restantes': 75 - len(numeros_sorteados)
        }
    })

@app.route('/bingo/gerar-cartelas', methods=['POST'])
def bingo_gerar_cartelas():
    try:
        dados = request.json
        quantidade = int(dados.get('quantidade', 1))
        
        if quantidade < 1 or quantidade > 10:
            return jsonify({'erro': 'Quantidade deve ser entre 1 e 10'}), 400
        
        cartelas = []
        
        for _ in range(quantidade):
            cartela = {
                'B': random.sample(range(1, 16), 5),
                'I': random.sample(range(16, 31), 5),
                'N': random.sample(range(31, 46), 4),  # 4 números (espaço livre no meio)
                'G': random.sample(range(46, 61), 5),
                'O': random.sample(range(61, 76), 5)
            }
            cartelas.append(cartela)
        
        return jsonify({
            'sucesso': True,
            'cartelas': cartelas,
            'total_folhas': quantidade
        })
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# ========== ROTA DE VERSÃO (API) ==========
@app.route('/api/version', methods=['GET'])
def api_version():
    """Endpoint para consultar a versão atual"""
    return jsonify(get_build_info())

# ========== INICIALIZAÇÃO ==========
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"\n{'='*50}")
    print(f"🎲 Sistema de Sorteios v{get_version()}")
    print(f"📅 Build: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"🌍 Ambiente: {os.environ.get('FLASK_ENV', 'production')}")
    print(f"🐍 Python: {os.sys.version.split()[0]}")
    print(f"{'='*50}\n")
    app.run(host='0.0.0.0', port=port, debug=False)