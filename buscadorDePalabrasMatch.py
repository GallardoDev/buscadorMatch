import re

texto="Ser programador es un sueño increible"

buscar = input("Que palabra desea buscar: ")
if re.search(buscar, texto) is not None:
    print("Tengo una coincidencia en el texto")
    
else:
    print("No hay coincidencias")