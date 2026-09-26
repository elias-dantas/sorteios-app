// ========== GERENCIAMENTO DE TEMAS ==========
function toggleMenuTema(event) {
    event.stopPropagation();
    const dropdown = document.getElementById('dropdownMenuTema');
    dropdown.classList.toggle('visivel');
}

document.addEventListener('click', function(event) {
    const dropdown = document.getElementById('dropdownMenuTema');
    if (dropdown && !dropdown.contains(event.target)) {
        dropdown.classList.remove('visivel');
    }
});

function mudarTema(tema) {
    document.body.className = '';
    if (tema === 'escuro') {
        document.body.classList.add('tema-escuro');
    }
    localStorage.setItem('tema', tema);
    atualizarSelecaoTema(tema);
    document.getElementById('dropdownMenuTema').classList.remove('visivel');
}

function atualizarSelecaoTema(tema) {
    document.querySelectorAll('.opcao-tema').forEach(btn => {
        btn.classList.remove('selecionado');
        if (btn.dataset.tema === tema) {
            btn.classList.add('selecionado');
        }
    });
}

function carregarTema() {
    const temaSalvo = localStorage.getItem('tema') || 'sistema';
    if (temaSalvo === 'escuro') {
        document.body.classList.add('tema-escuro');
    } else if (temaSalvo === 'sistema') {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.body.classList.add('tema-escuro');
        }
    }
    atualizarSelecaoTema(temaSalvo);
}

// ========== GERENCIAMENTO DE TABS ==========
function mudarTab(tipo) {
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.form-container').forEach(form => form.classList.remove('active'));
    document.querySelector(`[data-tipo="${tipo}"]`).classList.add('active');
    document.getElementById(`form-${tipo}`).classList.add('active');
}

// ========== TOGGLE CORES CUSTOM ==========
function toggleCoresCustom() {
    const modo = document.getElementById('modo-cores').value;
    const container = document.getElementById('cores-custom-container');
    container.style.display = modo === 'custom' ? 'block' : 'none';
}

// ========== REALIZAR SORTEIO ==========
async function realizarSorteio(tipo) {
    const resultadoDiv = document.getElementById('resultado-conteudo');
    resultadoDiv.innerHTML = '<p class="placeholder">Sorteando...</p>';
    
    try {
        let url = '';
        let dados = {};
        
        switch(tipo) {
            case 'numero':
                url = '/sortear/numero';
                dados = {
                    minimo: parseInt(document.getElementById('minimo').value),
                    maximo: parseInt(document.getElementById('maximo').value),
                    quantidade: parseInt(document.getElementById('quantidade-num').value),
                    permitir_repeticao: document.getElementById('permitir-repeticao-num').checked
                };
                break;
            case 'nomes':
                url = '/sortear/nomes';
                dados = {
                    nomes: document.getElementById('nomes').value,
                    quantidade: parseInt(document.getElementById('quantidade-nomes').value),
                    permitir_repeticao: document.getElementById('permitir-repeticao-nomes').checked
                };
                break;
            case 'cores':
                url = '/sortear/cores';
                dados = {
                    modo: document.getElementById('modo-cores').value,
                    quantidade: parseInt(document.getElementById('quantidade-cores').value),
                    cores_custom: document.getElementById('cores-custom').value.split('\n').filter(c => c.trim())
                };
                break;
            case 'dados':
                url = '/sortear/dados';
                dados = {
                    tipo_dado: document.getElementById('tipo-dado').value,
                    quantidade: parseInt(document.getElementById('quantidade-dados').value)
                };
                break;
        }
        
        // Animação antes do resultado
        if (tipo === 'numero') {
            await animarNumerosRolagem(resultadoDiv, dados.minimo, dados.maximo, 3000);
        } else if (tipo === 'nomes') {
            await animarNomesRolagem(resultadoDiv, dados.nomes, 3000);
        } else if (tipo === 'cores') {
            await animarCores(resultadoDiv, dados.modo, 3000);
        } else if (tipo === 'dados') {
            await animarDadosGirando(resultadoDiv, dados.quantidade, 3000);
        }
        
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dados)
        });
        
        const resultado = await response.json();
        
        if (resultado.erro) {
            resultadoDiv.innerHTML = `<p style="color: red;">Erro: ${resultado.erro}</p>`;
            return;
        }
        
        exibirResultado(resultado, tipo);
        
    } catch (error) {
        resultadoDiv.innerHTML = `<p style="color: red;">Erro: ${error.message}</p>`;
    }
}

// ========== ANIMAÇÃO DE NÚMEROS ==========
function animarNumerosRolagem(container, min, max, duracao) {
    return new Promise(resolve => {
        const inicio = Date.now();
        function atualizar() {
            const agora = Date.now();
            if (agora - inicio < duracao) {
                const numeroAleatorio = Math.floor(Math.random() * (max - min + 1)) + min;
                container.innerHTML = `<div class="resultado-numero animacao-selecao">${numeroAleatorio}</div>`;
                requestAnimationFrame(atualizar);
            } else {
                resolve();
            }
        }
        atualizar();
    });
}

