# Banco de respostas
responses = {
    "horário": "Nosso horário de funcionamento é das 9h às 18h.",
    "preço": "Nossos produtos variam de R$50 a R$300.",
    "contato": "Você pode nos contatar pelo e-mail contato@exemplo.com.",
    "localização": "Estamos localizados na Rua Exemplo, 123, São Paulo.",
}

# Função para buscar a resposta
def chatbot_response(user_input):
    for keyword in responses.keys():
        if keyword in user_input.lower():
            return responses[keyword]
    return "Desculpe, não entendi sua pergunta. Pode reformular?"

# Loop de interação
print("Bem-vindo ao Chatbot de Perguntas Frequentes! (Digite 'sair' para encerrar)")
while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        print("Chatbot: Obrigado por conversar! Até logo.")
        break
    print("Chatbot:", chatbot_response(user_input))
