import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

CHAVE_API = os.getenv("CHAVE_API")

client = genai.Client(api_key=CHAVE_API)

instrucao_agente = (
    "Você é um tutor de IA especializado em tecnologia e programação. "
    "Seu objetivo é ajudar o usuário a aprender de forma didática. "
    "Nunca dê a resposta pronta de um código logo de cara. Em vez disso, explique a lógica, "
    "faça perguntas que guiem o usuário a descobrir o erro ou a solução, e use analogias simples."
)

chat = client.chats.create(
    model="gemini-2.5-flash", 
    config=types.GenerateContentConfig(
        system_instruction=instrucao_agente,
        temperature=0.7, 
    )    
)

print("Agente de Estudos Ativo! Digite 'sair' para encerrar")

# Esse Loop eu criei para conversar com o agente pelo terminal
while True:
    pergunta_usuario = input("Você: ")
    if pergunta_usuario.lower() == 'sair':
        print("Até logo e bons estudos!")
        break
        
    # Envia a mensagem para o modelo dentro do contexto do chat
    response = chat.send_message(pergunta_usuario)
    
    print(f"\nAgente: {response.text}\n")
    print("-" * 50)