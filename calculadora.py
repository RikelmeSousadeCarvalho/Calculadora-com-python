import tkinter as tk
from tkinter import messagebox

main = tk.Tk()
main.resizable(False, False)
main.title("Calculadora")
main.geometry("400x600")
main.configure(background="#0A81AB")

###########################################################################

num1 = 0.0
op = ""

def num1_click():
    if lbtela.cget('text') == "0":
        lbtela.config(text = "")
    lbtela.config(text = lbtela.cget('text') + "1" ) 

def num2_click():
    if lbtela.cget('text') == "0":
        lbtela.config(text = "")
    lbtela.config(text = lbtela.cget('text') + "2" ) 

def num3_click():
    if lbtela.cget('text') == "0":
        lbtela.config(text = "")
    lbtela.config(text = lbtela.cget('text') + "3" ) 

def num4_click():
    if lbtela.cget('text') == "0":
        lbtela.config(text = "")
    lbtela.config(text = lbtela.cget('text') + "4" ) 

def num5_click():
    if lbtela.cget('text') == "0":
        lbtela.config(text = "")
    lbtela.config(text = lbtela.cget('text') + "5" ) 

def num6_click():
    if lbtela.cget('text') == "0":
        lbtela.config(text = "")
    lbtela.config(text = lbtela.cget('text') + "6" ) 

def num7_click():
    if lbtela.cget('text') == "0":
        lbtela.config(text = "")
    lbtela.config(text = lbtela.cget('text') + "7" ) 

def num8_click():
    if lbtela.cget('text') == "0":
        lbtela.config(text = "")
    lbtela.config(text = lbtela.cget('text') + "8" ) 

def num9_click():
    if lbtela.cget('text') == "0":
        lbtela.config(text = "")
    lbtela.config(text = lbtela.cget('text') + "9" ) 

def num0_click():
    if lbtela.cget('text') == "0":
        lbtela.config(text = "")
    lbtela.config(text = lbtela.cget('text') + "0" ) 

def limpar():
    global op, num1
    lbtela.config(text="0")
    num1 = 0.0
    op = ""

def soma():
    global op, num1
    num1 = float(lbtela.cget('text'))
    lbtela.config(text="")
    op = "+"

def sub():
    global op, num1
    num1 = float(lbtela.cget('text'))
    lbtela.config(text="")
    op = "-"

def multi():
    global op, num1
    num1 = float(lbtela.cget('text'))
    lbtela.config(text="")
    op = "*"

def div():
    global op, num1
    num1 = float(lbtela.cget('text'))
    lbtela.config(text="")
    op = "/"

def igual():
    global op, num1
    num2 = float(lbtela.cget('text'))
    if op == "+":
        total = num1 + num2
    elif op == "-":
        total = num1 - num2
    elif op == "*":
        total = num1 * num2
    else:
        if num2 == 0:
            messagebox.showerror("Erro", "Divisão por zero!")
            return
        total = num1 / num2
    lbtela.config(text=str(total))

def back():
    x = lbtela.cget("text")
    x = x[:-1]
    lbtela.config(text=x)
    if x == "":
        limpar()

def ponto():
    text_atual = lbtela.cget('text')
    if '.' not in text_atual:
        lbtela.config(text=text_atual + ".")

def conversao_binario(decimal):
    binary = ""
    if decimal == 0:
        return "0"
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

def bin():
    x = int(lbtela.cget('text'))
    lbtela.config(text=conversao_binario(x))


def dec():
    x = int(lbtela.cget('text'), 2)
    lbtela.config(text=str(x))

###########################################################################

lbtela = tk.Label(main, text="0", background="#fff", relief="solid", borderwidth=3, anchor="e", font=("Segoe UI",32))
lbtela.place(x=25, y=50, width=350, height=100)

lbteclas = tk.Frame(main, background="#fff", relief="solid", borderwidth=3)
lbteclas.place(x=25, y=200, width=350, height=350)

lb1 = tk.Button(lbteclas, text="1", font=("Segoe UI",20), command=num1_click)
lb2 = tk.Button(lbteclas, text="2", font=("Segoe UI",20), command=num2_click)
lb3 = tk.Button(lbteclas, text="3", font=("Segoe UI",20), command=num3_click)
lb4 = tk.Button(lbteclas, text="4", font=("Segoe UI",20), command=num4_click)
lb5 = tk.Button(lbteclas, text="5", font=("Segoe UI",20), command=num5_click)
lb6 = tk.Button(lbteclas, text="6", font=("Segoe UI",20), command=num6_click)
lb7 = tk.Button(lbteclas, text="7", font=("Segoe UI",20), command=num7_click)
lb8 = tk.Button(lbteclas, text="8", font=("Segoe UI",20), command=num8_click)
lb9 = tk.Button(lbteclas, text="9", font=("Segoe UI",20), command=num9_click)
lb0 = tk.Button(lbteclas, text="0", font=("Segoe UI",20), command=num0_click)
btnapag = tk.Button(lbteclas, text="C", font=("Segoe UI",20), command=limpar)
lbmais = tk.Button(lbteclas, text="+", font=("Segoe UI",20), command=soma)
lbmenos = tk.Button(lbteclas, text="-", font=("Segoe UI",20), command=sub)
lbmulti = tk.Button(lbteclas, text="X", font=("Segoe UI",20), command=multi)
lbdiv = tk.Button(lbteclas, text="/", font=("Segoe UI",20), command=div)
lbigual = tk.Button(lbteclas, text="=", font=("Segoe UI",20), command=igual)
lbback = tk.Button(lbteclas, text="⌫", font=("Segoe UI",20), command=back)
lbponto = tk.Button(lbteclas, text=".", font=("Segoe UI",20), command=ponto)
lbbin = tk.Button(lbteclas, text="Bin", font=("Segoe UI",20), command=bin)
lbdec = tk.Button(lbteclas, text="Dec", font=("Segoe UI",20), command=dec)

lb1.grid(column=0, row=0, padx=10, pady=10)
lb2.grid(column=1, row=0, padx=10, pady=10)
lb3.grid(column=2, row=0, padx=10, pady=10)
btnapag.grid(column=0, row=3, padx=10, pady=10)
lbponto.grid(column=2, row=3, padx=10, pady=10)
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
lbdiv.grid(column=4, row=0, padx=10, pady=10)
lbigual.grid(column=5, row=0, padx=10, pady=10)
lbback.grid(column=5, row=1, padx=10, pady=10)
lbbin.grid(column=5, row=2, padx=10, pady=10)
lbdec.grid(column=5, row=3, padx=10, pady=10)

main.mainloop()
