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
