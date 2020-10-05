#creates commands

def HelloWorld():
    return "HELLO WORLD"

def CMD():
    return "This is a command"

def thx():
    return "Thx NeKro for this software "

def UwU():
    return "UwU "

def index():
    return "#######\nhi\ncmd/command\nthx\nuwu\nq/quit to exit\n#######"




#return commands

while True:

    check = input("")
    if check.lower() == "hi":
        print (HelloWorld())
    
    elif check.lower() == "cmd":
        print (CMD())
#you can take several spellings for one function
    elif check.lower() == "COMMAND":
        print (CMD())

    elif check.lower() == "thx":
        print (thx())
    

    elif check.lower() == "uwu":
        print (UwU())
     
    elif check.lower() == "h":
        print (index())

    elif check.lower() == "help":
        print (index())

    elif check.lower() == "q":
        break
    
    elif check.lower() == "quit":
        break
########################################################        
#Don't cheat on an exam,it's bad                       #
#                                                      #
#UwU                                                   #
#                                                      #
#Created by NeKro git: https://github.com/NeKroFR      #  
########################################################
