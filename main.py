'''
Created by NeKro
'''

import os

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
        name = input("file name: ")
        name = (name +".py")
        print ("compiling...\n")
        try:
            os.remove(name)
            compil = open('def.py', "w")
            #copy all content    
            compil.close()
            compil = open(name, "a")
            #paste
            compil.write("\n\n\n#return commands\n\nwhile True:\n\n    check = input('')\n    if check.lower() == 'q':\n        break\n\n")
            compil.close()
            compil = open('word.py', "a")
            #copy all  content
            compil.close()
            compil = open(name, "a")
            #paste
            compil.close()
            os.remove("def.py")
            os.remove("word.py")
            print ("done\n")
        except:
            compil = open('def.py', "w")
            #copy all content    
            compil.close()
            compil = open(name, "a")
            #paste
            compil.write("\n\n\n#return commands\n\nwhile True:\n\n    check = input('')\n    if check.lower() == 'q':\n        break\n\n")
            compil.close()
            compil = open('word.py', "a")
            #copy all  content
            compil.close()
            compil = open(name, "a")
            #paste
            compil.close()
            os.remove("def.py")
            os.remove("word.py")
            print ("done\n")

    if choice == "q":
        break
    if choice == "Q":
        break

