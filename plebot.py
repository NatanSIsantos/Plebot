import re
import os
from flask import Flask
from interacoes import *
import web


app = Flask(__name__)


@app.route('/')
def Main():
    '''
    MÉTODOS DO PLEBOT                                  
    '''
    # verifica qual é a mensagem do usuário e se há resposta do plebot
    def verifyMessage(message, question, response):
        verify = re.search(question, message, re.IGNORECASE)
        if (verify):
            return "<h1>"+response+"</h1>"

    # controla o fluxo de mensagens do plebot
    def plebotMessage(message):
        check = 'false'
        for i in range(len(listResponses)):
            if(verifyMessage(message, listResponses[i][0], listResponses[i][1])):
                check = 'true'
                plebotExit(len(listResponses), i)
                break

        if (check == 'false'):
            return "<h1>Não entendo tais palavras, é melhor que você não esteja fazendo bruxaria.</h1>"

    # controla quando a conversação deve terminar
    def plebotExit(listLen, listPos):
        if(listPos == listLen - 1 or listPos == listLen - 2 or
                listPos == listLen - 3 or listPos == listLen - 4):
            exit(1)

    '''
    FLUXO DO PLEBOT
    '''

    while(True):
        message = web.input()
        plebotMessage(message)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
