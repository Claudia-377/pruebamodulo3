
nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']


grandes_magos = ['Harry Houdini', 'David Blaine', 'Teller']
grandes_cientificos = ['Newton', 'Hawking', 'Einstein']
otros_personajes = []


def hacer_grandioso(grandes_magos):
    for i in range(len(grandes_magos)):
        grandes_magos[i] = f"{i + 1}- {grandes_magos[i]}"   


def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)


def clasificar_nombres():
    for nombre in nombres:
        if nombre not in grandes_magos and nombre not in grandes_cientificos:
            otros_personajes.append(nombre)  


print("Lista original de nombres:")
imprimir_nombres(nombres)  


clasificar_nombres()


hacer_grandioso(grandes_magos)


print("\nMagos grandiosos:")
imprimir_nombres(grandes_magos)  

print("\nCientíficos:")
imprimir_nombres(grandes_cientificos)  

print("\nOtros:")
imprimir_nombres(otros_personajes)  