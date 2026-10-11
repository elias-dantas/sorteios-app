# 📖 Guia de Uso - Sistema de Sorteios

## 🎯 Sobre este Documento

Este guia apresenta todas as funcionalidades do **Sistema de Sorteios**, explicando passo a passo como utilizar cada recurso disponível na aplicação.

---

## 🚀 Acesso à Aplicação

### Via Navegador
1. Abra seu navegador (Chrome, Firefox, Edge, Safari)
2. Acesse a URL da aplicação: `https://sorteios-app.onrender.com`
3. A página inicial carregará automaticamente

### Requisitos
- Navegador moderno com suporte a JavaScript
- Conexão com a internet
- Resolução mínima recomendada: 360px de largura

---

## 🎨 Interface Principal

A aplicação possui os seguintes elementos visuais:

| Elemento | Descrição |
|----------|-----------|
| **Menu de Temas** | Canto superior direito - alterna entre Claro, Escuro e Sistema |
| **Título** | Nome da aplicação com gradiente |
| **Abas de Navegação** | 5 tipos de sorteio disponíveis |
| **Área de Formulário** | Configuração dos parâmetros do sorteio |
| **Área de Resultado** | Exibição do resultado do sorteio |
| **Rodapé** | Informações de versão e desenvolvedor |

---

## 🌗 Alternância de Temas

A aplicação oferece 3 modos de exibição:

### ☀️ Tema Claro
- Fundo com gradiente colorido (roxo, rosa, azul)
- Container com efeito de vidro fosco
- Ideal para uso diurno

###  Tema Escuro
- Fundo escuro com gradiente (azul-marinho, roxo)
- Elementos com glow roxo/violeta
- Ideal para uso noturno ou ambientes com pouca luz

### 💻 Tema Sistema
- Detecta automaticamente a preferência do seu sistema operacional
- Segue a configuração do Windows/macOS/Linux

### Como Alternar
1. Clique no botão **"🎨 Tema"** no canto superior direito
2. Selecione uma das opções: Claro, Escuro ou Sistema
3. A preferência é salva automaticamente no navegador

---

## 🔢 Sorteio de Números

Sorteia números aleatórios dentro de um intervalo definido.

### Passo a Passo

1. **Clique na aba "🔢 Números"**
2. **Configure os parâmetros:**
   - **Valor Mínimo**: Número inicial do intervalo (ex: `1`)
   - **Valor Máximo**: Número final do intervalo (ex: `100`)
   - **Quantidade**: Quantos números sortear (ex: `1`)
   - **Permitir repetição**: Marque se os números podem se repetir
3. **Clique em "🎰 Sortear"**
4. **Aguarde a animação** (3 segundos de rolagem)
5. **Veja o resultado** na área inferior

### Exemplos de Uso

| Cenário | Mínimo | Máximo | Quantidade | Repetição |
|---------|--------|--------|------------|-----------|
| Loteria Mega-Sena | 1 | 60 | 6 | Não |
| Dado de 100 faces | 1 | 100 | 1 | Não |
| Múltiplos números | 1 | 10 | 3 | Sim |
| Número da sorte | 1 | 1000 | 1 | Não |

### Regras e Validações

- ✅ O valor mínimo deve ser menor que o máximo
- ✅ A quantidade deve ser pelo menos 1
- ✅ Se não permitir repetição, a quantidade não pode exceder o intervalo

---

##  Sorteio de Nomes

Sorteia nomes de uma lista de participantes, com suporte a telefone opcional.

### Passo a Passo

1. **Clique na aba "👥 Nomes"**
2. **Insira a lista de participantes:**
   - Um nome por linha
   - Formato opcional: `Nome - Telefone`
3. **Configure:**
   - **Quantidade a sortear**: Quantos vencedores
   - **Permitir repetição**: Se o mesmo nome pode sair mais de uma vez
4. **Clique em "🎯 Sortear"**
5. **Aguarde o spinner** (3 segundos)
6. **Veja o(s) vencedor(es)** com nome e telefone (se informado)

### Formato da Lista

João Silva - (11) 99999-9999
Maria Santos - (11) 88888-8888
Pedro Oliveira
Ana Costa - (11) 77777-7777
Carlos Souza


### Exemplos de Uso

