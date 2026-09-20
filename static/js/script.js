// ========== GERENCIAMENTO DE TEMAS ==========
function aplicarTema(tema) {
    const body = document.body;
    const botoes = document.querySelectorAll('.opcao-tema');
    
    body.classList.remove('tema-escuro');
    
    if (tema === 'escuro') {
        body.classList.add('tema-escuro');
    } else if (tema === 'sistema') {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            body.classList.add('tema-escuro');
        }
    }
    
    botoes.forEach(btn => {
        btn.classList.remove('selecionado');
        if (btn.dataset.tema === tema) {
            btn.classList.add('selecionado');
        }
    });
    
    localStorage.setItem('tema-preferido', tema);
}

function toggleMenuTema(event) {
    if (event) event.stopPropagation();
    const dropdown = document.getElementById('dropdownMenuTema');
    if (dropdown) {
        dropdown.classList.toggle('visivel');
    }
}

function mudarTema(tema) {
    aplicarTema(tema);
    const dropdown = document.getElementById('dropdownMenuTema');
    if (dropdown) {
        dropdown.classList.remove('visivel');
    }
}

document.addEventListener('click', function() {
    const dropdown = document.getElementById('dropdownMenuTema');
    if (dropdown) {
        dropdown.classList.remove('visivel');
    }
});

// ========== INICIALIZAÇÃO ==========
document.addEventListener('DOMContentLoaded', function() {
    const temaSalvo = localStorage.getItem('tema-preferido') || 'sistema';
    aplicarTema(temaSalvo);
    
    const modoCoresSelect = document.getElementById('modo-cores');
    if (modoCoresSelect) {
        modoCoresSelect.addEventListener('change', function(e) {
            const container = document.getElementById('cores-custom-container');
            if (container) {
                container.style.display = e.target.value === 'custom' ? 'block' : 'none';
            }
        });
    }
    
    if (window.matchMedia) {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function() {
            const temaAtual = localStorage.getItem('tema-preferido') || 'sistema';
            if (temaAtual === 'sistema') {
                aplicarTema('sistema');
            }
        });
    }
});

// ========== GERENCIAMENTO DE TABS ==========
function mudarTab(tipo) {
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.form-container').forEach(form => form.classList.remove('active'));
    
    const btnAtivo = document.querySelector(`.tab-btn[data-tipo="${tipo}"]`);
    if (btnAtivo) btnAtivo.classList.add('active');
    
    const formAtivo = document.getElementById(`form-${tipo}`);
    if (formAtivo) formAtivo.classList.add('active');
}

function toggleCoresCustom() {
    const modo = document.getElementById('modo-cores').value;
    const container = document.getElementById('cores-custom-container');
    if (container) {
        container.style.display = modo === 'custom' ? 'block' : 'none';
    }
}

