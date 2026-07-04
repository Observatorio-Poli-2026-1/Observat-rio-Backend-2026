# **Back_2026.1 - Observatório de Projetos**

Bem-vindo ao repositório de **Back-End** do **Observatório de Projetos** versão 3.0 da **POLI-UPE**! Este projeto faz parte da disciplina de Engenharia de Software do curso de Engenharia da Computação e foi projetado para oferecer uma plataforma colaborativa, onde projetos acadêmicos e artigos podem ser explorados, submetidos e gerenciados.

#### ATENÇÃO: Cuidado para não expor o 'key-admin.json'!!, pois contem informações sensíveis

## 🧰 **Tecnologias Utilizadas**

- 🐍 **Python**: Linguagem principal utilizada no desenvolvimento do back-end.
- ⚡ **FastAPI**: Framework moderno e performático para construção de APIs RESTful.
- 🔥 **Firestore Database**: Banco de dados NoSQL da Google, usado para armazenar dados em tempo real e de forma escalável.
- ☁️ **Render Web Service**: Plataforma utilizada para o deploy automatizado do back-end na nuvem.
- 🐳 **Docker**: Utilizado para criar contêineres, garantindo ambiente consistente de desenvolvimento e produção.

## 🌐 Endpoints:

### 🔧 **Back-end**  
- **Descrição**: Este é o endpoint da API desenvolvida com FastAPI. Através dele, é possível visualizar e testar os endpoints disponíveis utilizando a interface interativa gerada automaticamente pela documentação Swagger. Ideal para desenvolvedores entenderem os serviços oferecidos e testarem requisições de forma prática.

## 🧑‍💻 Instruções para Desenvolvedores

### 🔁 Clonar o Repositório

```bash```
```git clone https://github.com/PriscillaIA/poli-egs-fastapi-backend-equipe-2.git```
```cd poli-egs-fastapi-backend-equipe-2```

### 🛠️ Criar e Ativar Ambiente Virtual (Recomendado)

#### Criar o ambiente virtual:
- python -m venv nome_do_seu_ambiente

#### Entrar no venv:
- **🪟 Windows:**
```.\nome_do_seu_ambiente\Scripts\activate```

- **🐧 Linux/Mac:**
```source nome_do_seu_ambiente/bin/activate```

### 📦 Instalar Dependências:

#### Acesse a pasta FastApi e instale os pacotes do projeto:
-  ```pip install -r requirements.txt```

#### Caso esteja usando o VS Code, selecione o interpretador do ambiente virtual:
- C:\Users\NomeUsuario\nome_do_seu_ambiente\Scripts\python.exe

### ▶️ Rodar o Servidor Local:

#### Execute o servidor FastAPI a partir da raiz do projeto:

- Opção 1:
```fastapi dev app.py```

- Opção 2:
```fastapi dev app.py```

- Opção 3 (para expor publicamente):
```uvicorn app:app --host 0.0.0.0 --port 8000```
  - Observação: no comando uvicorn app:app, o primeiro app é o nome do arquivo (app.py) e o segundo é a variável FastAPI definida dentro dele (app = FastAPI()).

### ☁️ Deploy no Servidor Render
- Após um commit na branch configurada, o Render faz o deploy automaticamente. Então, é necessário cadastrar no servidor Render os links do front e back-end
- ⚠️ Atenção: verifique se todas as alterações foram testadas e validadas antes de fazer push, pois o deploy ocorrerá automaticamente.

### 🔐 Variáveis de Ambiente
- É necessário criar um arquivo .env na raiz do projeto com as chaves corretas.
- 📩 Solicite esse arquivo .env a outro desenvolvedor do projeto ou ao dono do sistema se ainda não tiver.

### 🗄️ Banco de Dados:
- Este projeto utiliza Firestore do Firebase como banco de dados NoSQL.
- Peça a outro desenvolvedor do projeto acesso ao banco de dados.

### 🐳 Executando com Docker
Isso executará o backend na porta 8000 do seu host local. Entao voce pode acessar via navegador: http://localhost:8000/docs
- Build da imagem: ```docker build -t your-image-name .```
- Executar o container: ```docker run -p 8000:8000 your-image-name```

