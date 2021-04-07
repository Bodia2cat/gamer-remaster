#game v3
from reg import log, pas, inventory_1, inventory_true
import sys
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()
import time
time.sleep(3)
try:
	print(sys.argv[1])
	print("log " + sys.argv[2])
	print("pas " + sys.argv[3])
	if sys.argv[1]=="BvCk-2045-ztTS" and sys.argv[2]==log[0] or sys.argv[2]==log[1] and sys.argv[3]==pas[0] or sys.argv[3]==pas[1]:
		#def inww():
			#print("------------INVENTORY---------------")
			#print("axe: " + inw.axe)
			#print("gun: " + inw.gun)
			#print("life centre: " + inw.life_centre
		def rando():
			
			b = random.randint(1, 6)
			if b == 1:
				print("today is nothing happend!")
			elif b == 3:
				print("Raders is here!")
				if sys.argv[2] == "Bodia" and inventory_1.axe == True:
					print("-raders, -axe")
					inventory_1.axe == False
				if sys.argv[2] == "root":
					print("-raders")	
			elif b == 5:
				print("we watch for some eat!")
			elif b == 6:
				print("we find axe!")
				if sys.argv[2] == "Bodia":
					print("+axe Bodia")
					inventory_1.axe = True
				if sys.argv[2] == "root":
					inventory_true.axe = True
			elif b == 2:
				print("we find life_centre")
				if sys.argv[2] == "Bodia":
					print("+life Bodia")
					inventory_1.life_centre = True
				if sys.argv[2] == "root":
					inventory_true.life_centre = True
			elif b == 4:
				print("we find gun!")
				if sys.argv[2] == "Bodia":
					print("+gun Bodia")
					inventory_1.gun = True
				if sys.argv[2] == "root":
					inventory_true.gun = True
				



		def gameplay():
			print("first day!")
			rando()
			print("press '1' for continue....")
			con = input(" ")
			print("second day!")
			rando()
			print("press '1' for continue....")
			con = input(" ")
			print("third day!")
			rando()
			print("press '1' for continue....")
			con = input(" ")
			print("firth day!")
			rando()
			print("press '1' for continue....")
			con = input(" ")
			print("fifeth day!")
			rando()
			print("press '1' for continue....")
			con = input(" ")
			print("sixes day!")
			rando()
			print("press '1' for continue....")
			con = input(" ")

			

		def main():
			print(Back.GREEN + "Welcome!")
			print(Back.BLUE + "1) Play! ")
			print(Style.RESET_ALL)
			print("2) Creators")
			print("             ")
			print(Back.RED + "3) exit")
			print(Style.RESET_ALL)
			mainq = input("choose: ")
			if mainq == 1:
				print("game")
				gameplay()


			

		main()
		gameplay()
	else:
		print("error2")
except: 
	print("error1")

