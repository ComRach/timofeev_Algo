from tkinter import *
from random import randint
def  woops():
    print("woops...")

def tax():
    global gold
    global burg
    burg -= 2
    gold += 1
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
def man():
    global milt
    global nobl
    nobl -= 2
    milt += 1
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
def less():
    global gold
    global burg
    burg += 1
    gold -= 2
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
def disband():
    global milt
    global nobl
    nobl += 1
    milt -= 2
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
def repression():
    global milt
    global riot
    riot -= 1
    milt -= 2
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
    lbl2.configure(text="Домен: " + str(land) + ". Беспорядки: " + str(riot))
def nobl_gift():
    global gold
    global nobl
    gold -= 2
    nobl += 1
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
def conq_land():
    global milt
    global land
    land += 1
    milt -= 4
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
    lbl2.configure(text="Домен: " + str(land) + ". Беспорядки: " + str(riot))
def convert():
    global prst
    global powr
    prst -= 1
    powr += 1
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
def unity():
    global burg
    global nobl
    global powr
    powr -= 1
    burg += 1
    nobl += 1
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
def  gold_and_army():
    global powr
    global gold
    global milt
    milt += 2
    gold += 1
    powr -= 1
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))


def end_turn():
    global turn
    global gold
    global burg
    global nobl
    global prst
    global milt
    global riot
    global powr
    global land
    if turn % 12 == 0: gold += 2
    turn += 1
    btn_event2.grid()
    a = randint(1,13)
    if a <= 2:
        elbl.configure(text="О, король! Наши купцы не выдерживают конкуренции с нашими соседями! \nМногие крупные гильдии близки к разорению! Все торговцы надеются \nна помощь со стороны короны, но разрешите ли вы распорядиться частью \nвашей казны?")
        btn_event1.configure(text="Да", command=burgs_event_1a)
        btn_event2.configure(text="Нет", command=burgs_event_1b)
    elif a <= 4:
        elbl.configure(text="Король, важный представитель купеческой гильдии обратился с просьбой \nнемного ограничить безразмерные права дворян. Само собой дворяне \nбудут не рады такому изменению. Примите ли вы предложение купца?")
        btn_event1.configure(text="Да", command=burgs_event_2a)
        btn_event2.configure(text="Нет", command=burgs_event_2b)
    elif a <= 6:
        elbl.configure(text="На севере страны бушуют беспорядки. Их основная причина – недовольные \nкрестьяне, но среди бунтовщиков есть и мелкие горожане. Их бургомистры \nпросят не трогать при подавлении восстаний. Согласимся ли мы \nигнорировать некоторых бунтовщиков? ")
        btn_event1.configure(text="Да", command=burgs_event_3a)
        btn_event2.configure(text="Нет", command=burgs_event_3b)
    elif a <= 8:
        elbl.configure(text="Титул дворянства даёт множество привилегий. Многие богатые купцы покупают \nтитулы у разорённых дворян.  Однако, крупные благородные дома считают, \nчто титул должен передаваться по крови, а не деньгам. Запретим ли мы продавать титулы?")
        btn_event1.configure(text="Да", command=nobl_event_1a)
        btn_event2.configure(text="Нет", command=nobl_event_1b)
    elif a <= 10:
        elbl.configure(text="Король! В нашей стране начался конфликт двух союзов феодалов! Если не \nпрекратить внутреннюю войну, то мы потеряем часть получаемого \nополчения! Но если мы решим дать дворянам самим решать свои \nпроблемы они станут более благосклонными к вам. Будем ли мы \nигнорировать конфликт?")
        btn_event1.configure(text="Да", command=nobl_event_2a)
        btn_event2.configure(text="Нет", command=nobl_event_2b)
    elif a == 11:
        elbl.configure(text="Наступил день праздника! В этом месяце крестьяне собрали большой урожай, \nа ремесленники выгодно продали свои товары. Все приносят дары в казну, \nно если у вас не враждебные отношения со средним сословием, то они \nпринесут больше даров!")
        if burg >= 4:
            gold += 1
        gold += 1
    elif a == 12:
        elbl.configure(text="Ужасные новости! Наши враги выдвинули нам ультиматум! Либо мы отдаём \nчасть наших земель, либо они попытаются уничтожить наше королевство \nпримите ли вы их требования?")
        btn_event1.configure(text="Да", command=attacka)
        btn_event2.configure(text="Нет", command=attackb)
    else:
        elbl.configure(text="Хорошие новости! У нас появился шанс наладить отношение с духовенством! \nСамо собой, это будет стоить немалых денег, но жрецы могут повлиять на \nвсе сословия или призвать армию. Взвести все “За” и “Против” и примите \n мудрое решение…")
        btn_event1.configure(text="Наладить связи.", command=priest_event_1a)
        btn_event2.configure(text="Это слишком дорого", command=priest_event_1b)
    if burg < 1 or nobl < 1 or prst < 1 or gold < 1 or milt < 1 or powr < 1 or riot > 9 or land < 1:
        lbl1.destroy()
        lbl.destroy()
        lbl2.destroy()
        elbl.configure(text="Вы проиграли. Вы правили " + str(turn) + " месяцев")
        btn_event1.destroy()
        btn_event2.destroy()

