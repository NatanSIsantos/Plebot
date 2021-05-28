import re

def verificaMessage(message, question, response):
    verifica = re.search(question, message, re.IGNORECASE)
    if (verifica):
        print(response)
        return(True)

listResponses = [[r'bom dia', "Saudações nobre cliente"], [r'boa tarde', "Saudações nobre cliente"], [r'boa noite', "Saudações nobre cliente"], [
    r'eae', "Saudações nobre cliente"], [r'oi', "Saudações nobre cliente"], [r'olá', "Saudações nobre cliente"], [r'ola', "Saudações nobre cliente"]]

while(True):
    message = input()
    check = 'false'
    for i in range(len(listResponses)):
        if(verificaMessage(message, listResponses[i][0], listResponses[i][1])):
            check = 'true'
            break
    
    if (check == 'false'):
        print("Não entendo tais palavras, você poderia estar fazendo bruxaria.")

