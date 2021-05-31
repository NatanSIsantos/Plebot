import re
import unicodedata
from webbot import *
from interacoes import *

'''
MÉTODOS DO PLEBOT                                  
'''
# verifica qual é a mensagem do usuário e se há resposta do plebot
def verifyMessage(message, question, response):
    verify = re.search(question, message, re.IGNORECASE)
    if (verify):
        print("PLEBOT:"+ response)
        return(True)

# controla o fluxo de mensagens do plebot        
def plebotMessage(message):

    # removendo caracteres especiais
    process = unicodedata.normalize("NFD", message)
    process = process.encode("ascii", "ignore")
    process = process.decode("utf-8")
    
    check = 'false'
    for i in range(len(listResponses)):
        if(verifyMessage(process, listResponses[i][0], listResponses[i][1])):
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
FLUXO DO PLEBOT
'''

while(True):
    message = input("\n>>>     ")
    plebotMessage(message)
