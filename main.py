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
        print ("compiling...\n")
        os.remove(cmd.py)
        compil = open('def.py', "a")
        #copy all
        compil.close()
        compil = open('cmd.py', "a")
        #paste
        compil.write("\n\n\n#return commands\n\nwhile True:\n\n    check = input('')\n    if check.lower() == 'q':\n        break\n\n")
        compil.close()
        compil = open('word.py', "a")
        #copy all
        compil.close()
        compil = open('cmd.py', "a")
        #paste
        compil.close()
        os.remove(def.py)
        os.remove(word.py)
        print ("done\n")


    if choice == "q":
        break
    if choice == "Q":
        break

