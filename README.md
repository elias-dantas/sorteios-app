# 🎲 Sistema de Sorteios

Aplicação web completa para realização de sorteios randômicos com interface moderna, animações visuais e sistema de Bingo profissional.

![Status](https://img.shields.io/badge/status-produção-green)
![Python](https://img.shields.io/badge/python-3.12+-blue)
![Flask](https://img.shields.io/badge/flask-3.0.0-lightgrey)
![License](https://img.shields.io/badge/license-MIT-yellow)

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [API Endpoints](#api-endpoints)
- [Configuração de Produção](#configuração-de-produção)
- [CI/CD com GitHub Actions](#cicd-com-github-actions)
- [Domínio Local](#domínio-local)
- [Troubleshooting](#troubleshooting)
- [Licença](#licença)
- [Autor](#autor)

---

## 🎯 Visão Geral

O **Sistema de Sorteios** é uma aplicação web full-stack desenvolvida em Python com Flask, projetada para realizar diversos tipos de sorteios com interface visual rica e animações. Ideal para eventos corporativos, jogos, reuniões, rifas e qualquer situação que necessite de seleção aleatória profissional.

### 🌟 Destaques

- ✅ **5 tipos de sorteios** diferentes
- ✅ **Sistema de Bingo completo** com globo animado
- ✅ **Impressão profissional** de cartelas (4 por folha A4)
- ✅ **Deploy automático** via CI/CD
- ✅ **Temas adaptativos** (claro, escuro, sistema)
- ✅ **100% responsivo** para mobile e desktop

---

## ✨ Funcionalidades

### 🔢 Sorteio de Números
- Definição de intervalo personalizado (mínimo e máximo)
- Quantidade de números a sortear
- Opção de permitir ou bloquear repetição
- Animação de rolagem por 3 segundos
- Validação de parâmetros no backend e frontend

###  Sorteio de Nomes
- Lista de participantes (nome e telefone opcional)
- Formato flexível: `Nome - Telefone` ou apenas `Nome`
- Quantidade a sortear
- Animação de rolagem estilo "slot machine"
- Exibição do telefone do vencedor (se informado)

### 🎨 Sorteio de Cores
- **3 modos disponíveis:**
  - 🎨 **Cores Predefinidas** (15 cores clássicas)
  -  **RGB Aleatório** (qualquer cor do espectro)
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
- ☀️ **Claro** - Interface clara e clean
- 🌙 **Escuro** - Interface escura para conforto visual
-  **Sistema** - Detecta automaticamente a preferência do SO
- **Persistência:** preferência salva no `localStorage`
- **Transições suaves** entre temas

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
| Git | Versionamento |
| GitHub Actions | CI/CD |
| Self-hosted Runner | Deploy automático local |

---

##  Estrutura do Projeto


sorteios_app/
├── app.py # Aplicação Flask principal
├── requirements.txt # Dependências Python
├── README.md # Documentação
── .gitignore # Arquivos ignorados pelo Git
├── .github/
│ └── workflows/
│ ├── deploy.yml # Workflow de deploy
│ └── validate.yml # Workflow de validação
├── sorteios/ # Pacote de lógica de sorteios
│ ├── init.py
│ ├── models.py # Classes de sorteio (OO)
│ └── utils.py # Funções auxiliares
├── static/ # Arquivos estáticos
│ ├── css/
│ │ └── style.css # Estilos e animações
│ └── js/
│ └── script.js # Lógica frontend
└── templates/ # Templates HTML
└── index.html # Página principal (SPA)


---

## 🚀 Instalação

### Pré-requisitos

- **Python 3.12** ou superior
- **pip** (gerenciador de pacotes Python)
- **Git** (controle de versão)
- **Ubuntu 24.04** (recomendado para produção)

### Ambiente de Desenvolvimento

```bash
# 1. Clonar o repositório
git clone https://github.com/elias-dantas/sorteios-app.git
cd sorteios_app

# 2. Criar ambiente virtual
python3 -m venv venv

# 3. Ativar ambiente virtual
source venv/bin/activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Executar em modo desenvolvimento
python app.py

Acesse: http://localhost:5000

🎮 Uso

Sorteio de Números
Defina o valor mínimo (ex: 1)
Defina o valor máximo (ex: 100)
Escolha a quantidade de números
Marque "Permitir repetição" se desejar
Clique em 🎰 Sortear

👥 Sorteio de Nomes

Insira os participantes (um por linha)
Formato opcional: Nome - Telefone

   João - (11) 99999-9999
   Maria - (11) 88888-8888
   Pedro
   Ana - (11) 77777-7777

Defina a quantidade a sortear
Clique em 🎯 Sortear

🎨 Sorteio de Cores

Escolha o modo:
Cores Predefinidas (15 cores clássicas)
RGB Aleatório (qualquer cor)
Cores Customizadas (digite suas cores)
Se custom, insira as cores (uma por linha)
Defina a quantidade
Clique em 🎨 Sortear

🎲 Sorteio de Dados

Escolha o tipo de dado (D4 a D100)
Defina a quantidade (1-10)
Clique em 🎲 Rolar Dados
A soma é exibida automaticamente (múltiplos dados)

🎱 Bingo

Gerar e Imprimir Cartelas
Defina a quantidade de folhas (1-10)
Clique em 🎫 Gerar Cartelas
A janela de impressão abre automaticamente
Selecione a impressora e imprima

Jogar Bingo

Clique em ▶️ Iniciar Bingo
Clique em ** Sortear Número** para cada bola
O globo gira por 3 segundos e revela o número
O número é destacado no quadro B-I-N-G-O
Use 🔄 Reiniciar para novo jogo

API Endpoints

GET /
Renderiza a página inicial.
POST /sortear/numero
Sorteia números em um intervalo.
Request:

{
  "minimo": 1,
  "maximo": 100,
  "quantidade": 1,
  "permitir_repeticao": true
}

Response:

{
  "sucesso": true,
  "tipo": "numero",
  "resultado": 42,
  "detalhes": {
    "intervalo": [1, 100],
    "quantidade": 1,
    "permitir_repeticao": true
  }
}

POST /sortear/nomes
Sorteia nomes de uma lista.
Request:

{
  "nomes": "João - (11) 99999-9999\nMaria\nPedro",
  "quantidade": 1,
  "permitir_repeticao": false
}

Response:

{
  "sucesso": true,
  "tipo": "nomes",
  "resultado": {
    "nome": "João",
    "telefone": "(11) 99999-9999"
  },
  "detalhes": {
    "total_participantes": 3,
    "quantidade": 1,
    "permitir_repeticao": false
  }
}

POST /sortear/cores
Sorteia cores.
Request:

{
  "modo": "predefinidas",
  "quantidade": 1,
  "cores_custom": null
}

Modos disponíveis:
"predefinidas" - 15 cores clássicas
"rgb" - RGB aleatório
"custom" - Cores customizadas (enviar array em cores_custom)
POST /sortear/dados
Sorteia dados.
Request:

{
  "tipo_dado": "d6",
  "quantidade": 2
}

Tipos disponíveis: d4, d6, d8, d10, d12, d20, d100
POST /bingo/gerar-cartelas
Gera cartelas de bingo.
Request:

{
  "quantidade": 1
}

Response:

{
  "sucesso": true,
  "cartelas": [
    {
      "B": [1, 5, 9, 12, 14],
      "I": [16, 20, 23, 27, 30],
      "N": [32, 35, 40, 44],
      "G": [47, 50, 53, 57, 60],
      "O": [62, 65, 69, 72, 75]
    }
  ],
  "total_folhas": 1
}

POST /bingo/iniciar
Inicia novo jogo de bingo.
Response:

{
  "sucesso": true,
  "mensagem": "Bingo iniciado!"
}

POST /bingo/sortear
Sorteia próximo número do bingo.
Response:

{
  "sucesso": true,
  "resultado": {
    "numero": 42,
    "letra": "N",
    "total_sorteados": 15,
    "fim": false
  },
  "detalhes": {
    "total_numeros": 75,
    "numeros_sorteados": 15,
    "restantes": 60
  }
}

🏭 Configuração de Produção
1. Instalar Gunicorn

source venv/bin/activate
pip install gunicorn

2. Criar Service do Systemd

sudo nano /etc/systemd/system/sorteios.service

[Unit]
Description=Sistema de Sorteios - Gunicorn
After=network.target

[Service]
User=elias
Group=www-data
WorkingDirectory=/home/elias/projetos/sorteios_app
Environment="PATH=/home/elias/projetos/sorteios_app/venv/bin"
ExecStart=/home/elias/projetos/sorteios_app/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target

Ativar:

sudo systemctl daemon-reload
sudo systemctl enable sorteios
sudo systemctl start sorteios
sudo systemctl status sorteios

3. Configurar Nginx

sudo nano /etc/nginx/sites-available/sorteios

server {
    listen 80;
    server_name sorteios.local www.sorteios.local 192.168.0.22;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /home/elias/projetos/sorteios_app/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}

Ativar:

sudo ln -s /etc/nginx/sites-available/sorteios /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx

4. Configurar Firewall

sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw enable

🔄 CI/CD com GitHub Actions
Arquitetura
O projeto utiliza GitHub Actions com Self-Hosted Runner para deploy automático:

[Desenvolvedor] 
    ↓ git push
[GitHub Repository]
    ↓ trigger
[GitHub Actions]
    ├─ Job 1: Testes (ubuntu-latest)
    └─ Job 2: Deploy (self-hosted runner)
              ↓
[Servidor Ubuntu 24.04]
    ├─ git pull
    ├─ pip install
    └─ systemctl restart sorteios
              ↓
[sorteios.local] ✅

Workflow de Deploy

O arquivo .github/workflows/deploy.yml define dois jobs:

1. ** Testes** (roda na nuvem GitHub):
Instala dependências
Valida imports
Testa lógica de sorteios
2. 🚀 Deploy em Produção (roda no servidor local):
Cria backup da versão atual
Atualiza código via git pull
Instala dependências
Reinicia o serviço

Configurar Self-Hosted Runner

# 1. Criar diretório
mkdir -p ~/actions-runner && cd ~/actions-runner

# 2. Baixar runner
curl -o actions-runner-linux-x64-2.321.0.tar.gz -L \
  https://github.com/actions/runner/releases/download/v2.321.0/actions-runner-linux-x64-2.321.0.tar.gz

# 3. Extrair
tar xzf ./actions-runner-linux-x64-2.321.0.tar.gz

# 4. Configurar (token obtido no GitHub)
./config.sh --url https://github.com/elias-dantas/sorteios-app --token TOKEN

# 5. Instalar como service
sudo ./svc.sh install
sudo ./svc.sh start
sudo ./svc.sh status

Secrets Necessários

Secret               | Valor
DEPLOY_PATH          | /home/user/projetos/sorteios_app

🌐 Domínio Local

Configurar Arquivo Hosts
Windows (C:\Windows\System32\drivers\etc\hosts):

192.168.0.22    sorteios.local    www.sorteios.local

Linux/Mac (/etc/hosts):

sudo nano /etc/hosts
# Adicionar:
192.168.0.22    sorteios.local    www.sorteios.local

Acesse: http://sorteios.local

🐛 Troubleshooting

Service não inicia

# Ver logs
sudo journalctl -u sorteios -f

# Verificar se porta está em uso
sudo lsof -i :5000

Nginx 502 Bad Gateway

# Verificar se Gunicorn está rodando
sudo systemctl status sorteios

# Ver logs do Nginx
sudo tail -f /var/log/nginx/error.log

Permissões de arquivo

sudo chmod -R 755 /home/elias/projetos/sorteios_app
sudo chown -R elias:elias /home/elias/projetos/sorteios_app
sudo usermod -a -G elias www-data

Runner offline

cd ~/actions-runner
sudo ./svc.sh status
sudo ./svc.sh restart

📊 Comandos Úteis

# Gerenciar serviço
sudo systemctl start sorteios
sudo systemctl stop sorteios
sudo systemctl restart sorteios
sudo systemctl status sorteios

# Ver logs em tempo real
sudo journalctl -u sorteios -f

# Ver logs do Nginx
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# Testar configuração Nginx
sudo nginx -t

# Reiniciar Nginx
sudo systemctl restart nginx

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

👨‍💻 Autor

Elias R. Dantas - Arquiteto Cloud & Dev. iniciante

📧 eliasrangel@hotmail.com
🐙 GitHub: elias-dantas

🙏 Agradecimentos

Desenvolvido com ❤️ usando Python, Flask e muito café ☕

📝 Changelog

v2.0.0 (2026-09-20)

✅ Sistema de Bingo completo
✅ Geração e impressão de cartelas
✅ Globo animado estilo grade metálica
✅ CI/CD com GitHub Actions
✅ Self-hosted runner
✅ Deploy automático

v1.0.0 (2026-09-15)

✅ Sorteio de números, nomes, cores e dados
✅ Animações visuais
✅ Temas claro, escuro e sistema
✅ Interface responsiva



---