// ========== ANIMAÇÃO DE NOMES ==========
function animarNomesRolagem(container, nomesStr, duracao) {
    return new Promise(resolve => {
        const nomes = nomesStr.split('\n').filter(n => n.trim());
        if (nomes.length === 0) { resolve(); return; }
        
        const inicio = Date.now();
        
        function atualizar() {
            const agora = Date.now();
            const decorrido = agora - inicio;
            
            if (decorrido < duracao) {
                const nomeAleatorio = nomes[Math.floor(Math.random() * nomes.length)];
                const nomeExibicao = nomeAleatorio.split(' - ')[0].trim();
                
                container.innerHTML = `
                    <div class="resultado-nome-item animacao-selecao" style="animation: selecaoPiscando 0.1s ease-in-out infinite;">
                        <div class="resultado-nome-texto" style="font-size: 2em; color: var(--text-primary);">
                             ${nomeExibicao}
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

// ========== GLOBO DE BINGO - GERAR BOLAS ==========
function gerarBolasGlobo() {
    const container = document.getElementById('bolasContainer');
    if (!container) return;
    
    container.innerHTML = '';
    
    const cores = [
        '#ff6b6b', '#4ecdc4', '#ffe66d', '#95e1d3',
        '#f38181', '#aa96da', '#fcbad3', '#a8d8ea',
        '#ff9a9e', '#fecfef', '#a18cd1', '#fbc2eb'
    ];
    
    for (let i = 0; i < 15; i++) {
        const bola = document.createElement('div');
        bola.className = 'bola-girando';
        
        const angulo = Math.random() * Math.PI * 2;
        const raio = Math.random() * 90;
        const x = 135 + raio * Math.cos(angulo);
        const y = 135 + raio * Math.sin(angulo);
        
        const cor = cores[Math.floor(Math.random() * cores.length)];
        const numero = Math.floor(Math.random() * 75) + 1;
        
        bola.style.left = x + 'px';
        bola.style.top = y + 'px';
        bola.style.background = `radial-gradient(circle at 30% 30%, ${cor}, ${cor}dd)`;
        bola.style.animationDelay = `${Math.random() * 2}s`;
        bola.textContent = numero;
        
        container.appendChild(bola);
    }
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
            
            ['B', 'I', 'N', 'G', 'O'].forEach(letra => {
                html += `<div class="cartela-cabecalho">${letra}</div>`;
            });
            
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
    
    const globoWrapper = document.getElementById('globoWrapper');
    const bolaSorteada = document.getElementById('globoBolaSorteada');
    const bolaNumero = document.getElementById('bolaNumeroDisplay');
    const btnSortear = document.getElementById('btnSortearBingo');
    const letraBingo = document.getElementById('letraBingo');
    const numeroBingo = document.getElementById('numeroBingo');
    const totalSorteados = document.getElementById('totalSorteados');
    
    // Esconde a bola anterior e reinicia animação
    if (bolaSorteada) bolaSorteada.style.display = 'none';
    if (globoWrapper) globoWrapper.classList.remove('sorteado');
    
    // Regenera bolas para efeito visual
    gerarBolasGlobo();
    
    if (btnSortear) btnSortear.disabled = true;
    
    try {
        // Aguarda 3 segundos de animação
        await new Promise(resolve => setTimeout(resolve, 3000));
        
        const response = await fetch('/bingo/sortear', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        
        const data = await response.json();
        
        if (data.erro) { 
            alert(data.erro); 
            if (btnSortear) btnSortear.disabled = false;
            return; 
        }
        
        if (data.resultado.numero !== null) {
            const numero = data.resultado.numero;
            const letra = data.resultado.letra;
            
            // Para animação e mostra bola
            if (globoWrapper) globoWrapper.classList.add('sorteado');
            if (bolaNumero) bolaNumero.textContent = numero;
            if (bolaSorteada) bolaSorteada.style.display = 'flex';
            
            // Atualiza display
            if (letraBingo) letraBingo.textContent = letra;
            if (numeroBingo) numeroBingo.textContent = numero;
            if (totalSorteados) totalSorteados.textContent = data.resultado.total_sorteados;
            
            // Marca no quadro
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
    const bolaSorteada = document.getElementById('globoBolaSorteada');
    const globoWrapper = document.getElementById('globoWrapper');
    
    if (btnIniciar) btnIniciar.disabled = false;
    if (btnSortear) btnSortear.disabled = true;
    if (totalSorteados) totalSorteados.textContent = '0';
    if (letraBingo) letraBingo.textContent = '-';
    if (numeroBingo) numeroBingo.textContent = '-';
    if (bolaNumero) bolaNumero.textContent = '?';
    if (bolaSorteada) bolaSorteada.style.display = 'none';
    if (globoWrapper) globoWrapper.classList.remove('sorteado');
    
    // Regenerar bolas
    gerarBolasGlobo();
    
    ['B', 'I', 'N', 'G', 'O'].forEach(letra => {
        const container = document.getElementById(`numeros-${letra}`);
        if (container) container.innerHTML = '';
    });
}

// ========== INICIALIZAÇÃO ==========
document.addEventListener('DOMContentLoaded', function() {
    carregarTema();
    gerarBolasGlobo();
});