#### 🖼️ Exemplo de execução bem-sucedida
![image](https://github.com/user-attachments/assets/3c8c93fb-9a3e-4221-9663-eefa464ccec1)

### 📑 Documentação:

### Tabela de Rastreamento de Funcionalidades
  
  ![image](https://github.com/user-attachments/assets/6062ab5d-879d-45de-9f4f-62ca36cf4b73)

## Storys Trabalhadas no Observatório 2.0 (Jira)

![Sprint 1](https://github.com/user-attachments/assets/ff19bbc9-404d-4ad5-962b-307f961c683f)

![Sprint 2](https://github.com/user-attachments/assets/1bd5f9f1-20cf-4ea6-821c-5ba50baa84d7)

![Sprint 3](https://github.com/user-attachments/assets/81f3783f-a704-4ccc-8fdf-b627fece9041)

![Sprint 4](https://github.com/user-attachments/assets/a04c48a9-560f-4d25-bd9e-d6924a47497e)

### Equipe 5 do semestre 2026.1:
- **EMMANOEL BARBOSA (DEV FRONT-END E BACK-END)**
- **JOSÉ LÚCIO (DEV FRONT-END E BACK-END)**
- **RANIE CAMPOS (DEV FRONT-END E BACK-END)**
- **DIEGO AMARAL (DEV FRONT-END E BACK-END)**
- **LUIZ ANDRÉ(SCRUM MASTER)**
- **MÁRCIA REJANE (GERENTE DE PROJETO)**


## 2026.1

# ✨ Atualização 1 – Gestão de Submissão de Desafios

A Sprint foi dedicada à implementação do fluxo completo de submissão e moderação de desafios, permitindo um gerenciamento mais seguro e organizado do conteúdo disponibilizado na plataforma.

### Funcionalidades Implementadas
- Implementação dos endpoints para criação, consulta, atualização e gerenciamento de desafios.
- Criação do fluxo de aprovação e rejeição de desafios submetidos por administradores.
- Controle de permissões baseado em perfis administrativos.
- Validação das informações enviadas antes da persistência dos dados.
- Estruturação das regras de negócio responsáveis pelo ciclo de vida dos desafios.

---

# ✨ Atualização 2 – Segurança da Plataforma

Esta Sprint concentrou-se no fortalecimento da segurança da aplicação, implementando mecanismos para reduzir vulnerabilidades e proteger a infraestrutura da API.

### Melhorias Implementadas
- Implementação de **Rate Limiting**, limitando a quantidade de requisições permitidas por usuário em um determinado intervalo de tempo.
- Mitigação de ataques de força bruta e abuso dos endpoints públicos.
- Correção de vulnerabilidades identificadas durante o processo de desenvolvimento.
- Aprimoramento das validações de autenticação e autorização.
- Fortalecimento das validações de entrada (*Input Validation*) para reduzir riscos de dados maliciosos.
- Revisão das regras de segurança da API visando maior confiabilidade da aplicação.

---

# ✨ Atualização 3 – Correção e Estabilização

Foi realizado um processo completo de estabilização da aplicação, eliminando inconsistências presentes nas versões anteriores.

### Correções Realizadas
- Resolução dos bugs identificados na implementação desenvolvida pela equipe anterior.
- Correção de falhas relacionadas ao fluxo de autenticação.
- Correção de inconsistências nos serviços e endpoints da API.
- Revisão da integração entre frontend, backend e banco de dados.
- Otimização da estabilidade geral da aplicação para ambiente de produção.

---

# ✨ Atualização 4 – Refatoração da Arquitetura

Além das correções, o backend passou por melhorias estruturais para facilitar futuras manutenções e expansões da plataforma.

### Melhorias Estruturais
- Refatoração de partes da arquitetura do backend visando maior organização do código.
- Padronização dos serviços e da estrutura dos endpoints.
- Melhor organização das responsabilidades entre *Controllers*, *Services* e modelos.
- Aprimoramento da legibilidade, modularidade e manutenção do código.
- Organização das rotas da API seguindo boas práticas de arquitetura REST.

---

# ✨ Atualização 5 – Deploy e Publicação

A etapa final concentrou-se na disponibilização da plataforma para utilização em ambiente institucional.

### Deploy
- Realizado o deploy oficial do Observatório na infraestrutura da Escola Politécnica de Pernambuco (POLI).
- Configuração do ambiente de produção utilizando Docker.
- Validação dos serviços após a publicação.
- Testes finais de integração entre frontend, backend e banco de dados.
- Verificação da estabilidade dos endpoints, autenticação e comunicação entre os serviços.
- Homologação da aplicação para utilização na rede institucional.
