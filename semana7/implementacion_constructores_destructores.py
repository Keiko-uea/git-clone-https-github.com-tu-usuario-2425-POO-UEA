class Libro:
    def __init__(self, titulo, autor):
        """Constructor que inicializa los atributos del objeto."""
        self.titulo = titulo
        self.autor = autor
        print(f"Libro creado: '{self.titulo}' por {self.autor}")

    def __del__(self):
        """Destructor que se llama cuando el objeto es destruido."""
        print(f"El libro '{self.titulo}' ha sido destruido.")

    def mostrar_info(self):
        """Método para mostrar la información del libro."""
        print(f"Título: {self.titulo}, Autor: {self.autor}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de Libro
    libro1 = Libro("El velero de cristal", "Jose Mauro de Vascocelos")
    libro1.mostrar_info()

    # Forzar la destrucción del objeto
    del libro1  # Esto llamará al destructor

