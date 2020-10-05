#creates commands

def HelloWorld():
    return "HELLO WORLD"

def CMD2():
    return "This is a secound command"

def git():
    return "Thx NeKro for this software "

def UwU():
    return "UwU "




#return commands

while True:

    check = input("")
    if check.lower() == "hello":
        print (HelloWorld())
    

    elif check.lower() == "cmd2":
        print (CMD2())

    elif check.lower() == "git":
        print (git())
        
    elif check.lower() == "uwu":
        print (UwU())
#you can take several spellings for one function

    elif check.lower() == "UWU":
        print (UwU())

     elif check.lower() == "UwU":
        print (UwU())
     
    
      elif check.lower() == "q":
        break
    
    elif check.lower() == "quit":
        break
        
#UwU
