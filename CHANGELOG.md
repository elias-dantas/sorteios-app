\# 📝 Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),

e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

\---

\## [Não lançado]

\### Adicionado

- Sistema de versionamento automático com Conventional Commits
- Workflow `release.yml` para automação de releases
- Script `bump\_version.py` para incremento de versão
- Endpoint `/api/version` para consulta de versão via API
- Badge de versão no rodapé da aplicação
- Data de build exibida no rodapé
- Documentação completa de uso (`docs/use\_sorteios.md`)
- CHANGELOG.md para histórico de mudanças

\---

\## [1.0.0] - 2026-10-05

\### 🎉 Lançamento Inicial

Primeira versão estável do Sistema de Sorteios com todas as funcionalidades principais.

\### Adicionado

- \*\*Sorteio de Números\*\*
- Intervalo personalizável (mínimo e máximo)
- Quantidade configurável
- Opção de permitir repetição
- Animação de rolagem por 3 segundos
- Validação completa de parâmetros

- \*\*Sorteio de Nomes\*\*
- Lista de participantes com telefone opcional
- Formato flexível: `Nome - Telefone`
- Spinner de carregamento durante o sorteio
- Exibição do telefone do vencedor

- \*\*Sorteio de Cores\*\*
- 3 modos: Predefinidas, RGB Aleatório, Customizadas
- 15 cores predefinidas
- Suporte a códigos hexadecimais customizados
- Animação de revelação da cor

- \*\*Sorteio de Dados\*\*
- 7 tipos de dados: D4, D6, D8, D10, D12, D20, D100
- Representação visual tradicional com pontos
- Animação de giro
- Soma automática para múltiplos dados
- Suporte até 10 dados simultâneos

- \*\*Sistema de Bingo Completo\*\*
- Globo animado com CSS puro (bolas coloridas girando)
- Grade metálica com meridianos e paralelos
- Bola sorteada com animação de zoom
- Quadro de números B-I-N-G-O (1-75)
- Destaque visual para números sorteados
- Contador de números sorteados
- Geração de cartelas seguindo regras oficiais
- Impressão profissional (4 cartelas por folha A4)
- Cartelas de 9cm x 13cm
- Espaço livre (★) no centro da cartela

- \*\*Interface Moderna\*\*
- Layout híbrido: Glassmorphism + Neumorphism + Dark Premium
- Fundo com gradiente animado
- Container com efeito de vidro fosco (backdrop blur)
- Sombras duplas (efeito tátil)
- Glow em elementos ativos
- Título com texto em gradiente
- Botões com efeito de elevação
- Inputs com efeito de profundidade

- \*\*Sistema de Temas\*\*
- Tema Claro (gradiente colorido)
- Tema Escuro (fundo escuro com glow roxo)
- Tema Sistema (detecta preferência do SO)
- Persistência via localStorage
- Transições suaves entre temas
- Dropdown de seleção de tema

- \*\*Responsividade Completa\*\*
- Desktop (13"+): Layout completo
- Tablet (7"-12"): Layout adaptado
- Smartphone (6.0"-6.9"): Layout otimizado
- Quadro do bingo com rolagem horizontal em mobile
- Botões empilhados em telas pequenas
- Globo redimensionado proporcionalmente

- \*\*Rodapé Profissional\*\*
- Nome do desenvolvedor (Elias Dantas)
- Copyright 2026
- Badge de versão com gradiente
- Data de build
- Menção à licença MIT

- \*\*Backend Python/Flask\*\*
- API RESTful completa
- Validação de dados no servidor
- Tratamento de erros com mensagens claras
- Estado do jogo de bingo em memória
- Geração aleatória de cartelas
- Sorteios sem repetição quando configurado

- \*\*CI/CD com GitHub Actions\*\*
- Workflow de deploy automático
- Self-hosted runner no servidor Ubuntu
- Testes automatizados de imports e lógica
- Deploy via SSH para servidor de produção
- Backup automático antes do deploy
- Reinício automático do serviço

- \*\*Infraestrutura\*\*
- Servidor Ubuntu 24.04
- Nginx como reverse proxy
- Gunicorn como servidor WSGI
- Systemd para gerenciamento de serviços
- Firewall UFW configurado
- Hospedagem no Render.com

- \*\*Documentação\*\*
- README.md completo
- Guia do usuário detalhado
- Documentação da API
- Instruções de instalação
- Configuração de produção

\### Tecnologias

- Python 3.12
- Flask 3.0.0
- Gunicorn 21.2.0
- HTML5, CSS3, JavaScript ES6+
- GitHub Actions
- Nginx
- Systemd

\---

\## Convenções

\### Tipos de Mudanças

- \*\*Adicionado\*\* - Novas funcionalidades
- \*\*Alterado\*\* - Mudanças em funcionalidades existentes
- \*\*Descontinuado\*\* - Recursos que serão removidos em breve
- \*\*Removido\*\* - Recursos removidos
- \*\*Corrigido\*\* - Correções de bugs
- \*\*Segurança\*\* - Correções de vulnerabilidades

\### Formato de Versão

- \*\*MAJOR.MINOR.PATCH\*\*
- \*\*MAJOR\*\*: Mudanças incompatíveis (breaking changes)
- \*\*MINOR\*\*: Novas funcionalidades (compatíveis)
- \*\*PATCH\*\*: Correções de bugs

\---

\## Links Úteis

- [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/)
- [Semantic Versioning](https://semver.org/lang/pt-BR/)
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/)
- [Licença MIT](https://opensource.org/licenses/MIT)

\---

\*\*© 2026 Sistema de Sorteios. Todos os direitos reservados.\*\*
