import random

menssagens_boas_vindas = [
    "Olá! Como posso ajudar você hoje? 😊",
    "Seja bem-vindo! Estou aqui para responder suas perguntas. 🚀",
    "Oi! Estou pronto para te ajudar. Vamos lá! 💬"
]

mensagem_adeus= [
    "Foi um prazer ajudar! Até a próxima. 👋",
    "Volte sempre! Qualquer dúvida, estarei aqui. 😊",
    "Até logo! Boa sorte com suas atividades. 🚀"
]

print(random.choice(menssagens_boas_vindas))


respostas = {
    "horário": "Nosso horário de funcionamento é das 9h às 18h. Geralmente temos respostas rápidas",
    "preço": "Nossos produtos variam de R$50 a R$300, vai depeder da sua necessidade na aplicação",
    "contato": "Você pode nos contatar pelo e-mail nicolas.macedof10@gmail.com.",
    "localização": "Estamos localizados na Rua Pinheiro Machado, 2614, Caxias do Sul.",
}

def chatbot_respostas(user_input):
    for keyword in respostas.keys():
        if keyword in user_input.lower():
            return respostas[keyword]
    return "Desculpe, não entendi sua pergunta. Pode reformular?"

def show_menu():
    print("\nEscolha uma das opções abaixo:")
    print("1. Horário de funcionamento")
    print("2. Preços")
    print("3. Contato")
    print("4. Localização")
    print("5. Digitar minha própria pergunta")
    print("6. Sair")

print("Bem-vindo ao Chatbot de Perguntas Frequentes!")
while True:
    show_menu()
    user_input = input("Digite a opção desejada (número ou texto): ")
    if user_input == "6" or user_input.lower() == "sair":
        print("Chatbot: Obrigado por conversar! Até logo.")
        break
    elif user_input == "1":
        print("Chatbot:", respostas["horário"])
    elif user_input == "2":
        print("Chatbot:", respostas["preço"])
    elif user_input == "3":
        print("Chatbot:", respostas["contato"])
    elif user_input == "4":
        print("Chatbot:", respostas["localização"])
    elif user_input == "5":
        custom_question = input("Digite sua pergunta: ")
        print("Chatbot:", chatbot_respostas(custom_question))
    else:
        print("Opção inválida. Por favor, escolha novamente.")
        continue
         
    
      # Perguntar se o usuário deseja continuar
    continuar = input("\nVocê deseja mais alguma coisa? (sim/não): ").strip().lower()
    if continuar == "não" or continuar == "nao":
        print(random.choice(mensagem_adeus))
        break


print(random.choice(mensagem_adeus))

