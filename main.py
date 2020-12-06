'''
Created by NeKro
'''
while True:
    choice = input("\najouter un nouveau mot : 0\ncompiler : 1\nquit : q\n")
    if choice == "0":
        word = str(input("entrer le mot de voc:")) 
        definition = str(input("entrer la defs:"))
        word_file = open('word.py', "a")
        word_file.write("elif check.lower() == '"+ word +"':\n print ("+ word +"())'"+ word +"'\n\n")
        word_file.close()
        def_file = open('def.py', "a")
        def_file.write("def "+ word +"():\n return '"+ definition +"'\n\n")
        def_file.close()

    if choice == "1":
        print ("compile\n")

    if choice == "q":
        break
    if choice == "Q":
        break

