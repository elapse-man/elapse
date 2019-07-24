# auther elapse
#this is a system like ATM
import time
balance=10000
flag=1
def decorater_back(func):
    def wrapper():
        func()
        homepage()
    return wrapper
def homepage():
    page=["1.deposit","2.draw money","3.select","4.back","5.exit"]
    for i in page:
        print(i)
    choose=input("what you want to do?")
    if choose=="1" or choose=="deposit" or choose=="1.deposit":
        deposit()
    elif choose=="2" or choose=="draw money" or choose=="2.draw money":
        draw_money()
    elif choose=="3" or choose=="select" or choose=="3.select":
        select()
    elif choose=="4" or choose=="back" or choose=="4.back":
        back()
    elif choose=="5" or choose=="exit" or choose=="5.exit":
        exit()
    else:
        print("invild choose")
@decorater_back
def deposit():
    global balance
    how_much=int(input("how much you deposit?"))
    balance+=how_much
    print("deposit successfully")
    print("your balance:%f"%balance)
@decorater_back
def draw_money():
    global balance
    how_much=int(input("how much you draw?"))
    balance-=how_much
    print("draw successfully")
    print("your balance:%f"%balance)
@decorater_back
def select():
    print("your balance:%f"%balance)
def back():
    homepage()
def exit():
    global flag
    flag=0

while flag:
    homepage()


























	
	
