def metros_millas(metros):
    millas = metros * 0.000621371
    return millas

def millas_metros(millas):
    metros = millas * 1609.34
    return metros

def millas_pies(millas):
    pies = millas * 5280
    return pies

def pies_millas(pies):
    millas = pies / 5280
    return millas

def metros_pies(metros):
    pies = metros * 0.3048
    return pies

def pies_metros(pies):
    metros = pies * 3.28084
    return metros


print("=== Conversor de Unidades ====")

while True:
    try:
        print("\n\n--- Elija la conversión a realizar ---")
        eleccion = int(input("1.Metros a millas.\n2.Millas a metros.\n3.Millas a pies.\n4.Pies a millas.\n5.Metros a pies.\n6.Pies a metros.\n\n"))
        match eleccion:
            case 1:
                print("\n____________ Metros a millas ____________")
                metros = float(input("Ingrese los metros:\t"))
                resultado = metros_millas(metros)
                print(f"{metros} m = {round(resultado, 2)} millas")
                continue
            
            case 2:
                print("\n____________ Millas a metros ____________")
                millas = float(input("Ingrese las milllas:\t"))
                resultado = millas_metros(millas)
                print(f"{millas} millas = {round(resultado, 2)} m")

            case 3:
                print("\n____________ Millas a pies ____________")
                millas = float(input("Ingrese las millas:\t"))
                resultado = millas_pies(millas)
                print(f"{millas} millas = {round(resultado, 2)} pies")

            case 4:
                print("\n____________ Pies a millas ____________")
                pies = float(input("Ingrese los pies:\t"))
                resultado = pies_millas(pies)
                print(f"{pies} pies = {round(resultado, 2)} millas")
            
            case 5:
                print("\n____________ Metros a pies ____________")
                metros = float(input("Ingrese los metros:\t"))
                resultado = metros_pies(metros)
                print(f"{metros} m = {round(resultado, 2)} pies")

            case 6:
                print("\n____________ Pies a metros ____________")
                pies = float(input("Ingrese los pies:\t"))
                resultado = pies_metros(pies)
                print(f"{pies} pies = {round(resultado, 2)} m")

            case 7:
                print("Saliendo del conversor")
                break

            case _:
                print("Elección no válida.")
    except:
        print("Valor ingresado incorrecto")