import math as m
import random as r
import mysql as d

code=0
roomno=0
def booking():
    s='0123456789abcdefghifklmnopqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZ'
    otp=""
    l=len(s)
    for i in range(8):
        otp=otp+s[m.floor(r.random()*l)]
    print("CUSTOMER CODE:",otp)
    code=otp
    name=input("Enter Customer's Name :")
    phno=input("Enter Customer's Phone Number :")
    address=input("Enter Customer's Address :")
    tdays=int(input("Enter Total Number of Days :"))
    print("__ROOM TYPES__")
    print("1. DEXLUXE ROOM - RS.5000_PN (INCLUDING TAXES)")
    print("2. SUPER DEXLUXE ROOM - RS.6000_PN(INCLUDING TAXES)")
    print("3. SUITE ROOM - RS.7500_PN(INCLUDING TAXES)")
    print("4. DUPLEX ROOM - RS.8000_PN(INCLUDING TAXES)")
    p=int(input("ENTER YOUR CHOICE : "))
    if(p==1):
        rent=5000
        roomtype=str("DEXULE ROOM")
        roomn=r.randint(100,150)
    elif(p==2):
        roomn=r.randint(200,250)
        rent=6000
        roomtype=str("SUPER DEXULE ROOM")
    elif(p==3):
        roomn=r.randint(300,350)
        rent=7500
        roomtype=str("SUITE ROOM")
    elif(p==4):
        roomn=r.randint(400,450)
        rent=8000
        roomtype=str("DUPLEX ROOM")
    else:
        print("INVALID INPUT")
    orent=rent
    rent=int(rent*tdays)
    print("YOUR BOOKING HAS BEEN CONFIRMED")
    print("Your room number is:" ,int(roomn))
    c2=mydb.cursor()
    c2.execute("select c_roomno from s_hotel")
    roomn1=c2.fetchall()
    l=len(roomn1)
    if(l==0):
        c2.execute("INSERT INTO s_hotel values('"+str(code)+"','"+str(name)+"',"+str(phno)+",'"+str(address)+"',"+str(tdays)+","+str(roomn)+",'"+str(roomtype)+"',"+str(rent)+")")
        c2.execute("INSERT INTO ordered values('"+str(code)+"',"+str(roomn)+",'"+str(roomtype)+"',null,"+str(orent)+","+str(tdays)+")")
        mydb.commit()
    else:
        for i in range(0,l):
            if(str(roomn1[i])!=str(roomn)):
                c2.execute("INSERT INTO s_hotel values('"+str(code)+"','"+str(name)+"',"+str(phno)+",'"+str(address)+"',"+str(tdays)+","+str(roomn)+",'"+str(roomtype)+"',"+str(rent)+")")
                c2.execute("INSERT INTO ordered values('"+str(code)+"',"+str(roomn)+",'"+str(roomtype)+"',null,"+str(orent)+","+str(tdays)+")")
                mydb.commit()
                break
            else:
                print("Error")
    return