// ========== FUNÇÃO PRINCIPAL DE SORTEIO ==========
async function realizarSorteio(tipo) {
    const resultadoDiv = document.getElementById('resultado-conteudo');
    const btnSortear = document.querySelector(`.btn-sortear[onclick*="'${tipo}'"]`);
    
    if (!btnSortear) return;
    
    btnSortear.disabled = true;
    const textoOriginal = btnSortear.textContent;
    btnSortear.textContent = 'Sorteando...';
    
    try {
        let dados = {};
        let url = '';
        
        switch(tipo) {
            case 'numero':
                dados = {
                    minimo: parseInt(document.getElementById('minimo').value),
                    maximo: parseInt(document.getElementById('maximo').value),
                    quantidade: parseInt(document.getElementById('quantidade-num').value),
                    permitir_repeticao: document.getElementById('permitir-repeticao-num').checked
                };
                url = '/sortear/numero';
                await animarNumeros(resultadoDiv, dados.minimo, dados.maximo, 3000);
                break;
                
            case 'nomes':
                dados = {
                    nomes: document.getElementById('nomes').value,
                    quantidade: parseInt(document.getElementById('quantidade-nomes').value),
                    permitir_repeticao: document.getElementById('permitir-repeticao-nomes').checked
                };
                url = '/sortear/nomes';
                await animarNomesRolagem(resultadoDiv, dados.nomes, 3000);
                break;
                
            case 'cores':
                dados = {
                    modo: document.getElementById('modo-cores').value,
                    quantidade: parseInt(document.getElementById('quantidade-cores').value)
                };
                if (dados.modo === 'custom') {
                    dados.cores_custom = document.getElementById('cores-custom').value
                        .split('\n')
                        .map(cor => cor.trim())
                        .filter(cor => cor);
                }
                url = '/sortear/cores';
                await animarCores(resultadoDiv, dados.modo, 3000);
                break;
                
            case 'dados':
                dados = {
                    tipo_dado: document.getElementById('tipo-dado').value,
                    quantidade: parseInt(document.getElementById('quantidade-dados').value)
                };
                url = '/sortear/dados';
                await animarDadosGirando(resultadoDiv, dados.quantidade, 3000);
                break;
        }
        
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dados)
        });
        
        const resultado = await response.json();
        
        if (resultado.erro) {
            resultadoDiv.innerHTML = `<p style="color: red; font-size: 1.2em;">❌ ${resultado.erro}</p>`;
            btnSortear.disabled = false;
            btnSortear.textContent = textoOriginal;
            return;
        }
        
        exibirResultado(resultado, tipo);
        
    } catch (error) {
        resultadoDiv.innerHTML = `<p style="color: red; font-size: 1.2em;">❌ Erro ao realizar sorteio: ${error.message}</p>`;
    } finally {
        btnSortear.disabled = false;
        btnSortear.textContent = textoOriginal;
    }
}

// ========== ANIMAÇÃO DE NÚMEROS ==========
function animarNumeros(container, minimo, maximo, duracao) {
    return new Promise(resolve => {
        const inicio = Date.now();
        function atualizar() {
            const agora = Date.now();
            if (agora - inicio < duracao) {
                const num = Math.floor(Math.random() * (maximo - minimo + 1)) + minimo;
                container.innerHTML = `<div class="resultado-numero animacao-selecao">${num}</div>`;
                requestAnimationFrame(atualizar);
            } else {
                resolve();
            }
        }
        atualizar();
    });
}

// ========== ANIMAÇÃO DE NOMES COM ROLAGEM (CORRIGIDA) ==========
function animarNomesRolagem(container, nomesStr, duracao) {
    return new Promise(resolve => {
        const nomes = nomesStr.split('\n').filter(n => n.trim());
        if (nomes.length === 0) { 
            resolve(); 
            return; 
        }
        
        const inicio = Date.now();
        
        function atualizar() {
            const agora = Date.now();
            const decorrido = agora - inicio;
            
            if (decorrido < duracao) {
                const nomeAleatorio = nomes[Math.floor(Math.random() * nomes.length)];
                const nomeExibicao = nomeAleatorio.split(' - ')[0].trim();
                
                // Mesma estrutura da animação de cores
                container.innerHTML = `
                    <div class="resultado-nome-item animacao-selecao" style="animation: selecaoPiscando 0.1s ease-in-out infinite;">
                        <div class="resultado-nome-texto" style="font-size: 2em; color: var(--text-primary);">
                            🎲 ${nomeExibicao}
                        </div>
                    </div>
                `;
                
                requestAnimationFrame(atualizar);
            } else {
                resolve();
            }
        }
        
        atualizar();
    });
}

