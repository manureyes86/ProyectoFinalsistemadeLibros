import pandas as pd 
personasData = pd.read_excel (r'.\\personas.xlsx')
listaPersonas = personasData.values.tolist()
personas = []
for p in listaPersonas:
    personas.append({

        "Identificación": p[0],
        "Nombre": p[1],
        "Primer Apellido": p[2],
        "Segundo Apellido": p[3],
        "Correo Electrónico": p[4],
        
        })

import pandas as pd 
librosData = pd.read_excel (r'.\\libros.xlsx')
listaLibros = librosData.values.tolist()
libros = []
for p in listaLibros:
    libros.append({

        "idLibro": p[0],
        "Nombre":str(p[1]),
        "Genero": p[2],
        "Autor": p[3],

        })
        
print (personas)
print (libros)
librosPrestados = []

def porNombre(p):
  return p['Nombre']
while True :
    print ("a - Ver lista de personas") 
    print ("b - Ordenar lista de personas") 
    print ("c - Imprimir registro de lista de persona") 
    print ("d - Ver lista de libros") 
    print ("e - Buscar libro") 
    print ("f - Prestar libro") 
    print ("g - Ver prestamo de libros") 
    print ("h - Salir") 
    opt = input(" Digite una opcion del Menu ")
    if opt == "h":
        break
    elif opt == "a":
        for persona in personas:
            print ("nombre: %s %s %s, Identificación: %s, Correo Electrónico: %s " % (persona["Nombre"], persona["Primer Apellido"], persona["Segundo Apellido"], persona["Identificación"], persona["Correo Electrónico"]))
    elif opt == "b":
        personas.sort(key= porNombre)
    elif opt == "c":
        try:
            indice = int( input (" Digite el indice de la Persona "))
            if personas [indice] :
                print ("nombre: %s %s %s, Identificación: %s, Correo Electrónico: %s " % (personas [indice]["Nombre"], personas [indice]["Primer Apellido"], personas [indice]["Segundo Apellido"], personas [indice]["Identificación"], personas [indice]["Correo Electrónico"]))
        except Exception:
            print("Indice no valido")
    elif opt == "d" : 
        for libro in libros : 
           print ("idLibro: %s, Nombre: %s, Genero: %s , Autor : %s " % (libro["idLibro"], libro["Nombre"], libro["Genero"], libro["Autor"]))       
    elif opt == "e":
        print ("Que quiere buscar: ")
        texto = str (input ())
        l = 0
        while (l < len(libros)):
            if(libros[l]["Nombre"].find(texto) >= 0):
                print(libros[l])
            l = l + 1
    elif opt == "f" :
        print ("Que quiere prestar: ")
        texto = str (input ())
        l = 0
        libroEncontrado = False
        while (l < len(libros)):
            if(libros[l]["Nombre"].find(texto) >= 0):
                librosPrestados.append(libros[l])
                libroEncontrado = True
            l = l + 1   
        if not libroEncontrado : 
            print ("Libro no encontrado")
    elif opt== "g" :  
        for libro in librosPrestados : 
           print ("idLibro: %s, Nombre: %s, Genero: %s , Autor : %s " % (libro["idLibro"], libro["Nombre"], libro["Genero"], libro["Autor"]))       
               
    else:
        print ("Opcion no Valida")
        




