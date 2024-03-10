import os
import math
import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Menu, Toplevel
from PIL import Image, ImageTk 
from tkinter import messagebox

main = tk.Tk()
main.resizable(False, False)
main.title("Calculadora")
main.geometry("400x600")
main.configure(background="#0A81AB")

lbtela = Label(main, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", background="#fff", relief="solid", borderwidth=3)
lbtela.place(x=100, y=50)

lbteclas = Frame(main, background="#fff", relief="solid", borderwidth=3)
lbteclas.place(x=25, y=200, width=350, height=350)

lb1 = Label(lbteclas, text="1", font=("Segoe UI",32))
lb2 = Label(lbteclas, text="2", font=("Segoe UI",32))
lb3 = Label(lbteclas, text="3", font=("Segoe UI",32))
lb4 = Label(lbteclas, text="4", font=("Segoe UI",32))
lb5 = Label(lbteclas, text="5", font=("Segoe UI",32))
lb6 = Label(lbteclas, text="6", font=("Segoe UI",32))
lb7 = Label(lbteclas, text="7", font=("Segoe UI",32))
lb8 = Label(lbteclas, text="8", font=("Segoe UI",32))
lb9 = Label(lbteclas, text="9", font=("Segoe UI",32))
lb0 = Label(lbteclas, text="0", font=("Segoe UI",32))
btnapag = Button(lbteclas, text="limpar", font=("Segoe UI",20))
lbmais = Label(lbteclas, text="+", font=("Segoe UI",32))
lbmenos = Label(lbteclas, text="-", font=("Segoe UI",32))
lbmulti = Label(lbteclas, text="X", font=("Segoe UI",32))
lbdiv = Label(lbteclas, text="/", font=("Segoe UI",32))
lbigual = Label(lbteclas, text="=", font=("Segoe UI",32))

lb1.grid(column=0, row=0, padx=10, pady=10)
lb2.grid(column=1, row=0, padx=10, pady=10)
lb3.grid(column=2, row=0, padx=10, pady=10)
btnapag.grid(column=4, row=0, padx=10, pady=10)
lb4.grid(column=0, row=1, padx=10, pady=10)
lb5.grid(column=1, row=1, padx=10, pady=10)
lb6.grid(column=2, row=1, padx=10, pady=10)
lbmais.grid(column=4, row=1, padx=10, pady=10)
lb7.grid(column=0, row=2, padx=10, pady=10)
lb8.grid(column=1, row=2, padx=10, pady=10)
lb9.grid(column=2, row=2, padx=10, pady=10)
lbmenos.grid(column=4, row=2, padx=10, pady=10)
lb0.grid(column=1, row=3, padx=10, pady=10)
lbmulti.grid(column=4, row=3, padx=10, pady=10)
lbdiv.grid(column=4, row=4, padx=10, pady=10)
lbigual.grid(column=4, row=5, padx=10, pady=10)

main.mainloop()
