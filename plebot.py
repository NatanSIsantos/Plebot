import re

'''
MÉTODOS DO PLEBOT                                  
'''
# verifica qual é a mensagem do usuário e se há resposta do plebot
def verifyMessage(message, question, response):
    verify = re.search(question, message, re.IGNORECASE)
    if (verify):
        print(response)
        return(True)

# controla o fluxo de mensagens do plebot        
def plebotMessage(message):
    check = 'false'
    for i in range(len(listResponses)):
        if(verifyMessage(message, listResponses[i][0], listResponses[i][1])):
            check = 'true'
            plebotExit(len(listResponses), i)
            break
    
    if (check == 'false'):
        print("Não entendo tais palavras, é melhor que você não esteja fazendo "
            + "bruxaria.")

# controla quando a conversação deve terminar            
def plebotExit(listLen, listPos):
    if( listPos == listLen - 1 or listPos == listLen - 2 or 
        listPos == listLen - 3 or listPos == listLen - 4 ):
        exit(1)

'''
RESPOSTAS DO PLEBOT
'''
                # Saudações
listResponses = [[r'boa tarde', "Saudações nobre cliente"], 
                [r'boa noite', "Saudações nobre cliente"],
                [r'bom dia', "Saudações nobre cliente"],
                [r'eae', "Saudações nobre cliente"], 
                [r'olá', "Saudações nobre cliente"], 
                [r'ola', "Saudações nobre cliente"],
                [r'oi', "Saudações nobre cliente"],
                # Despedidas
                [r'até mais', "Volte sempre que quiser o melhor produto"],
                [r'até a próxima', "Até a próxima, forasteiro..."],
                [r'adeus', "Que os deuses lhe guiem!"],
                [r'tchau', "Vá pela sombra jovem!"]]

'''
FLUXO DO PLEBOT
'''

while(True):
    message = input()
    plebotMessage(message)
