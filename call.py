from cProfile import label
from cgitb import text
import tkinter as tk


window = tk.Tk()
window.title('calculator')
window.geometry('500x550')
window.resizable(False, False)
window.configure(bg='black')

#функция высчитывания калькулятора
def calculate(operation):
    global formula

    if operation =='C':
        formula = ' '
    elif operation =='del':
        formula = formula[0:-1]
    elif operation =='x^2':
        formula = str((eval(formula))**2)
    elif operation =='=':
        formula = str(eval(formula))
    else:
        if formula == '0':
            formula = ' '
        formula += operation
    label_text. configure(text=formula)
# создание окна для вывода вычислений
formula = '0'
label_text = tk.Label(text=formula, font=('Roboto', 30, 'bold'), bg='black', fg='white')
label_text.place(x=11, y=50)
# создаем кнопки
buttons = ['C', 'del', '*', '=','1', '2','3','/', '4', '5', '6', '+', '7', '8', '9','-', '+/-', '0', '%', 'x^2']
x = 18
y = 140
for button in buttons:
    get_lbl = lambda x=button:calculate(x)
    tk.Button(text=button, bg='orange', font=('Roboto', 20), command=get_lbl).place(x=x, y=y, width=115, height=79)
    x += 117
    if x> 400:
        x = 18
        y += 81

window.mainloop()