// ========== ANIMAÇÃO DE CORES ==========
function animarCores(container, modo, duracao) {
    return new Promise(resolve => {
        const coresPredefinidas = ["Vermelho", "Verde", "Azul", "Amarelo", "Roxo", "Laranja", "Rosa", "Ciano", "Magenta", "Marrom", "Preto", "Branco", "Cinza"];
        const inicio = Date.now();
        function atualizar() {
            const agora = Date.now();
            if (agora - inicio < duracao) {
                let corNome, corHex;
                if (modo === 'rgb') {
                    corHex = `#${Math.floor(Math.random()*16777215).toString(16).padStart(6, '0')}`;
                    corNome = "RGB Aleatório";
                } else {
                    corNome = coresPredefinidas[Math.floor(Math.random() * coresPredefinidas.length)];
                    corHex = getHexCor(corNome);
                }
                container.innerHTML = `
                    <div class="resultado-cor animacao-selecao" style="background-color: ${corHex}; animation: selecaoPiscando 0.1s ease-in-out infinite;"></div>
                    <div class="cor-nome">${corNome}</div>`;
                requestAnimationFrame(atualizar);
            } else { resolve(); }
        }
        atualizar();
    });
}

// ========== ANIMAÇÃO DE DADOS ==========
function animarDadosGirando(container, quantidade, duracao) {
    return new Promise(resolve => {
        const inicio = Date.now();
        function atualizar() {
            const agora = Date.now();
            if (agora - inicio < duracao) {
                let html = '<div class="resultado-dados">';
                for (let i = 0; i < quantidade; i++) {
                    const valor = Math.floor(Math.random() * 6) + 1;
                    html += criarDadoHTML(valor, true);
                }
                html += '</div>';
                container.innerHTML = html;
                requestAnimationFrame(atualizar);
            } else { resolve(); }
        }
        atualizar();
    });
}

// ========== FUNÇÕES AUXILIARES ==========
function getHexCor(nome) {
    const cores = {
        "Vermelho": "#FF0000", "Verde": "#00FF00", "Azul": "#0000FF",
        "Amarelo": "#FFFF00", "Roxo": "#800080", "Laranja": "#FFA500",
        "Rosa": "#FFC0CB", "Ciano": "#00FFFF", "Magenta": "#FF00FF",
        "Marrom": "#A52A2A", "Preto": "#000000", "Branco": "#FFFFFF", "Cinza": "#808080"
    };
    return cores[nome] || "#000000";
}

function criarDadoHTML(valor, girando = false) {
    const classesGirando = girando ? 'dado-girando' : '';
    return `<div class="dado-tradicional dado-${valor} ${classesGirando}">${Array(9).fill('<div class="ponto-dado"></div>').join('')}</div>`;
}

function exibirResultado(resultado, tipo) {
    const resultadoDiv = document.getElementById('resultado-conteudo');
    let html = '';
    
    switch(tipo) {
        case 'numero':
            if (Array.isArray(resultado.resultado)) {
                html = resultado.resultado.map(num => `<div class="resultado-numero">${num}</div>`).join('');
            } else {
                html = `<div class="resultado-numero">${resultado.resultado}</div>`;
            }
            break;
        case 'nomes':
            const nomes = Array.isArray(resultado.resultado) ? resultado.resultado : [resultado.resultado];
            html = nomes.map(p => `
                <div class="resultado-nome-item">
                    <div class="resultado-nome-texto">🎉 ${p.nome}</div>
                    ${p.telefone ? `<div class="resultado-telefone">📱 ${p.telefone}</div>` : ''}
                </div>`).join('');
            break;
        case 'cores':
            const cores = Array.isArray(resultado.resultado) ? resultado.resultado : [resultado.resultado];
            html = cores.map(cor => `
                <div class="resultado-cor" style="background-color: ${cor.hex}"></div>
                <div class="cor-nome">${cor.nome}</div>`).join('<hr style="margin: 30px 0; border: none; border-top: 2px solid var(--border-color);">');
            break;
        case 'dados':
            const valores = resultado.resultado.valores;
            const soma = resultado.resultado.soma;
            html = '<div class="resultado-dados">';
            valores.forEach(valor => { html += criarDadoHTML(valor, false); });
            html += '</div>';
            if (valores.length > 1) { html += `<div class="dado-soma">Soma: ${soma}</div>`; }
            break;
    }
    resultadoDiv.innerHTML = html;
}

