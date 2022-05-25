import tkinter as tk

calculation =   ""

def addToCalculation(symbol):
    global calculation
    calculation += str(symbol)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)
  

def evaluateCalculation():
    global calculation
    try: 
        calculation = str(eval(calculation))
        textResult.delete(1.0, "end")
        textResult.insert(1.0, calculation)
    except:
        clearField()
        textResult.insert(1.0, "Error")

def clearField():
    global calculation
    calculation = ""
    textResult.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x275")

textResult=tk.Text(root, height=2, width=16,font=("Arial", 24))
textResult.grid(columnspan=5)

button1 = tk.Button(root, text="1", command=lambda: addToCalculation(1), width=5, font=("Arial", 14))
button1.grid(row=2, column=1)

button2 = tk.Button(root, text="2", command=lambda: addToCalculation(2), width=5, font=("Arial", 14))
button2.grid(row=2, column=2)

button3 = tk.Button(root, text="3", command=lambda: addToCalculation(3), width=5, font=("Arial", 14))
button3.grid(row=2, column=3)

button4 = tk.Button(root, text="4", command=lambda: addToCalculation(4), width=5, font=("Arial", 14))
button4.grid(row=3, column=1)

button5 = tk.Button(root, text="5", command=lambda: addToCalculation(5), width=5, font=("Arial", 14))
button5.grid(row=3, column=2)

button6 = tk.Button(root, text="6", command=lambda: addToCalculation(6), width=5, font=("Arial", 14))
button6.grid(row=3, column=3)

button7 = tk.Button(root, text="7", command=lambda: addToCalculation(7), width=5, font=("Arial", 14))
button7.grid(row=4, column=1)

button8 = tk.Button(root, text="8", command=lambda: addToCalculation(8), width=5, font=("Arial", 14))
button8.grid(row=4, column=2)

button9 = tk.Button(root, text="9", command=lambda: addToCalculation(9), width=5, font=("Arial", 14))
button9.grid(row=4, column=3)

button0 = tk.Button(root, text="0", command=lambda: addToCalculation(0), width=5, font=("Arial", 14))
button0.grid(row=5, column=2)

buttonPlus = tk.Button(root, text="+", command=lambda: addToCalculation("+"), width=5, font=("Arial", 14))
buttonPlus.grid(row=2, column=4)

buttonMinus = tk.Button(root, text="-", command=lambda: addToCalculation("-"), width=5, font=("Arial", 14))
buttonMinus.grid(row=3, column=4)

buttonMultiplication = tk.Button(root, text="*", command=lambda: addToCalculation("*"), width=5, font=("Arial", 14))
buttonMultiplication.grid(row=4, column=4)

buttonDivision = tk.Button(root, text="/", command=lambda: addToCalculation("/"), width=5, font=("Arial", 14))
buttonDivision.grid(row=5, column=4)

buttonOpen = tk.Button(root, text="(", command=lambda: addToCalculation("("), width=5, font=("Arial", 14))
buttonOpen.grid(row=5, column=1)

buttonClose = tk.Button(root, text=")", command=lambda: addToCalculation(")"), width=5, font=("Arial", 14))
buttonClose.grid(row=5, column=3)

buttonClear = tk.Button(root, text="C", command=clearField, width=11, font=("Arial", 14))
buttonClear.grid(row=6, column=3, columnspan=2)

buttonEquals = tk.Button(root, text="=", command=evaluateCalculation, width=11, font=("Arial", 14))
buttonEquals.grid(row=6, column=3, columnspan=2)


root.mainloop()
