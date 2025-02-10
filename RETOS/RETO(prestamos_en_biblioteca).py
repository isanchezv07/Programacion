# Definir el diccionario de libros disponibles
libros = {
    'L001': {
        'titulo': 'The Great Gatsby',
        'autor': 'F. Scott Fitzgerald',
        'año': 1925
    },
    'L002': {
        'titulo': 'Ready Player One',
        'autor': 'Ernest Cline', 
        'año': 2011
    },
    'L003': {
        'titulo': '1984',
        'autor': 'George Orwell',
        'año': 1949
    },
    'L004': {
        'titulo': 'El Señor de los Anillos',
        'autor': 'J.R.R. Tolkien',
        'año': 1954
    },
    'L005': {
        'titulo': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'año': 1967
    }
}

libros_prestados = set()

def prestar_libro(codigo_libro):
    if codigo_libro not in libros:
        print("✉️ El libro no existe en la biblioteca")
        return
        
    titulo = libros[codigo_libro]['titulo']
    if titulo in libros_prestados:
        print(f"✉️ El libro '{titulo}' ya está prestado")
    else:
        libros_prestados.add(titulo)
        print(f"✉️ Libro '{titulo}' prestado con éxito")

def devolver_libro(codigo_libro):
    if codigo_libro not in libros:
        print("✉️ El libro no existe en la biblioteca")
        return
        
    titulo = libros[codigo_libro]['titulo']
    if titulo in libros_prestados:
        libros_prestados.remove(titulo)
        print(f"✉️ Libro '{titulo}' devuelto con éxito")
    else:
        print(f"✉️ El libro '{titulo}' no está prestado")

def mostrar_disponibles():
    print("\n📚 Libros disponibles para préstamo:")
    for codigo, libro in libros.items():
        if libro['titulo'] not in libros_prestados:
            print(f"- '{libro['titulo']}' ({libro['autor']}, {libro['año']})")

prestar_libro('L001')  
prestar_libro('L001')  
mostrar_disponibles()
devolver_libro('L001') 
mostrar_disponibles()
