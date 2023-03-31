import tkinter as tk

#Criação de janela UI
window = tk.Tk();
#Colocar nome da janela
window.title("Calculadora");

def calculate():
    operation = operator.get();
    num1 = float(entry1.get());
    num2 = float(entry2.get());
    result = 0;

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        print("Invalid operation.");

    result_label.config(text="Resultado " + str(result));

#Elementos da Parte grafica GUI

entry1 = tk.Entry(window);
entry1.pack();

operator = tk.StringVar(window);
operator.set("+");

operator_dropdown = tk.OptionMenu(window, operator, "+", "-", "*", "/", "%");
operator_dropdown.pack();

entry2 = tk.Entry(window);
entry2.pack();

calculate_button = tk.Button(window, text="Calcular", command=calculate);
calculate_button.pack();

result_label = tk.Label(window, text = "Resultado: ");
result_label.pack();

#Empacotar os elementos GUI dentro da janela
window.mainloop()