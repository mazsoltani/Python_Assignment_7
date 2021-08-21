from pyfiglet import Figlet
f= Figlet(font="standard")
print(f.renderText( "Dictionary."))

words=[
    {'english':'apple','persian':'sib'},
    {'english':'tree','persian':'derakht'},
    {'english':'i','persian':'man'},
    {'english':'you','persian':'shoma'}
]
# print(words)


def show_menu():
    print("Menu Dictionary")
    print("1- add new word ")
    print("2- translation english2persian ")
    print("3- translation persian2english .")
    print("4- exit")



def add_word():

 while True:
         
        add_item = input("Do You Want to Additinon Vocabulary Please Type y/n= ")
        if add_item == "y":
            english_word = input('Please enter  english word= ')
            persian_word = input('Please enter  persian word= ')
            

            for i in range(len(words)):               
                          
                dict = {}
                dict['english'] = english_word
                dict['persian'] = persian_word
                words.append(dict)
                print(words)
                print("ADD Is Successful.")
                
                break
        if add_item == "n":
            print(words)
            exit_Dictionary()
            break


def exit_Dictionary():
    while True:
        save_item = input("Do You Want to Save Please Enter s ")
        if save_item=="s":
           
            file = open("Dictionary_DB.txt","w")
            for i in range(len(words)):
                english = words[i]['english']
                persian = words[i]['persian']
                save_file = english + '\n' + persian
                file.write(str(save_file))
                if i < len(words)-1:
                    file.write("\n")
            file.close()           
            exit()
            break


# while True:
show_menu()
choice = input("Please Choose a Number Of Menu= ")

if choice =="1":
    add_word()
        

elif choice =="2":
    pass

elif choice =="3":
    pass
elif choice =="4":
    exit_Dictionary()
    

