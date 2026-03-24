# 🪐 Nexus Workspace

Nexus Workspace é um sistema web de gerenciamento de tarefas desenvolvido com **Python (Flask)** no backend e uma interface moderna com estética **Cyber-Glass**.

O projeto foi criado com foco em organização, produtividade e aplicação de boas práticas de desenvolvimento web, simulando uma aplicação SaaS (Software as a Service) real.

---

## 🎯 Objetivo do Projeto

Desenvolver uma aplicação completa com autenticação de usuários, controle de tarefas e isolamento de dados, aplicando conceitos reais de backend, arquitetura e integração lógica entre frontend e backend.

O Nexus Workspace representa a evolução prática das minhas habilidades em **Desenvolvimento de Sistemas**.

---

## 🎥 Demonstração

📌 **Fluxo principal do sistema:**
- Cadastro e login de usuário
- Criação de tarefas
- Edição e exclusão
- Atualização dinâmica da interface
- Indicadores de produtividade em tempo real

📌 **Interface moderna com:**
- Painéis translúcidos com efeito `backdrop-filter` (Glassmorphism avançado)
- Aurora background dinâmico interativo
- Micro-interações e animações construídas via JavaScript puro
- Sistema nativo de tema Claro/Escuro salvo em cache do navegador


![Demonstração Oficial do Nexus Workspace](file:///C:/Users/PAULOOTAVIODESOUZALU/.gemini/antigravity/brain/613b45a5-d85d-4e76-b828-f94dd4630b53/nexus_demo_final_1774382453486.webp)

---

## ✨ Funcionalidades

- ✅ **Autenticação Segura**: Gerenciamento de sessão persistente com Flask-Login.
- ✅ **CRUD Completo**: Criação, leitura, edição e exclusão de tarefas em SQL.
- ✅ **Filtro Dinâmico via Command Palette**: Spotlight acionado por `Ctrl + K` para busca interativa em tempo real.
- ✅ **Timer Hyper Focus**: Widget integrado estilo Pomodoro SVG para gestão extrema do ciclo de foco.
- ✅ **Indicadores Visuais**: Acompanhamento analítico imediato da taxa de progresso das tarefas da semana.
- ✅ **Micro-interações Modernas**: Cursor customizado integrado aos elementos (`Lerp Physics`), Tilt Holográfico 3D nos cartões e transições ao eliminar dados do painel.

---

## 🛠️ Stack Tecnológica

### 🔹 Backend
- **Python 3**
- **Flask** (Framework Web Minimalista)
- **Flask-Login** (Autenticação stateful via Sessões)
- **Werkzeug.security** (Salts e Criptografia Hash)
- **SQLite3** (Banco de Dados Relacional nativo leve)

### 🔹 Frontend
- **HTML5** & **CSS3** (CSS Grid System + Flexbox Avançado)
- **Vanilla JavaScript** (Lógicas complexas de Observer, DOM Nodes manipulados 100% sem jQuery)
- **Bootstrap Icons**
- **Vanilla-Tilt.js** (Projeção paralaxe tridimensional na UI)

---

## 🧩 Arquitetura do Projeto

O projeto foi rigorosamente desenhado seguindo as metodologias de separação física de responsabilidades (Modular Architecture):

```text
gerenciador_tarefas/
│
├── core/
│   ├── models.py       # Classes Orientadas a Objetos e Entidades do Domínio de Negócios
│   └── repository.py   # Camada estrita de Comunicação de Banco (Queries e Persistência)
│
├── web/
│   ├── app.py          # Entrypoint Principal que absorve Rotas, Controladores e Interceptors
│   ├── static/         # Motor Visual interativo e UI Stylies (Javascript e CSS base)
│   └── templates/      # Páginas de Visão embutidas com Template Engine Avançada (Jinja2)
│
├── Iniciar Nexus.bat   # Ferramenta Prática do Dev Environment 
└── README.md
```

### Padrões Aplicados
- Separação em camadas estritas.
- Arquitetura Modular garantindo facilidade para manutenção colaborativa futura.
- Responsabilidade Única (Evitando que a ponte Frontend-Backend sofra colapsos visuais).
- Isolamento intencional de lógica de banco e da formatação do design.

---

## ⚙️ Desafios Técnicos Enfrentados

Durante o planejamento, design e efetivação do código, dediquei minha inteligência a superar os seguintes obstáculos limitadores:

- **Autenticação Segura e Rotas:** Blindar endpoints contra acessos de URLs não autenticadas antes da passagem devida de login. Noites garantindo a validação de sessão em todos os pontos críticos.
- **Isolamento de Dados Estrito:** Como fazer o banco isolar de forma performática a requisição do Usuário A sem permitir manipulações espelhadas do Usuário B? Usando escopo restrito por chaves primárias e relacionais nos modelos do Flask em toda operação ao SQL.
- **Integração Backend/Frontend Pura:** Movimentar e alterar os contextos dinâmicos passados pelo backend do Flask (Jinja) injetando poder puro com lógicas ativas de animação em JavaScript na hora da renderização das instâncias de Tarefas. 
- **Micro-interações Customizadas (JS Purista):** Construir cronômetros independentes (Timer Overlay) e Spotlight Global (Command Palette) usando algoritmos Vanilla JS interagindo com SVGs pesados de UI, tudo em nome de uma Developer Experience de extrema estirpe gráfica.

Esses desafios e aprendizados contribuíram diretamente e imensuravelmente para meu grande e recente salto maturacional abrangendo **Backend e Arquitetura de Sistemas de ponta**, focando não no processo genérico de se programar, mas na base da "Boa Programação". 

---

## 🔒 Segurança

- Proteção hermética de senhas ao serem transmutadas aos hashes unicamente ilegíveis utilizando algoritmos rigorosos do `generate_password_hash`.
- Validações de sessões nativas por cookies seguros via `Flask-Login`.
- Regras de rotas decoradas obrigatoriamente sob `@login_required` para prevenir brechas de Inocência Frontend.

---

## 💡 Casos de Uso

- **Para Estudantes:** Organizador dinâmico de prioridades de módulos e ciclos de estudos sob Hyper Focus guiado por timer base (Pomodoro). 
- **Para Desenvolvedores:** Painel nativo para documentações particulares de backlog, fixes, bugs e rotinas do dia a dia enquadrando prioridades "Alta", "Média" ou "Baixa".
- **Squads Particulares:** Projetos para controle interno minimalista, dispensando sistemas monótonos pela facilidade global de acesso interativo 3D.

---

## 🚀 Como Executar Localmente

### 🔹 Método Rápido (Exclusivo Windows)

1. Faça o download da pasta raiz (`gerenciador_tarefas`).
2. Vá até essa pasta e realize 2 cliques no executável de rotina **`Iniciar Nexus.bat`**.
3. Assista ao banco e ao servidor se compilarem juntos; O navegador em seu computador disparará diretamente para sua nova home. Pronto para uso!

### 🔹 Método Manual (Windows / OS X Cripto / Distribuições Unix)

1. **Clone seu repositório localmente:**
   ```bash
   git clone <Insira-Seu-Repositorio-Git-AQUI>
   cd licenciador_tarefas
   ```

2. **Certifique-se do Ambiente Virtual (Opcional, mas Seguro)** e Instale suas exigências externas:
   ```bash
   pip install flask flask-login werkzeug
   ```

3. **Suba todo o BackEnd:**
   ```bash
   python -m web.app
   ```

4. **Entre na sua aplicação:** Acesse via Navegador:
   `http://127.0.0.1:5000/`

---

## 📈 Próximas Melhorias do Core

- Deploy full-cycle definitivo em ambientes robustos na cloud (Instâncias como Render, Railway ou VPS localizadas).
- Refatoração para adaptação SQL Complexa, injetando integração por ORM pesada voltando de SQLite à arquitetura sólida de um **PostgreSQL**.
- Expandir a camada analítica com lógicas visuais de progressão (Chart.js / D3 Charts).
- Mudar para um ambiente flex em formato board-painel permitindo um visual purista tipo Kanban (Cards re-arrastados e realocados).

---

## 👨‍💻 Sobre o Desenvolvedor

Muito Prazer. Atuo ativamente e intensamente aos estudos de **Desenvolvimento de Sistemas** focando 100% de minhas energias diárias no desdobramento de arquiteturas complexas Backend e Frontends dinâmicos puristas focados em interações profundas e funcionais.

O presente gerenciador não surgiu do acaso, mas da ambição real de se forjar na dor e suor uma **Aplicação Espelhada em Estilo SaaS**, agregando segurança sólida e código polido a uma das Experiências de Usuário (UX) mais gratificantes que decidi montar até agora.

Constante Inconformado. Construo esse portfólio como **minha porta de entrada vitrine clamando pela minha primeira oportunidade direta (Estágio Oficial em T.I.)**. Busco um ambiente e uma empresa repleta e saturada de desafios onde de fato minha obstinação pela boa prática escale rumo à engenharia de inovação.

---

⭐ **Fale do meu trabalho e me note!** Se esse projeto e essa abordagem capturaram e ressoaram com você, abrace as dependências, queime testes locais nas features feitas e deixe sem hesitar aquela **Sua Preciosa Estrela⭐** documentada neste projeto do fundo do coração. Eu o vejo evoluir, e espero que você se torne o proximo a impulsionar minha caminhada!
