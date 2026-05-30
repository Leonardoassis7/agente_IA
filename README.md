# 🤖 Agente de Estudos com Gemini

Meu primeiro projeto de Agente de IA voltado para estudos e aprendizado em programação.

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de criar um agente de estudos utilizando a API do Google Gemini. O agente atua como um tutor virtual de tecnologia e programação, ajudando o usuário a aprender de forma mais didática.

Ao invés de fornecer respostas prontas imediatamente, o agente busca:

* Explicar conceitos passo a passo.
* Incentivar o raciocínio lógico.
* Fazer perguntas que ajudem o usuário a encontrar a solução.
* Utilizar exemplos e analogias simples para facilitar o aprendizado.

A interação acontece diretamente pelo terminal, mantendo o contexto da conversa durante toda a sessão.

---

## Tecnologias Utilizadas

* Python 3
* Google Gemini API
* Google GenAI SDK
* python-dotenv

---

## Estrutura do Projeto

```bash
projeto/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## Configuração

### Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### Configure a chave da API

Para utilizar o projeto, você precisará de uma chave da API do Gemini.

Acesse o Google AI Studio.
Faça login com sua conta Google.
Gere uma nova chave de API.
Crie um arquivo .env na raiz do projeto.
Adicione sua chave conforme o exemplo abaixo:
CHAVE_API=sua_chave_api_aqui

---

## Executando o Projeto

Execute o arquivo principal:

```bash
python main.py
```

Saída esperada:

```text
Agente de Estudos Ativo! Digite 'sair' para encerrar
```

Para finalizar a conversa:

```text
Você: sair
Até logo e bons estudos!
```

---

## 💡 Exemplo de Uso

```text
Você: O que é uma função em Python?

Agente: Pense em uma função como uma máquina...
```

---

## Objetivo do Projeto

Este projeto foi criado como meu primeiro agente de inteligência artificial utilizando a API do Gemini.

Além de aprender sobre integração com modelos de IA, o objetivo foi desenvolver uma ferramenta que incentive o aprendizado ativo, ajudando estudantes e iniciantes em programação a compreender conceitos em vez de apenas copiar respostas.

---

## Aprendizados

Durante o desenvolvimento deste projeto, pratiquei:

* Consumo de APIs de IA.
* Uso de variáveis de ambiente com `.env`.
* Criação de chats com contexto persistente.
* Engenharia de Prompt (Prompt Engineering).
* Estruturação de aplicações Python.

---

## 🔮 Melhorias Futuras

* Interface gráfica.
* Histórico de conversas salvo em arquivo.
* Suporte a múltiplas áreas de estudo.
* Integração com banco de dados.
* Versão web utilizando Flask ou FastAPI.

---

## 👨‍💻 Autor

Desenvolvido por **LEONARDO ROBERTO DE ASSI** como parte dos estudos em Inteligência Artificial e Python.
Linkedin: https://www.linkedin.com/in/leonardo-assis-a0614a185/?skipRedirect=true

Se este projeto foi útil para você, considere deixar uma estrela no repositório.

Primeira Versão do Projeto
<img width="1360" height="696" alt="image" src="https://github.com/user-attachments/assets/bbd8e04d-35f5-429d-9a3f-04c5ea4fe28e" />

