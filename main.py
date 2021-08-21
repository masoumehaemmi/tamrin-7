
from pyfiglet import Figlet
import qrcode

def load():

        print("loading......")

        myfile=open("database.txt", "r")
        bigtest= myfile.read()
        rows=bigtest.split("\n")
        for i in range (len(rows)):
            production_info=rows[i].split(",")
            mydict={}
            mydict["id"]=int(production_info[0])
            mydict["name"]=production_info[1]
            mydict["price"]=float(production_info[2])
            mydict["count"]=int(production_info[3])
            PRODUCTION.append(mydict)
        print("Wellcome")
PRODUCTION=[]

def addkala():
    
    id = int(input("enter your add for  id kala:"))
    name = input('enter your name: ')
    price = float(input('enter your price: '))
    count = int(input('enter your count: '))
    productDict = {}
    productDict['id'] = id
    productDict['name'] = name
    productDict['price'] = int(price)
    productDict['count'] = int(count)
    PRODUCTION.append(productDict)
    print(PRODUCTION) 
    print("add product")

def show_list():
    for i in range(len(PRODUCTION)):
        print(PRODUCTION[i]["id"], "\t" ,PRODUCTION[i]["name"], "\t" ,PRODUCTION[i]["price"], "\t" ,PRODUCTION[i]["count"], "\t" ,)

def show_edit_menu():
    print("1- name")
    print("2- price")
    print("3- count")
    print("4- end")

def editkala():

    id = int(input("enter your idkala for edit :"))
    for i in range (len(PRODUCTION)):
    
        if PRODUCTION[i]["id"] == id:
            while True:
                show_edit_menu()
                choice=int(input("choice from edit menu:"))
                if choice == 1:
                    new_name =input("enter your new name :")
                    PRODUCTION[i]["name"]== new_name
                elif choice == 2:
                    new_price =float(input("enter your new price:"))
                    PRODUCTION[i]["price"] == new_price
                elif choice ==3 :
                    new_count =int(input("enter your new count :"))
                    PRODUCTION[i]["count"] == new_count
                elif choice == 4:
                    break
                else:
                    print("idkala mojod nemibashad")

def delkala():
    id= int(input("enter your id kala for delete :"))
    
    for i in range(len(PRODUCTION)):
        if PRODUCTION[i]["id"]==id:
            PRODUCTION.pop(i)
            print("hazf shod")
            break
           
def searchkala():
    
        user_keyword = input("your id kala or name for jostojo :")

        for i in range(len(PRODUCTION)):
        
           if PRODUCTION[i]['name'] == user_keyword or str(PRODUCTION[i]["id"])== user_keyword:
            print(PRODUCTION[i]) 

def ShowQrcode():
    idqr=input('Enter id kala for qrcode:')
    for i in range(len(PRODUCTION)):
        if idqr==PRODUCTION[i]['id']:
          myqr=qrcode.make(PRODUCTION[i])
          myqr.save(f'qrcode{i}.png')
          print('QrCode created')    


def buykala() :

    basket=[]
    while True:

        id = int(input("enter your id kala :"))
            
        for i in range (len(PRODUCTION)):
            if PRODUCTION[i]["id"]== id:
                count= int(input("enter count :"))

                if PRODUCTION[i]["count"]>=count:
                        basket.append({"name":PRODUCTION[i]["name"],
                                    "price":PRODUCTION[i]["price"],
                                    "count":count })
                        PRODUCTION[i]["count"] -= count
                        print("kala add to basket")

                else:
                    print("not exit!")
                    print("we have",PRODUCTION[i]["count"] , "from this product")
            
        choice=input("do you want to continue? (y/N")
        if choice == "N" or choice == "n":
            break
    print(basket)  
    total_price=0
    for i in range(len(basket)):  
        total_price +=basket[i]["price"] * basket[i]["count"] 
    print("total price is : " , total_price)
    print("tankyou for buy ")

def save_and_exit():
    my_file= open("database.txt","w")
    r=0
    for i in range(len(PRODUCTION)):
        row = str(PRODUCTION[i]["id"]) + ',' + (PRODUCTION[i]["name"]) + "," + str(PRODUCTION[i]["price"]) + ',' + str(PRODUCTION[i]["count"])
        my_file.write(row)
        r=r+1
        if r<len(PRODUCTION):
            my_file.write("\n")
    my_file.close()
    exit()


#def show_list():
#    for i in range(len(PRODUCTION)):
#        print(PRODUCTION[i] )

def show_menu():

    print("1- add product")
    print("2-edit product")
    print("3- delete product")
    print("4- search")
    print("5-show list")
    print("6-buy")
    print("7- qrcode")
    print("8- exit")

load()
        
f=Figlet(font="standard")
print(f.renderText("YASAMIN   STORE"))


while True:

    show_menu()
    choice= int(input("please choose a number : "))

    if choice ==1:
        addkala()
    elif choice==2:
        editkala()
    elif choice==3:
        delkala()
    elif choice==4:
        searchkala()
    elif choice==5:
        show_list()
    elif choice==6:
        buykala()
    elif choice==7:
        ShowQrcode()  
    elif choice==8:
        save_and_exit()
        