def restaurant():
        print("------------------------------------------------------------------------------------")
        print("The restaurant began with Britta’s Pensionat,")
        print("a unique guesthouse in the quaint village of Harads in Northern Sweden.")
        print("Our chefs passion for food and the best local products Sweden has to offer,")
        print("Hotel SE now has the highest quality catering to match its guest service experience.")
        print("------------------------------------------------------------------------------------")
        print("                                                                                    ")
        r=int(input("Enter the Room Number :"))
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sahitya@12132004",database="hotel")
        c1=mydb.cursor()
        c1.execute("select c_code from s_hotel where c_roomno="+str(r))
        a=c1.fetchall()
        a=str(''.join(map(str,a[0])))
        print(a)
        amt=0
        while(True):
            print("\t\t_________________________________")
            print("\t\t_________ RESTAURANT MENU________")
            print("\t\t_________________________________")
            print("                                 ")
            print("                                 ")
            print("1. MINERAL WATER----------------------> RS.50")
            print("2. COLD CAPPUCCINO--------------------> RS.100")
            print("3. HOT CAPPUCCINO---------------------> RS.150")
            print("4. DARJEELING TEA---------------------> RS.100")
            print("5. BREAKFAST BUFFET-------------------> RS.800")
            print("6. LUNCH BUFFET-----------------------> RS.1000")
            print("7. DINNER BUFFET----------------------> RS.1500")
            print("8. SPECIAL DINNER BUFFET(At Terrace)--> RS.1800")
            c=int(input("Enter the Requirement(1-7) :"))
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="sahitya@12132004",database="hotel")
            c3=mydb.cursor()
            q=0
            if(c==1):
                q=int(input("Enter the quantity :"))
                amt=amt+(50*q)
                ordered="Mineral Water"
                c3.execute("insert into ordered values('"+str(a)+"',"+str(r)+",null,'"+str(ordered)+"',50,"+str(q)+")")
                mydb.commit()
                print("THANK YOU FOR CHOOSING HOTEL_S RESTAURANT THE ITEM WILL BE IN YOUR ROOM IN FEW MINTUES")
            if(c==2):
                q=int(input("Enter the quantity :"))
                amt=amt+(100*q)
                ordered="Cold Cappuccino"
                c3.execute("insert into ordered values('"+str(a)+"',"+str(r)+",null,'"+str(ordered)+"',100,"+str(q)+")")
                mydb.commit()
                print("THANK YOU FOR CHOOSING HOTEL_S RESTAURANT THE ITEM WILL BE IN YOUR ROOM IN FEW MINTUES")
            if(c==3):
                q=int(input("Enter the quantity :"))
                amt=amt+(150*q)
                ordered="Hot Cappuccino"
                c3.execute("insert into ordered values('"+str(a)+"',"+str(r)+",null,'"+str(ordered)+"',150,"+str(q)+")")
                mydb.commit()
                print("THANK YOU FOR CHOOSING HOTEL_S RESTAURANT THE ITEM WILL BE IN YOUR ROOM IN FEW MINTUES")
            if(c==4):
                q=int(input("Enter the quantity :"))
                amt=amt+(100*q)
                ordered="Darjeeling Tea"
                c3.execute("insert into ordered values('"+str(a)+"',"+str(r)+",null,'"+str(ordered)+"',100,"+str(q)+")")
                mydb.commit()
                print("THANK YOU FOR CHOOSING HOTEL_S RESTAURANT THE ITEM WILL BE IN YOUR ROOM IN FEW MINTUES")
            if(c==5):
                q=int(input("Enter the quantity :"))
                amt=amt+(800*q)
                ordered="Breakfast Buffet"
                c3.execute("insert into ordered values('"+str(a)+"',"+str(r)+",null,'"+str(ordered)+"',800,"+str(q)+")")
                mydb.commit()
                print("THANK YOU FOR CHOOSING HOTEL_S RESTAURANT THE BUFFET HAS BEEN CONFIRMED")
            if(c==6):
                q=int(input("Enter the quantity :"))
                amt=amt+(1000*q)
                ordered="Lunch Buffet"
                c3.execute("insert into ordered values('"+str(a)+"',"+str(r)+",null,'"+str(ordered)+"',1000,"+str(q)+")")
                mydb.commit()
                print("THANK YOU FOR CHOOSING HOTEL_S RESTAURANT THE BUFFET HAS BEEN CONFIRMED")
            if(c==7):
                q=int(input("Enter the quantity :"))
                amt=amt+(1500*q)
                ordered="Dinner Buffet"
                c3.execute("insert into ordered values('"+str(a)+"',"+str(r)+",null,'"+str(ordered)+"',1500,"+str(q)+")")
                mydb.commit()
                print("THANK YOU FOR CHOOSING HOTEL_S RESTAURANT THE BUFFET HAS BEEN CONFIRMED")
            if(c==8):
                q=int(input("Enter the quantity :"))
                amt=amt+(1800*q)
                ordered="Special Dinner Buffet"
                c3.execute("insert into ordered values('"+str(a)+"',"+str(r)+",null,'"+str(ordered)+"',1800,"+str(q)+")")
                mydb.commit()
                print("THANK YOU FOR CHOOSING HOTEL_S RESTAURANT THE BUFFET HAS BEEN CONFIRMED")
            if(c>9):
                print("PLEASE ENTER THE CORRECT NEED")
            ch=input("ORDER DONE ? ")
            if ch=='y':
                st=amt*5/100
                oamt=amt
                amt=amt+st
                print("Amount=",oamt)
                print("Service TAX 5% =",st)
                print("Total Amount =",amt)
                mydb.commit()
                input("Enter Any Key To Countine:")
                break
            
