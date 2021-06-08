import re
import unicodedata
from interacoes import *

'''
MÉTODO DO PLEBOT                                  
'''
# controla o fluxo de mensagens do plebot

def plebotMessage(message):

    # removendo caracteres especiais
    process = unicodedata.normalize("NFD", message)
    process = process.encode("ascii", "ignore")
    process = process.decode("utf-8")

    for i in range(len(listResponses)):
        verify = re.search(listResponses[i][0], process, re.IGNORECASE)
        if (verify):
            return({'message': "<div style='border: 1px solid #000000; background-color: #d5f4e6;'>PLEBOT<br></div>" + listResponses[i][1]})

    return({'message': "PLEBOT<br>Não entendo tais palavras, é melhor que você não esteja fazendo bruxaria."})

