""" 
problem: create chatbot

steps: input / listen
       process/decide
       output/talkback
 """

greet_words= ['hi','hello','yo','hey']
bye_words  = ['bye','tata','hasla la vista']
bad_words  = ['dog','cat','idiot']
def listen():
    return input("Say something: ")

def decide(command):
    command=command.lower()
    broken_words=command.split(" ")
    for word in broken_words:
        if word in greet_words:
            talkback("Hello")
            break

    for word in broken_words:
        if word in bye_words:
            talkback("Bye")
            break

    for word in broken_words:
        if word in bad_words:
            talkback("Don't use bad words. Behave!")
            break


def talkback(response):
    print(response)

while True:
    command=listen()
    if command =="stop":
        break
    else:
       decide(command)