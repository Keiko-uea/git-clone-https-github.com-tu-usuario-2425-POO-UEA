import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Diarias Keiko")

        self.tareas = []

        # Componentes de la interfaz
        self.label_nueva_tarea = tk.Label(root, text="Nueva Tarea:")
        self.label_nueva_tarea.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entry_nueva_tarea = tk.Entry(root, width=40)
        self.entry_nueva_tarea.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.entry_nueva_tarea.bind("<Return>", self.agregar_tarea)  # Permitir agregar con Enter

        self.boton_agregar = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.boton_agregar.grid(row=0, column=2, padx=5, pady=5)

        self.label_tareas = tk.Label(root, text="Tareas:")
        self.label_tareas.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.listbox_tareas = tk.Listbox(root, width=50)
        self.listbox_tareas.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
        self.listbox_tareas.bind("<Double-Button-1>", self.marcar_completada_doble_click) # Opcional: doble clic

        self.boton_completada = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completada.grid(row=3, column=0, padx=5, pady=5)

        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=3, column=1, padx=5, pady=5)

        # Configuración de la grilla para que la lista se expanda
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(2, weight=1)

        self.actualizar_lista()

    def agregar_tarea(self, event=None):
        nueva_tarea = self.entry_nueva_tarea.get().strip()
        if nueva_tarea:
            self.tareas.append({"texto": nueva_tarea, "completada": False})
            self.entry_nueva_tarea.delete(0, tk.END)
            self.actualizar_lista()

    def marcar_completada(self):
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
            self.actualizar_lista()

    def marcar_completada_doble_click(self, event):
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            tarea_a_eliminar = self.tareas[indice]["texto"]
            confirmacion = messagebox.askyesno("Confirmar Eliminación", f"¿Seguro que deseas eliminar la tarea: '{tarea_a_eliminar}'?")
            if confirmacion:
                del self.tareas[indice]
                self.actualizar_lista()

    def actualizar_lista(self):
        self.listbox_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            estado = "[Completada] " if tarea["completada"] else ""
            self.listbox_tareas.insert(tk.END, f"{estado}{tarea['texto']}")
            if tarea["completada"]:
                self.listbox_tareas.itemconfig(tk.END, {'fg': 'gray'}) # Opcional: cambiar color
            else:
                self.listbox_tareas.itemconfig(tk.END, {'fg': 'black'})

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()