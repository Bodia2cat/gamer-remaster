#!/usr/bin/python
# -*- coding: UTF8 -*-
import time
import os
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
class inventory_true:
	axe = True
	gun = True
	life_centre = True
time.sleep(2)
print("[+] Настройка завершенна, скрипт выключен!")