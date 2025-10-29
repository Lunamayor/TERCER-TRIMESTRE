class bibliotecaa {
    String nombre_libro;
    String autor;
    String prota;

    public bibliotecaa(String nombre_libro, String autor, String prota) {
        this.nombre_libro = nombre_libro;
        this.autor = autor;
        this.prota = prota;
    }

    public void mostrar_informacion() {
        System.out.println("nombre_libro : " + nombre_libro);
        System.out.println("autor : " + autor);
        System.out.println("prota : " + prota);
    }
}

class LibroInfantil extends bibliotecaa {
    int edad_recomendada;

    public LibroInfantil(String nombre_libro, String autor, String prota, int edad_recomendada) {
        super(nombre_libro, autor, prota);
        this.edad_recomendada = edad_recomendada;
    }

    @Override
    public void mostrar_informacion() {
        super.mostrar_informacion();
        System.out.println("edad_recomendada : " + edad_recomendada);
    }
}

public class biblioteca {
    public static void main(String[] args) {
        bibliotecaa LIB1 = new bibliotecaa("Cien años de soledad", "Gabriel García Márquez", "José Arcadio Buendía");
        bibliotecaa LIB2 = new bibliotecaa("El principito", "Antoine de Saint-Exupéry", "El principito obvioo");
        LibroInfantil LIB3 = new LibroInfantil("Harry Potter y la piedra filosofal", "J.K. Rowling", "Harry Potter", 12);

        LIB1.mostrar_informacion();
        LIB2.mostrar_informacion();
        LIB3.mostrar_informacion();
    }
}
