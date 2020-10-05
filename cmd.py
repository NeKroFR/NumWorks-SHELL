def HelloWorld():
    return "HELLO WORLD"

def CMD2():
    return "CECI EST UNE DEUXIEME COMMANDE"

def CMD3():
    return "CECI EST UNE TROISIEME COMMANDE"







while True:

    check = input("")
    if check.lower() == "hello":
        print (HelloWorld())
    

    elif check.lower() == "cmd2":
        print (CMD2())

    elif check.lower() == "cmd3":
        print (CMD3())

    elif check.lower() == "quit":
        break