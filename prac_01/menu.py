"""get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished messag"""

MENU = """(H)ELLO
(G)OODBYE
(Q)uit"""
name = input("Enter name : ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(F"Hello {name}")
    elif choice == "G":
        print(F"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished")