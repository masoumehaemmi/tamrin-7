my_dict=[]
def load():

    my_file=open("translate.txt" , "r")
    my_dict=my_file.read().split("\n")

    for i in range(0,len(my_dict),2):
            my_dict.append({"wordenglish":my_dict[i], "wordpersian" : my_dict[i+1]})
            #print([my_dict])

    print("Welcome to the translation program YASAMINJOON")


        


def show_menu():
    print("1- add new word")
    print("2- translation english2persian")
    print("3- translation persian2english")
    print("4- show_menu ")
    print("5- exit")
    


def add_new_word():
    eng=input("enter your word english to add Dictionary :")
    per=input("Enter the meaning of the word : ")

    my_dict.append({"wordenglish" : eng ,"wordpersian" : per})
    dict=open("translate.txt" , "a")
    dict.write("\n" +eng) 
    dict.write("\n" +per )
    print(" your word add a Dictionary")
    dict.close()

def translation_persian2englis():
    sentence =input ("enter your sentence : ")
    perword = sentence.split( )

    for i in range(len(my_dict)):
        for j in range (len(perword)):
            if perword[i] == my_dict[j]["wordpersian"]:
                #j=j+1
                print(my_dict[j]["wordenglish"] , end=" ")
                break
            else:
             print(perword )
                
def translation_english2persian():
    sentece = input("enter your sentence : ")
    engword = sentece.split( )

    for i in range(len(my_dict)):
        for j in range(len(engword)):
            if engword[i]==my_dict[j]["wordenglish"]:
                print(my_dict[j]["wordpersian"] , end= " ")
            else:
                print(engword)
        


while True:
    show_menu()
    choice = input("Choose one of the options : ")

    if choice=="1":
        add_new_word()
    elif choice=="2":
        translation_english2persian()
    elif choice=="3":
        translation_persian2english()
    elif choice=="4":
        show_menu()
    elif choice=="5":
        exit()