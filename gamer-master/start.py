from tkinter import *
import os
root = Tk()
#=====================functions================
def check(event):
	a = e1.get()
	b = e2.get()
	if a == "root" or a == "Bodia":
		if b == "root" or b == "4345":
			l['text'] = "You are log in"
			l['fg'] = "green"
			os.system("python3 logins.py")
			handle = open("logs", "a")
			handle.write("\nBodia is log in;")
			handle.close()
			os.system("python3 gam_v3.py BvCk-2045-ztTS " + a + " " + b)
		else:
			l['fg'] = "red"
			l['text'] = "Uncorrect login or password"
			handle = open("logs", "a")
			handle.write("\nPassword from Bodia is incorrect;")
			handle.close()
	else:
		l['fg'] = "red"
		l['text'] = "Uncorrect login or password;"
		handle = open("logs", "a")
		handle.write("\nLogin is incorrect")
		handle.close()

#=====================objects==================
l = Label(fg="green", text="All is ok")
l1 = Label(text="Login: ")
l2 = Label(text = "Password: ")
e1 = Entry()
e2 = Entry()
b1 = Button(text = "Log in")
#=====================bind=====================

b1.bind("<Button-1>", check)

#=====================pack=====================
l.pack()
l1.pack()
e1.pack()
l2.pack()
e2.pack()
b1.pack()
#==============================================
root.mainloop()