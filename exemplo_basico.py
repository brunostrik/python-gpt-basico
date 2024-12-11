from openai import OpenAI
mensagem = input("Você: ")
client = OpenAI(
    api_key=".......",  # Coloque aqui a chave de API da OpenAI
)

chat = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": mensagem,
        },
        {
            "role": "system",
            "content": "Você deve responder de forma seca e grosseira, como se estivesse irritado.", #Instrua como a IA deve agir
        }
    ],
    model="gpt-4o-mini",
)
resposta = chat.choices[0].message.content
print(resposta)