def bring_back():
    btn_event1.configure(text="Конец хода", command=end_turn)
    btn_event2.grid_forget()


def burgs_event_1a():
    global burg
    global gold
    burg += randint(1,2)
    gold -= randint(1,2)
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
    bring_back()
def burgs_event_1b():
    global burg
    burg -= randint(1,2)
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    bring_back()
def burgs_event_2a():
    global burg
    global nobl
    burg += randint(1,2)
    nobl -= randint(1,2)
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    bring_back()
def burgs_event_2b():
    global burg
    burg -= randint(1,2)
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    bring_back()
def burgs_event_3a():
    global burg
    global riot
    burg += randint(1,2)
    riot += 1
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    lbl2.configure(text="Домен: " + str(land) + ". Беспорядки: " + str(riot))
    bring_back()
def burgs_event_3b():
    global burg
    burg -= randint(1,2)
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    bring_back()
def nobl_event_1a():
    global nobl
    global burg
    nobl += randint(1,2)
    burg -= randint(1,2)
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    bring_back()
def nobl_event_1b():
    global nobl
    nobl -= randint(1,2)
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    bring_back()
def nobl_event_2a():
    global nobl
    global milt
    nobl += randint(1,2)
    milt -= randint(1,2)
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
    bring_back()
def nobl_event_2b():
    global nobl
    nobl -= randint(1,2)
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    bring_back()
def priest_event_1a():
    global gold
    global prst
    prst += 1
    gold -= 2
    lbl.configure(text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
    bring_back()
def priest_event_1b():
    bring_back()
def attacka():
    global land
    land -=  1
    lbl2.configure(text="Домен: " + str(land) + ". Беспорядки: " + str(riot))
    bring_back()
def attackb():
    global milt
    milt -= 3
    lbl1.configure(text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
    bring_back()





gold = 5
burg = 3
nobl = 4
prst = 1
milt = 3
riot = 4
powr = 2
land = 8
turn = 1


window = Tk()
window.title("Vlad's king simulator")
window.geometry('1000x500')


topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)


lbl = Label(topFrame, text= "Горожане: " + str(burg) + ". Дворяне: " + str(nobl) + ". Духовенство: " + str(prst))
lbl1 = Label(topFrame, text="Золото: " + str(gold) + ". Армия: " + str(milt) + ". Власть: " + str(powr))
lbl2 = Label(topFrame, text="Домен: " + str(land) + ". Беспорядки: " + str(riot))
elbl =Label(topFrame, text = 'Добро пожаловать!')
lbl.grid(column=0, row=0)
lbl1.grid(column=0, row=1)
lbl2.grid(column=0, row=2)
elbl.grid(column=0, row=5)

btn1 = Button(bottomFrame, text="Собрать дополнительные налоги", command=tax)
btn1.grid(column=0, row=0)
btn2 = Button(bottomFrame, text="Собрать феодальное ополчение", command=man)
btn2.grid(column=1, row=0)
btn3 = Button(bottomFrame, text="Снизить пошлины", command=less)
btn3.grid(column=2, row=0)
btn4 = Button(bottomFrame, text="Распустить часть войск", command=disband)
btn4.grid(column=3, row=0)
btn6 = Button(bottomFrame, text="Подавить восстания", command=repression)
btn6.grid(column=4, row=0)
btn7 = Button(bottomFrame, text="Заплатить дворянам", command=nobl_gift)
btn7.grid(column=1, row=2)
btn9 = Button(bottomFrame, text="Захватить территори", command=conq_land)
btn9.grid(column=2, row=2)
btn10 = Button(bottomFrame, text="Увеличить власть", command=convert)
btn10.grid(column=1, row=1)
btn11 = Button(bottomFrame, text="Успокоить сословия", command=unity)
btn11.grid(column=2, row=1)
btn11 = Button(bottomFrame, text="Собрать золото и армию", command=gold_and_army)
btn11.grid(column=3, row=1)
btn_event1 = Button(topFrame, text="Конец хода", command=end_turn)
btn_event1.grid(column=0,row=7)
btn_event2 = Button(topFrame, text="Нет", command=woops)
btn_event2.grid(column=1,row=7)
btn_event2.grid_forget()


window.mainloop()
