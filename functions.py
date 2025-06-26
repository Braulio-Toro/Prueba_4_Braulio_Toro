from os import system
from time import sleep

reservas=[]
stock=20

def limpiar():
    system("cls || clear")

def tiempo(espera):
    sleep(espera)

def menu():
    print("""TOTEM AUTOATENCIÓN RESERVA STRIKE
          
1) Reservar zapatillas
2) Buscar zapatillas reservadas
3) Cancelar reserva de zapatillas
4) Salir
""")

def opc():
    while True:
        limpiar()
        menu()
        opc=input("Seleccione una opción (1-4): ").strip()
        limpiar()
        if opc=="1":
            reservar_zapatillas()
        elif opc=="2":
            buscar_zapatillas()
        elif opc=="3":
            cancelar_reserva()
        elif opc=="4":
            print("Programa terminado...")
            break
        else:
            print("Opción no válida.")
        tiempo(3)

def reservar_zapatillas():
    global stock
    if stock==0:
        print("No queda stock de reservas.")
        return
    while True:
        print("-- Reservar Zapatillas --\n")
        nombre=val_nombre("Nombre del comprador: ")
        for x in reservas:
            if nombre==x["nombre"]:
                print("ERROR! Ese nombre ya está registrado.")
                return
        codigo=input("Digite la palabra secreta para confirmar la reserva: ").strip()
        if codigo=="EstoyEnListaDeReserva":
            print(f"\nReserva realizada exitosamente para: {nombre}")
            stock-=1
            reserva={
                "nombre":nombre,
                "reser":1
            }
            reservas.append(reserva)
            return reservas
        print("La palabra secreta es incorrecta.")
        return

def buscar_zapatillas():
    global stock
    print("-- Buscar Zapatillas Reservadas --\n")
    if len(reservas)==0:
        print("No hay reservas registradas.")
        return
    nombre=val_nombre("Nombre del comprador a buscar: ")
    for x in reservas:
        if nombre==x["nombre"]:
            print("\nReserva encontrada: Estela Perez - 1 par(es) (estándar).")
            vip=input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").strip().lower()
            if vip in ("si","s"):
                print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
                stock-=1
                reservas.remove(x)
                reserva={
                    "nombre":nombre,
                    "reser":2
                }
                reservas.append(reserva)
            else:
                print("Manteniendo reserva actual.")
            return
        print("Nombre no encontrado.")

def cancelar_reserva():
    global stock
    print("-- Cancelar Reserva --\n")
    if len(reservas)==0:
        print("No hay reservas registradas.")
        return
    nombre=val_nombre("Nombre del comprador cuya reserva desea cancelar: ")
    reservavip=2
    reservanor=1
    for x in reservas:
        if nombre==x["nombre"]:
            for x in reservas:
                if reservavip==x["reser"]:
                    stock+=reservavip
                    print(stock)
                elif reservanor==x["reser"]:
                    stock+=reservanor
            reservas.remove(x)
            tiempo(0.5)
            print(f"La reserva de {nombre} ha sido cancelada.")
        else:
            print("Nombre no encontrado.")


def val_nombre(mensaje):
    while True:
        nombre=input(mensaje).strip().title()
        if len(nombre)<=2:
            print("ERROR! El nombre debe tener al menos dos letras.")
        else:
            return nombre
        
