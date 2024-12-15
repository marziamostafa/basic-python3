""" with open('message.txt','w') as fileWrite: # w for writing(rewrite)
    fileWrite.write('started learning python') """

with open('message.txt','a') as fileWrite: # a for append
    fileWrite.write(". excited")

with open('message.txt','r') as fileRead: # r for read mode
    read=fileRead.read()
    print(read)