
import tkinter as tk
from tkinter import messagebox

# Diccionario con los precios de los libros
precios = {"Los juegos del hambre": 10,
		   "Harry Potter": 15,
		   "Crepúsculo": 12}

# Saldo inicial
saldo = 100


# Función que es llamada cuando el usuario hace clic en el botón "Comprar"
def comprar():
	# Obtener los valores ingresados por el usuario
	nombre = entry_nombre.get()
	email = entry_email.get()
	libro_selccionado = var_libro.get()

	# Obtener precio del libro seleccionado desde diccionario
	precio = precios[libro_selccionado]

	# Restar el precio del libro seleccionado al saldo
	global saldo
	if saldo >= precio:
		saldo -= precio

		# Escribir los datos en un archivo txt
		with open('compras.txt', 'a') as f:
			f.write(f"{nombre}, {email}, {libro_selccionado}\n")

		# Mostrar mensaje de confirmación al usuario
		messagebox.showinfo("Compra realizada", "¡Gracias por tu compra!")

	else:
		messagebox.showerror("Fondos insuficientes", "No tienes suficiente saldo para realizar esta compra")


# Crear ventana principal
root = tk.Tk()
root.title("Tienda de libros")
root.geometry("400x200")

# Agregar etiquetas y campos para ingresar datos
label_nombre = tk.Label(root, text="Nombre:")
entry_nombre = tk.Entry(root)

label_email = tk.Label(root, text="Email:")
entry_email = tk.Entry(root)

label_libro = tk.Label(root, text="Selecciona tu libro:")
var_libro = tk.StringVar(value='Elige opciones')
optionmenu = tk.OptionMenu(root, var_libro, "Los juegos del hambre", "Harry Potter", "Crepúsculo")

button_comprar = tk.Button(root, text="Comprar", command=comprar)

# Etiqueta y campo para mostrar el estado del saldo
label_saldo_actual = tk.Label(text=f"Saldo actual: {saldo}")
label_saldo_actual.grid(row=5, columnspan=2, pady=(10))

# Ubicar etiquetas y elementos dentro de la ventana utilizando grid
label_nombre.grid(row=0, column=0)
entry_nombre.grid(row=0, column=1)

label_email.grid(row=1, column=0)
entry_email.grid(row=1, column=1)

label_libro.grid(row=2, columnspan=2, pady=(5))
optionmenu.grid(row=3, columnspan=2, pady=(5))

button_comprar.grid(row=4, columnspan=2, pady=(5))

root.mainloop()


