definition = str(input("entrer les defs:")) 
def_file = open('def.py', "a")
def_file.write("def "+ definition +"():\n return '"+ definition +"'\n")
def_file.close()
