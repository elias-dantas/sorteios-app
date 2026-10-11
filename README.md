# 🎲 Sistema de Sorteios

[![Status](https://img.shields.io/badge/status-produção-green)](https://sorteios-app.onrender.com)
[![Python](https://img.shields.io/badge/python-3.12+-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.0.0-lightgrey)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange)](.github/workflows/)

Aplicação web completa para realização de sorteios randômicos com interface moderna, animações visuais e sistema de Bingo profissional.

🌐 **Acesse online**: [https://sorteios-app.onrender.com](https://sorteios-app.onrender.com)

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Capturas de Tela](#capturas-de-tela)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [API Endpoints](#api-endpoints)
- [Configuração de Produção](#configuração-de-produção)
- [CI/CD com GitHub Actions](#cicd-com-github-actions)
- [Versionamento](#versionamento)
- [Documentação Adicional](#documentação-adicional)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Autor](#autor)

---

##  Visão Geral

O **Sistema de Sorteios** é uma aplicação web full-stack desenvolvida em Python com Flask, projetada para realizar diversos tipos de sorteios com interface visual rica e animações. Ideal para eventos corporativos, jogos, reuniões, rifas e qualquer situação que necessite de seleção aleatória profissional.

### 🌟 Destaques

- ✅ **5 tipos de sorteios** diferentes (Números, Nomes, Cores, Dados, Bingo)
- ✅ **Sistema de Bingo completo** com globo animado e impressão de cartelas
- ✅ **Interface moderna** com layout híbrido (Glassmorphism + Neumorphism + Dark Premium)
- ✅ **Temas adaptativos** (claro, escuro, sistema)
- ✅ **100% responsivo** para mobile, tablet e desktop
- ✅ **Deploy automático** via CI/CD com GitHub Actions
- ✅ **Versionamento SemVer** com Conventional Commits
- ✅ **Código aberto** sob licença MIT

---

## ✨ Funcionalidades

###  Sorteio de Números
- Definição de intervalo personalizado (mínimo e máximo)
- Quantidade de números a sortear
- Opção de permitir ou bloquear repetição
- Animação de rolagem por 3 segundos
- Validação de parâmetros no backend e frontend

### 👥 Sorteio de Nomes
- Lista de participantes (nome e telefone opcional)
- Formato flexível: `Nome - Telefone` ou apenas `Nome`
- Quantidade a sortear
- Animação com spinner de carregamento
- Exibição do telefone do vencedor (se informado)

### 🎨 Sorteio de Cores
- **3 modos disponíveis:**
  - 🎨 **Cores Predefinidas** (15 cores clássicas)
  - 🌈 **RGB Aleatório** (qualquer cor do espectro)
  - ✏️ **Cores Customizadas** (defina suas próprias cores)
- Animação de seleção com efeito visual
- Exibição do nome e código hexadecimal

### 🎲 Sorteio de Dados
- **7 tipos de dados:** D4, D6, D8, D10, D12, D20, D100
- Representação visual tradicional com pontos
- Cálculo automático da soma (múltiplos dados)
- Animação de giro por 3 segundos
- Suporte até 10 dados simultâneos

### 🎱 Bingo Completo

#### 🎮 Jogo de Bingo
- **Globo tradicional** estilo grade metálica com meridianos e paralelos
- **Animação de giro** por 3 segundos
- **Bola com número** exibida abaixo do globo
- **Quadro de números** (1-75) organizado por colunas B-I-N-G-O
- **Destaque visual** para números sorteados
- **Controles completos:** Iniciar, Sortear, Reiniciar

#### 🎫 Cartelas de Bingo
- **Geração aleatória** seguindo regras oficiais:
  - **B**: números 1-15
  - **I**: números 16-30
  - **N**: números 31-45 (com espaço livre ★ no centro)
  - **G**: números 46-60
  - **O**: números 61-75
- **Impressão profissional:**
  - 4 cartelas por folha A4
  - Dimensões: 9cm x 13cm cada
  - Layout otimizado para impressão
  - Cabeçalho colorido B-I-N-G-O
- **Quantidade flexível:** 1 a 10 folhas por vez

### 🎨 Sistema de Temas
- ☀️ **Claro** - Interface clara com gradiente colorido
- 🌙 **Escuro** - Interface escura com glow roxo
- 💻 **Sistema** - Detecta automaticamente a preferência do SO
- **Persistência:** preferência salva no `localStorage`
- **Transições suaves** entre temas

---

## 📸 Capturas de Tela

> 💡 Acesse a aplicação em [https://sorteios-app.onrender.com](https://sorteios-app.onrender.com) para ver a interface em ação.

### Tema Claro
Interface com fundo gradiente animado (roxo, rosa, azul) e container com efeito de vidro fosco.

### Tema Escuro
Interface escura com fundo azul-marinho profundo e elementos com glow roxo/violeta.

---

## 🛠️ Tecnologias Utilizadas

### Backend
| Tecnologia | Versão | Função |
|------------|--------|--------|
| Python | 3.12+ | Linguagem principal |
| Flask | 3.0.0 | Framework web |
| Gunicorn | 21.2.0 | Servidor WSGI de produção |

### Frontend
| Tecnologia | Função |
|------------|--------|
| HTML5 | Estrutura semântica |
| CSS3 | Estilos, animações e temas |
| JavaScript (ES6+) | Interatividade e animações |

### Infraestrutura
| Tecnologia | Função |
|------------|--------|
| Nginx | Reverse proxy e servidor web |
| Systemd | Gerenciamento de serviços |
| Git | Controle de versão |
| GitHub Actions | CI/CD |
| Render.com | Hospedagem em nuvem |

---

##  Estrutura do Projeto

sorteios\_app/

├── .github/

│ └── workflows/

│ ├── deploy.yml # Workflow de deploy

│ └── release.yml # Workflow de versionamento

├── docs/

│ └── use\_sorteios.md # Guia do usuário

├── scripts/

│ └── bump\_version.py # Script de versionamento

├── sorteios/ # Pacote de lógica de sorteios

│ ├── init.py

│ ├── models.py # Classes de sorteio (OO)

│ └── utils.py # Funções auxiliares

├── static/ # Arquivos estáticos

│ ├── css/

│ │ └── style.css # Estilos e animações

│ └── js/

│ └── script.js # Lógica frontend

├── templates/ # Templates HTML

│ └── index.html # Página principal (SPA)

├── .gitignore # Arquivos ignorados pelo Git

├── .vscode/ # Configurações do VS Code

├── app.py # Aplicação Flask principal

├── CHANGELOG.md # Histórico de mudanças

├── LICENSE # Licença MIT

├── README.md # Este arquivo

├── requirements.txt # Dependências Python

└── VERSION # Versão atual (SemVer)

123456789101112131415161718192021222324252627282930

Acesse: http://localhost:5000

Uso

Para instruções detalhadas de uso, consulte o Guia do Usuário.

Resumo Rápido

Acesse a aplicação no navegador

Escolha o tipo de sorteio nas abas superiores

Configure os parâmetros conforme necessário

Clique em "Sortear" e aguarde a animação

Veja o resultado na área inferior

🔌 API Endpoints

GET /

Renderiza a página inicial.

POST /sortear/numero

Sorteia números em um intervalo.

Request:

json

1234

POST /sortear/nomes

Sorteia nomes de uma lista.

Request:

json

12345

POST /sortear/cores

Sorteia cores.

Request:

json

12345

Modos disponíveis:

"predefinidas" - 15 cores clássicas

"rgb" - RGB aleatório

"custom" - Cores customizadas (enviar array em cores\_custom)

POST /sortear/dados

Sorteia dados.

Request:

json

1234

Tipos disponíveis: d4, d6, d8, d10, d12, d20, d100

POST /bingo/iniciar

Inicia novo jogo de bingo.

POST /bingo/sortear

Sorteia próximo número do bingo.

POST /bingo/gerar-cartelas

Gera cartelas de bingo.

Request:

json

123

GET /api/version

Retorna informações da versão atual.

Response:

json

1234

🏭 Configuração de Produção

1. Instalar Gunicorn

bash

12

1. Criar Service do Systemd

bash

1

ini

123456789

Ativar:

bash

1234

1. Configurar Nginx

bash

1

nginx

123456789

Ativar:

bash

1234

1. Configurar Firewall

bash

123

🔄 CI/CD com GitHub Actions

O projeto utiliza GitHub Actions para automação de deploy e versionamento.

Workflows Disponíveis

deploy.yml - Deploy Automático

Trigger: Push na branch main

Jobs:

Testes - Valida imports e lógica de sorteios

Deploy - Atualiza o servidor via self-hosted runner

release.yml - Versionamento Automático

Trigger: Push na branch main

Detecção: Conventional Commits

Ações:

Detecta tipo de bump (major/minor/patch)

Incrementa versão no arquivo VERSION

Cria tag Git automaticamente

Faz push da tag

Conventional Commits

O versionamento automático segue o padrão Conventional Commits:

Prefixo

Tipo de Bump

Exemplo

feat:

MINOR

feat: adicionar sorteio de bingo

fix:

PATCH

fix: corrigir layout mobile

feat!:

MAJOR

feat!: mudar API de sorteios

docs:

Nenhum

docs: atualizar README

chore:

Nenhum

chore: atualizar dependências

Exemplo de Uso

bash

1234567891011121314

Versionamento

Este projeto utiliza Semantic Versioning (SemVer) no formato MAJOR.MINOR.PATCH:

MAJOR: Mudanças incompatíveis (breaking changes)

MINOR: Novas funcionalidades (compatíveis)

PATCH: Correções de bugs

Versão atual: Consulte o arquivo VERSION ou acesse /api/version.

Para mais detalhes, consulte o CHANGELOG.md.

📚 Documentação Adicional

Documento

Descrição

Guia do Usuário

Instruções detalhadas de uso

CHANGELOG

Histórico de mudanças por versão

LICENSE

Licença MIT completa

🤝 Contribuindo

Contribuições são bem-vindas! Siga estes passos:

Fork o repositório

Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'feat: add AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abra um Pull Request

Padrões de Commit

Utilize Conventional Commits para que o versionamento automático funcione corretamente:

feat: - Nova funcionalidade

fix: - Correção de bug

docs: - Documentação

style: - Formatação

refactor: - Refatoração

test: - Testes

chore: - Tarefas de manutenção

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

Resumo da Licença MIT:

✅ Uso comercial permitido

✅ Modificação permitida

✅ Distribuição permitida

✅ Uso privado permitido

⚠️ Aviso de licença deve ser incluído

👨‍💻 Autor

Elias Dantas - Desenvolvedor Full Stack

eliasrangel@hotmail.com

GitHub: elias-dantas

Agradecimentos

Desenvolvido com ❤️ usando Python, Flask e muito café ☕

📊 Status do Projeto

Componente

Status

Aplicação

✅ Produção

CI/CD

✅ Operacional

Versionamento

✅ Automático

Documentação

✅ Completa

Testes

✅ Passando

© 2026 Sistema de Sorteios. Todos os direitos reservados.