// ========== LÓGICA DO BINGO ==========
let bingoAtivo = false;
let cartelasGeradas = [];

async function gerarEImprimirCartelas() {
    const qtd = parseInt(document.getElementById('qtd-cartelas').value) || 1;
    
    if (qtd < 1 || qtd > 10) {
        alert('Quantidade deve ser entre 1 e 10');
        return;
    }
    
    try {
        const response = await fetch('/bingo/gerar-cartelas', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ quantidade: qtd })
        });
        
        const data = await response.json();
        
        if (data.erro) { 
            alert(data.erro); 
            return; 
        }
        
        cartelasGeradas = data.cartelas;
        prepararImpressao();
    } catch (error) { 
        alert('Erro ao gerar cartelas: ' + error.message); 
    }
}

function prepararImpressao() {
    if (cartelasGeradas.length === 0) {
        alert('Gere cartelas primeiro!');
        return;
    }
    
    const areaImpressao = document.getElementById('area-impressao');
    let html = '';
    
    const cartelasPorPagina = 4;
    const totalPaginas = Math.ceil(cartelasGeradas.length / cartelasPorPagina);
    
    for (let pagina = 0; pagina < totalPaginas; pagina++) {
        html += '<div class="pagina-a4">';
        html += '<div class="cartelas-grid-impressao">';
        
        const inicio = pagina * cartelasPorPagina;
        const fim = Math.min(inicio + cartelasPorPagina, cartelasGeradas.length);
        
        for (let i = inicio; i < fim; i++) {
            const cartela = cartelasGeradas[i];
            html += `<div class="cartela-bingo-impressao">`;
            
            // Cabeçalho B-I-N-G-O
            ['B', 'I', 'N', 'G', 'O'].forEach(letra => {
                html += `<div class="cartela-cabecalho">${letra}</div>`;
            });
            
            // 5 linhas de números
            for (let row = 0; row < 5; row++) {
                html += `<div class="cartela-celula">${cartela.B[row]}</div>`;
                html += `<div class="cartela-celula">${cartela.I[row]}</div>`;
                
                if (row === 2) {
                    html += `<div class="cartela-celula livre">★</div>`;
                } else {
                    const indexN = row < 2 ? row : row - 1;
                    html += `<div class="cartela-celula">${cartela.N[indexN]}</div>`;
                }
                
                html += `<div class="cartela-celula">${cartela.G[row]}</div>`;
                html += `<div class="cartela-celula">${cartela.O[row]}</div>`;
            }
            
            html += '</div>';
        }
        
        html += '</div></div>';
    }
    
    areaImpressao.innerHTML = html;
    
    setTimeout(() => {
        window.print();
    }, 100);
}

