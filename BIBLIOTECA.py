#BIBLIOTECA BABY
class bibliotaca:
    def __init__(self, nombre_libro, autor, prota):
        self.nombre_libro = nombre_libro
        self.autor = autor
        self.prota = prota


    def mostrar_informacion(self):
        print(f"nombre_libro : {self.nombre_libro}")
        print(f"autor : {self.autor}")
        print(f"prota : {self.prota}")


#CREACION DE INSTANCIAS
LIB1 = bibliotaca("Cien años de soledad", "Gabriel García Márquez", "José Arcadio Buendía")
LIB2 = bibliotaca("El principito", "Antoine de Saint-Exupéry", "El principito obvioo")
LIB3 = bibliotaca("Harry Potter y la piedra filosofal", "J.K. Rowling", "Harry Potter")


#MOSTRAR INFORMACION
LIB1.mostrar_informacion()
LIB2.mostrar_informacion()
LIB3.mostrar_informacion()

#-------------------------------------------------EJEMPLO CON POLIMORFISMO-----------------------------------------------

#BIBLIOTECA BABY

# Clase base
class biblioteca:
    def __init__(self, nombre_libro, autor, prota):
        self.nombre_libro = nombre_libro
        self.autor = autor
        self.prota = prota

    def mostrar_informacion(self):
        print(f"nombre_libro : {self.nombre_libro}")
        print(f"autor : {self.autor}")
        print(f"prota : {self.prota}")

# Clases hijas POLIMORFISMO
class libro_infantil(biblioteca):
    def mostrar_informacion(self):
        print(f"Libro Infantil, el mejor: '{self.nombre_libro}' de {self.autor}. Protagonista: {self.prota}")

class libro_fantasia(biblioteca):
    def mostrar_informacion(self):
        print(f"Libro de Fantasía: '{self.nombre_libro}' - Autor: {self.autor}. Personaje principal: {self.prota}")

class libro_clasico(biblioteca):
    def mostrar_informacion(self):
        print(f"Clásicoo literario: '{self.nombre_libro}' escrito por {self.autor}. Protagonista: {self.prota}")


# CREACIÓN DE INSTANCIAS
LIB1 = libro_clasico("Cien años de soledad", "Gabriel García Márquez", "José Arcadio Buendía")
LIB2 = libro_infantil("El principito", "Antoine de Saint-Exupéry", "El principito")
LIB3 = libro_fantasia("Harry Potter y la piedra filosofal", "J.K. Rowling", "Harry Potter")

# POLIMORFISMO EN ACCIÓN
biblioteca_total = [LIB1, LIB2, LIB3]

for libro in biblioteca_total:
    libro.mostrar_informacion()

#----------------------------biblioteca baby con heredad---------------------------------------------
# BIBLIOTECA BABY
class Biblioteca:
    def __init__(self, nombre_libro, autor, prota):
        self.nombre_libro = nombre_libro
        self.autor = autor
        self.prota = prota
    def mostrar_informacion(self):
        print(f"nombre_libro : {self.nombre_libro}")
        print(f"autor : {self.autor}")
        print(f"prota : {self.prota}")

# Subclase que hereda de Biblioteca
class LibroInfantil(Biblioteca):
    def __init__(self, nombre_libro, autor, prota, edad_recomendada):
        super().__init__(nombre_libro, autor, prota)
        self.edad_recomendada = edad_recomendada

#POLIMORFISMO
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"edad_recomendada : {self.edad_recomendada}")

# CREACIÓN DE OBJETOS
LIB1 = Biblioteca("Cien años de soledad", "Gabriel García Márquez", "José Arcadio Buendía")
LIB2 = Biblioteca("El principito", "Antoine de Saint-Exupéry", "El principito obvioo")
LIB3 = LibroInfantil("Harry Potter y la piedra filosofal", "J.K. Rowling", "Harry Potter", 12)

# MOSTRAR INFORMACIÓN
LIB1.mostrar_informacion()
LIB2.mostrar_informacion()
LIB3.mostrar_informacion()