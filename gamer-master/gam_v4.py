#game v3
from tkinter import *
from reg import log, pas, inventory_1, inventory_true
import sys
import random
import colorama
from colorama import Fore, Back, Style
import time
colorama.init()
time.sleep(3)
root = Tk()
day_num = 0 
print(sys.argv[1])
print("log " + sys.argv[2])
print("pas " + sys.argv[3])
if sys.argv[1]=="BvCk-2045-ztTS" and sys.argv[2]==log[0] or sys.argv[2]==log[1] and sys.argv[3]==pas[0] or sys.argv[3]==pas[1]:
	print("Login is ok")
	def rando():
		res1 = ""
		res2 = ""	
		b = random.randint(1, 6)
		if b == 1:
			res1 = "today is nothing happend!"
		elif b == 3:
			res1 = "Raders is here!"
			if sys.argv[2] == "Bodia" and inventory_1.axe == True:
				res2 = "-raders, -axe"
				inventory_1.axe == False
			if sys.argv[2] == "root":
				res2 = "-raders"	
		elif b == 5:
			res1 = "we watch for some eat!"
		elif b == 6:
			res1 = "we find axe!"
			if sys.argv[2] == "Bodia":
				res2 = "+axe Bodia"
				inventory_1.axe = True
			if sys.argv[2] == "root":
				inventory_true.axe = True
		elif b == 2:
			res1 = "we find life_centre"
			if sys.argv[2] == "Bodia":
				res2 = "+life Bodia"
				inventory_1.life_centre = True
		if sys.argv[2] == "root":
			inventory_true.life_centre = True
		elif b == 4:
			res1 = ("we find gun!")
			if sys.argv[2] == "Bodia":
				res2 = "+gun Bodia"
				inventory_1.gun = True
			if sys.argv[2] == "root":
				inventory_true.gun = True
		return res1, res2
	def Next_Day(event):
		global day_num
		day_num += 1
		text.delete(1.0, END)
		text.insert(1.0, "Следующий день №" + str(day_num))
		result = rando()
		text.insert(END, result)
	def Inventory_Show(event):
		if sys.argv[2] == 'Bodia':
			text.delete(1.0, END)
			text.insert(1.0, "Топорик: " + str(inventory_1.axe) + " Мед. Центр " + str(inventory_1.life_centre) + " Пистолет " + str(inventory_1.gun))
		if sys.argv[2] == 'root':
			text.delete(1.0, END)
			text.insert(1.0, "Топорик: " + str(inventory_true.axe) + " Мед. Центр " + str(inventory_true.life_centre) + " Пистолет " + str(inventory_true.gun))
	#objects
	text = Text()
	b_day = Button(text="След. день")		
	b_inw = Button(text="Инвентарь")
	#bind
	b_day.bind("<Button-1>", Next_Day)
	b_inw.bind("<Button-1>", Inventory_Show)
	#pack
	b_day.pack()
	b_inw.pack()
	text.pack()
	root.mainloop()	
else:
	print("error2")