async function iniciarBingo() {
    try {
        const response = await fetch('/bingo/iniciar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        
        const data = await response.json();
        
        if (data.sucesso) {
            bingoAtivo = true;
            
            const btnIniciar = document.getElementById('btnIniciarBingo');
            const btnSortear = document.getElementById('btnSortearBingo');
            const totalSorteados = document.getElementById('totalSorteados');
            const letraBingo = document.getElementById('letraBingo');
            const numeroBingo = document.getElementById('numeroBingo');
            const bolaNumero = document.getElementById('bolaNumeroDisplay');
            
            if (btnIniciar) btnIniciar.disabled = true;
            if (btnSortear) btnSortear.disabled = false;
            if (totalSorteados) totalSorteados.textContent = '0';
            if (letraBingo) letraBingo.textContent = '-';
            if (numeroBingo) numeroBingo.textContent = '-';
            if (bolaNumero) bolaNumero.textContent = '?';
            
            inicializarQuadroNumeros();
        }
    } catch (error) { 
        alert('Erro ao iniciar bingo: ' + error.message); 
    }
}

function inicializarQuadroNumeros() {
    ['B', 'I', 'N', 'G', 'O'].forEach(letra => {
        const container = document.getElementById(`numeros-${letra}`);
        if (!container) return;
        
        container.innerHTML = '';
        
        let inicio, fim;
        if (letra === 'B') { inicio = 1; fim = 15; }
        else if (letra === 'I') { inicio = 16; fim = 30; }
        else if (letra === 'N') { inicio = 31; fim = 45; }
        else if (letra === 'G') { inicio = 46; fim = 60; }
        else { inicio = 61; fim = 75; }
        
        for (let num = inicio; num <= fim; num++) {
            const div = document.createElement('div');
            div.className = 'numero-bingo-item';
            div.textContent = num;
            div.id = `num-${num}`;
            container.appendChild(div);
        }
    });
}

async function sortearNumeroBingo() {
    if (!bingoAtivo) return;
    
    const globo = document.getElementById('globoBingoTradicional');
    const btnSortear = document.getElementById('btnSortearBingo');
    const bolaNumero = document.getElementById('bolaNumeroDisplay');
    const letraBingo = document.getElementById('letraBingo');
    const numeroBingo = document.getElementById('numeroBingo');
    const totalSorteados = document.getElementById('totalSorteados');
    
    if (globo) globo.classList.add('girando');
    if (btnSortear) btnSortear.disabled = true;
    
    try {
        await new Promise(resolve => setTimeout(resolve, 3000));
        
        const response = await fetch('/bingo/sortear', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        
        const data = await response.json();
        
        if (globo) globo.classList.remove('girando');
        
        if (data.erro) { 
            alert(data.erro); 
            if (btnSortear) btnSortear.disabled = false;
            return; 
        }
        
        if (data.resultado.numero !== null) {
            const numero = data.resultado.numero;
            const letra = data.resultado.letra;
            
            if (bolaNumero) bolaNumero.textContent = numero;
            if (letraBingo) letraBingo.textContent = letra;
            if (numeroBingo) numeroBingo.textContent = numero;
            if (totalSorteados) totalSorteados.textContent = data.resultado.total_sorteados;
            
            const numeroElement = document.getElementById(`num-${numero}`);
            if (numeroElement) {
                numeroElement.classList.add('sorteado');
            }
            
            if (data.resultado.fim) {
                alert('Todos os números foram sorteados!');
                bingoAtivo = false;
                if (document.getElementById('btnIniciarBingo')) document.getElementById('btnIniciarBingo').disabled = false;
                if (btnSortear) btnSortear.disabled = true;
            } else {
                if (btnSortear) btnSortear.disabled = false;
            }
        }
    } catch (error) {
        if (globo) globo.classList.remove('girando');
        if (btnSortear) btnSortear.disabled = false;
        alert('Erro ao sortear número: ' + error.message);
    }
}

function reiniciarBingo() {
    bingoAtivo = false;
    
    const btnIniciar = document.getElementById('btnIniciarBingo');
    const btnSortear = document.getElementById('btnSortearBingo');
    const totalSorteados = document.getElementById('totalSorteados');
    const letraBingo = document.getElementById('letraBingo');
    const numeroBingo = document.getElementById('numeroBingo');
    const bolaNumero = document.getElementById('bolaNumeroDisplay');
    const globo = document.getElementById('globoBingoTradicional');
    
    if (btnIniciar) btnIniciar.disabled = false;
    if (btnSortear) btnSortear.disabled = true;
    if (totalSorteados) totalSorteados.textContent = '0';
    if (letraBingo) letraBingo.textContent = '-';
    if (numeroBingo) numeroBingo.textContent = '-';
    if (bolaNumero) bolaNumero.textContent = '?';
    if (globo) globo.classList.remove('girando');
    
    ['B', 'I', 'N', 'G', 'O'].forEach(letra => {
        const container = document.getElementById(`numeros-${letra}`);
        if (container) container.innerHTML = '';
    });
}