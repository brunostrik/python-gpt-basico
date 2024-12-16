
from openai import OpenAI
mensagem = input("Você: ")
client = OpenAI(
    api_key="....."
)

chat = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": mensagem,
        }
    ],
    model="gpt-4o-mini",
    max_tokens=100,
    temperature=0.7,
)
resposta = chat.choices[0].message.content
print(resposta)