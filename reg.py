#!/usr/bin/python
# -*- coding: UTF8 -*-
import time
import os
import os.path
import sys
print("[+] Вы запустили программу регистрации и записи")
time.sleep(3)
print("[?] Идет настройка, ожидайте....")
os.system("bash install.sh")
print("[+] Настройка системы завершенна, начата обработка данных")

log = ["Bodia", "root"]
pas = ["4345", "root"]
class inventory_1:
	axe = False
	gun = False
	life_centre = False
	key_to_end = False
class inventory_true:
	axe = True
	gun = True
	life_centre = True
	key_to_end = False
time.sleep(2)
print("[+] Настройка завершенна!")
print("[?] Начата проверка целостности игры")
if os.path.exists("gam_v4.py") == True and os.path.exists("install.sh") == True and os.path.exists("LICENSE") and os.path.exists("start.py") == True:
	print("[+] Проверка окончена! Скрипт завершил роботу")
else:
	print("[-] Проверка не пройдена!")
	sys.exit()