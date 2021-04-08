#game v4 //windows update 1.0. 
import configparser
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
root.title("The Game")
day_num = 0 
heal = 10
print(sys.argv[1])
print("log " + sys.argv[2])
print("pas " + sys.argv[3])
if sys.argv[1]=="BvCk-2045-ztTS" and sys.argv[2]==log[0] or sys.argv[2]==log[1] and sys.argv[3]==pas[0] or sys.argv[3]==pas[1]:
	print("Login is ok")
	def open_game(event):
		config = configparser.ConfigParser()
		config.read("save.ini")
		inventory_1.axe = config.get("Game", "axe")
		inventory_1.gun = config.get("Game", "gun")
		inventory_1.life_centre = config.get("Game", "med")
	def save_game(event):
		config = configparser.ConfigParser()
		config.add_section("Game")
		config.set("Game", "axe", str(inventory_1.axe))
		config.set("Game", "gun", str(inventory_1.gun))
		config.set("Game", "med", str(inventory_1.life_centre))

		with open("save.ini", "w") as config_file:
			config.write(config_file)
	def rando():
		res1 = ""
		res2 = ""	
		b = random.randint(1, 6)
		is_key = random.randint(1, 15)
		is_med = random.randint(1, 10)
		print(is_key)
		print(is_med)
		global heal
		if heal < 1:
			res2 = "Вы умерли. Игра окончена"
			time.sleep(10)
			sys.exit()
		if inventory_1.life_centre == True and is_med == 5:
			heal += 1
			print("Вы использовали мед. центр!")
		if is_key == 15:
			print("Был найден ключ! Игра окончена!")
			
			inventory_1.key_for_end = True
			inventory_true.key_for_end = True
			
			sys.exit()
		if b == 1:
			res1 = "нечег нового!!"
		elif b == 3:
			res1 = "Рейдеры!!"
			if sys.argv[2] == "Bodia" and inventory_1.axe == True or inventory_1.gun == True and sys.argv[2] == "Bodia":
				res2 = "-Рейдеры"
				inventory_1.axe == False
				inventory_1.gun == False
			if sys.argv[2] == "root":
				res2 = "-Рейдеры"
			if sys.argv[2] == "Bodia" and inventory_1.axe == False:
				heal -= 1	
				res2 = "-хп. Ваше хп теперь: " + str(heal)
		elif b == 5:
			res1 = "we watch for some eat!"
			res2 = "Ваше хп теперь: " + str(heal)
		elif b == 6:
			res1 = "Опа! Топорик!"
			if sys.argv[2] == "Bodia":
				res2 = "+топор Bodia " + str(heal)
				inventory_1.axe = True
			if sys.argv[2] == "root":
				inventory_true.axe = True
		elif b == 2:
			res1 = "we find life_centre"
			if sys.argv[2] == "Bodia":
				res2 = "+мед центр Bodia " + str(heal)
				inventory_1.life_centre = True
		if sys.argv[2] == "root":
			inventory_true.life_centre = True
		elif b == 4:
			res1 = ("Опа! Пестик!")
			if sys.argv[2] == "Bodia":
				res2 = "+пистолет Bodia"
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
	b_save = Button(text="Сохранить игру")
	b_load = Button(text="Загрузить игру")	
	#bind
	b_save.bind("<Button-1>", save_game)
	b_load.bind("<Button-1>", open_game)
	b_day.bind("<Button-1>", Next_Day)
	b_inw.bind("<Button-1>", Inventory_Show)
	#pack
	b_day.pack()
	b_inw.pack()
	b_save.pack()
	b_load.pack()
	text.pack()
	root.mainloop()	
else:
	print("error2")
