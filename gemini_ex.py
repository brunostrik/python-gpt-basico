#pip install google-generativeai
import google.generativeai as genai

genai.configure(api_key=".....")
model = genai.GenerativeModel("gemini-1.5-flash")
mensagem = input("Você: ")
response = model.generate_content(mensagem)
print("IA: " + response.text)