| Cenário | Formato | Quantidade |
|---------|---------|------------|
| Sorteio de brinde | Lista simples | 1 |
| Múltiplos prêmios | Lista com telefone | 3 |
| Rifa empresarial | Lista completa | 5 |

### Regras e Validações

- ✅ A lista não pode estar vazia
- ✅ A quantidade não pode exceder o número de participantes (sem repetição)
- ✅ O telefone é opcional - se não informado, apenas o nome é exibido

---

##  Sorteio de Cores

Sorteia cores de três formas diferentes.

### Modos Disponíveis

#### 1. 🎨 Cores Predefinidas
15 cores clássicas disponíveis:
- Vermelho, Verde, Azul, Amarelo, Roxo
- Laranja, Rosa, Ciano, Magenta, Marrom
- Preto, Branco, Cinza, Dourado, Prata

#### 2. 🌈 RGB Aleatório
- Gera qualquer cor do espectro RGB
- Retorna o código hexadecimal da cor
- Ideal para design e paletas aleatórias

#### 3. ✏️ Cores Customizadas
- Você define suas próprias cores
- Insira códigos hexadecimais (um por linha)
- Exemplo: `#FF0000`, `#00FF00`, `#0000FF`

### Passo a Passo

1. **Clique na aba " Cores"**
2. **Selecione o modo** no dropdown
3. **Se escolher "Custom"**, insira as cores no campo de texto
4. **Defina a quantidade** de cores a sortear
5. **Clique em "🎨 Sortear"**
6. **Veja a cor** com seu nome/código hexadecimal

### Exemplos de Uso

| Cenário | Modo | Quantidade |
|---------|------|------------|
| Escolher cor do dia | Predefinidas | 1 |
| Gerar paleta aleatória | RGB | 5 |
| Sortear entre opções da marca | Custom | 1 |

---

## 🎲 Sorteio de Dados

Simula o lançamento de dados de RPG com diversos tipos.

### Tipos de Dados Disponíveis

| Tipo | Faces | Uso Comum |
|------|-------|-----------|
| **D4** | 4 faces | Danos de adagas |
| **D6** | 6 faces | Dados tradicionais |
| **D8** | 8 faces | Danos de espadas longas |
| **D10** | 10 faces | Percentuais |
| **D12** | 12 faces | Danos de machados |
| **D20** | 20 faces | Testes de habilidade (D&D) |
| **D100** | 100 faces | Tabelas de encontro |

### Passo a Passo

1. **Clique na aba "🎲 Dados"**
2. **Selecione o tipo de dado** no dropdown
3. **Defina a quantidade** de dados (1 a 10)
4. **Clique em "🎲 Rolar Dados"**
5. **Aguarde a animação** de giro (3 segundos)
6. **Veja os valores** de cada dado e a soma total (se múltiplos)

### Exemplos de Uso

| Cenário | Tipo | Quantidade | Resultado Esperado |
|---------|------|------------|-------------------|
| Ataque com espada | D20 | 1 | 1-20 |
| Dano de fogo | D6 | 2 | 2-12 (com soma) |
| Teste de perícia | D20 | 1 | 1-20 |
| Tabela aleatória | D100 | 1 | 1-100 |

### Visualização dos Dados

Os dados são exibidos com:
- **Representação visual** tradicional (pontos nas faces)
- **Animação de giro** durante o sorteio
- **Soma automática** quando múltiplos dados são rolados

---

## 🎱 Bingo

Sistema completo de bingo com geração de cartelas, jogo interativo e quadro de números.

### Funcionalidades do Bingo

#### 🎫 Gerar Cartelas
- Gera cartelas seguindo as regras oficiais do bingo
- **B**: números 1-15
- **I**: números 16-30
- **N**: números 31-45 (com espaço livre ★ no centro)
- **G**: números 46-60
- **O**: números 61-75
- Gera de 1 a 10 folhas (4 cartelas por folha A4)
- Impressão profissional otimizada

#### ▶️ Iniciar Bingo
- Inicia um novo jogo
- Reseta o quadro de números
- Habilita o botão de sortear

#### 🎱 Sortear Número
- Sorteia um número aleatório não repetido
- Animação do globo girando por 3 segundos
- Exibe a letra (B-I-N-G-O) e o número
- Marca automaticamente no quadro

#### 🔄 Reiniciar
- Encerra o jogo atual
- Permite iniciar um novo bingo

### Passo a Passo - Gerar Cartelas

