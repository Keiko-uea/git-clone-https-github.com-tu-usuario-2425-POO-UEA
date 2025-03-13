import tkinter as tk
from tkinter import messagebox

class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Interfaz Gráfica de Usuario")
        self.datos = []

        # Etiqueta y campo de texto para ingresar datos
        self.etiqueta = tk.Label(root, text="Ingrese un dato:")
        self.etiqueta.pack()
        self.campo_texto = tk.Entry(root)
        self.campo_texto.pack()

        # Botón para agregar datos
        self.boton_agregar = tk.Button(root, text="Agregar", command=self.agregar_dato)
        self.boton_agregar.pack()

        # Botón para limpiar datos
        self.boton_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_datos)
        self.boton_limpiar.pack()

        # Lista para mostrar datos
        self.lista = tk.Listbox(root)
        self.lista.pack()

    def agregar_dato(self):
        dato = self.campo_texto.get()
        if dato:
            self.datos.append(dato)
            self.lista.insert(tk.END, dato)
            self.campo_texto.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un dato.")

    def limpiar_datos(self):
        self.datos = []
        self.lista.delete(0, tk.END)
        self.campo_texto.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
