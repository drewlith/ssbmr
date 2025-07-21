# Create Credits file by drewlith
import sys
name = sys.argv[1]
mod_creator = input("Enter modder's name: ")
mod_name = input("Enter mod name: ")
character = input("Enter character + color: ")
link = input("Enter link to mod: ")

file = open(name[:-4] + ".txt", 'w')
file.write(mod_name + " | " + character +
           "\nCreated by: " + mod_creator +
           "\n" + link)