1. **Clique na aba "🎱 Bingo"**
2. **Defina a quantidade de folhas** (1-10)
3. **Clique em " Gerar Cartelas"**
4. **A janela de impressão abrirá automaticamente**
5. **Selecione a impressora** e imprima

### Passo a Passo - Jogar Bingo

1. **Clique em "▶️ Iniciar Bingo"**
2. **Clique em " Sortear Número"** para cada bola
3. **Aguarde a animação** do globo (3 segundos)
4. **Veja o número sorteado** com sua letra
5. **O número é marcado** no quadro automaticamente
6. **Continue até** sortear todos os 75 números ou até alguém fazer bingo

### Quadro de Números

O quadro exibe:
- **5 colunas** (B, I, N, G, O)
- **15 números por coluna**
- **Destaque visual** para números sorteados
- **Contador** de números sorteados (ex: 15/75)

### Regras Oficiais do Bingo

- Cada cartela tem 25 espaços (5x5)
- O centro é livre (★)
- Cada coluna tem uma faixa específica de números
- Vitória: completar linha, coluna ou diagonal

---

## 📱 Uso em Dispositivos Móveis

A aplicação é totalmente responsiva e funciona em:

### Smartphones (6.0" - 6.9")
- Layout adaptado para telas pequenas
- Botões empilhados verticalmente
- Quadro do bingo com rolagem horizontal
- Globo reduzido proporcionalmente

### Tablets (7" - 12")
- Layout intermediário
- Abas em grid de 3 colunas
- Elementos com tamanho confortável

### Desktop (13"+)
- Layout completo
- Abas em linha (5 colunas)
- Todos os elementos em tamanho ideal

---

## 🖨️ Impressão de Cartelas

### Configurações Recomendadas

| Configuração | Valor |
|--------------|-------|
| **Tamanho do papel** | A4 |
| **Orientação** | Retrato |
| **Margens** | Mínimas (0.5cm) |
| **Escala** | 100% (tamanho real) |
| **Cores** | Colorido |

### Dicas de Impressão

- ✅ Use papel de boa gramatura (75g ou superior)
- ✅ Imprima em cores para melhor visualização
- ✅ Verifique a pré-visualização antes de imprimir
- ✅ Cada folha contém 4 cartelas (9cm x 13cm cada)

---

##  Perguntas Frequentes (FAQ)

### A aplicação funciona offline?
❌ Não. A aplicação requer conexão com a internet para funcionar.

### Posso usar em eventos comerciais?
✅ Sim. A aplicação é gratuita e pode ser usada livremente.

### Os sorteios são realmente aleatórios?
✅ Sim. Utiliza o módulo `random` do Python, que gera números pseudoaleatórios de alta qualidade.

### Posso salvar os resultados?
⚠️ Atualmente não há histórico persistente. Os resultados são exibidos apenas na sessão atual.

### A aplicação funciona em qualquer navegador?
✅ Sim. Compatível com Chrome, Firefox, Edge, Safari e navegadores móveis modernos.

### Como reportar um bug?
📧 Entre em contato com o desenvolvedor ou abra uma issue no repositório GitHub.

### Posso modificar o código?
✅ Sim. O projeto é distribuído sob a licença MIT, permitindo modificações e uso comercial.

---

## 🎯 Dicas de Uso

### Para Eventos
1. **Teste antes** do evento começar
2. **Tenha um backup** (lista de nomes em arquivo)
3. **Use tela grande** (projetor ou TV) para melhor visualização
4. **Desabilite o tema escuro** se o ambiente for muito iluminado

### Para Uso Pessoal
1. **Salve a página** nos favoritos para acesso rápido
2. **Use o tema sistema** para integração com seu SO
3. **Experimente diferentes modos** de sorteio de cores

### Para Jogos de RPG
1. **Use D20** para testes de habilidade
2. **Use D6** para danos de armas comuns
3. **Múltiplos dados** calculam a soma automaticamente

---

##  Suporte

Para dúvidas, sugestões ou reportar problemas:

- **Repositório**: https://github.com/elias-dantas/sorteios-app
- **Licença**: MIT
- **Desenvolvedor**: Elias Dantas

---

##  Licença

Este software é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` na raiz do projeto para mais detalhes.

**© 2026 Sistema de Sorteios. Todos os direitos reservados.**