def bill():
    gamt=0
    tamt=0
    print("_________________________________________")
    print("                                         ")
    print("-----------S HOTEL MANAGEMENT------------")
    print("_________________________________________")
    print("                                         ")
    t=int(input("Enter your room number : "))
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="sahitya@12132004",database="hotel")
    c3=mydb.cursor()
    c3.execute("select * from ordered where c_roomno="+str(t))
    ro=c3.fetchall()
    l=len(ro)
    sum=0
    print("_____ROOM CHARGE_____")
    print("",ro[0][2],"",ro[0][4],"*",ro[0][5],"=",int(ro[0][4])*int(ro[0][5]))
    print("_____FOOD CHARGE_____")
    gamt=int(ro[0][4])*int(ro[0][5])
    for i in range(1,l):
        tamt=int(ro[i][4])*int(ro[i][5])
        gamt=gamt+tamt
        print("",ro[i][3],"",ro[i][4],"*",ro[i][5],"=",tamt)
    print("-----------------------------------------------")
    print("                          Total              :",gamt)
    sum=int(gamt)+int(tamt*5/100)
    print("                          Service tax(5%)    :",tamt*5/100)
    print("                          Grand Total Amount :",sum)
    

def history():
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Even though you might be a world away from home, at the Hotel S we welcome you like family. Let us take you away from the stresses and demands of everyday life. Living up among the tall trees in the pine forest of Northern Sweden has never been so easy. Gaze out at Sweden’s spectacular nature from up in the Mirrorcube or the UFO. From September to March you have the chance to watch the Northern Lights illuminate the sky above you, or take a family fishing trip and learn all about the berries you pick up along the way. One thing’s for sure at the Hotel S, you’ll be inspired by your surroundings and experiences.Whether you’re looking for an adventure, a relaxing break or simply to wind down in nature, Hotel S invites you to experience nature, and our restaurant and surroundings, in the most unique and memorable way you can imagine.")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    return


import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Sahitya@12132004",database="hotel")
mycursor=mydb.cursor()
c1=mydb.cursor()
c1.execute("create table s_hotel(c_code varchar(10),c_name varchar(25),c_phno varchar(10),c_address varchar(30),c_tdays integer,c_roomno integer,c_roomtype varchar(25),c_rent integer)")
c1.execute("create table ordered(c_code varchar(10),c_roomno integer(11),r_ordered varchar(50),f_ordered varchar(50),r_amt integer(11),r_quantity integer(20))")
mydb.commit()
user=input("Enter User :")
passwd=input("Enter Password :")
ans='y'
if user=='sahitya' and passwd=='1061':
    while(ans=='y' or ans=='Y'):
        print("_________________________________________")
        print("                                         ")
        print("########## S HOTEL MANAGEMENT ##########")
        print("_________________________________________")
        print("                                         ")
        print("__1. HISTORY OF HOTEL S__")
        print("__2. BOOKING__")
        print("__3. RESTAURANT__")
        print("__4. CHECK OUT(BILL)__")
        print("__5. EXIT__")
        v_choice=int(input("Enter the Choice :"))
        rent=0
        if v_choice==1:
            history()       
        if v_choice==2:
            booking()    
        if v_choice==3:
            restaurant()
        if v_choice==4:
            bill()
            print("\t\t\tTHANK YOU FOR CHOOSING HOTEL S")
        ans=input("Enter 'Y' to continue and 'N' to Exit :")

