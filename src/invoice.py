from fpdf import FPDF
import warnings
import logging

warnings.filterwarnings("ignore")

logging.getLogger("fpdf").setLevel(logging.CRITICAL)


def monto_total(items):
    total = 0
    for i in items.values():
        total += i
    return total
    
def anadir_items(nombre, precio, cantidad):
    items[nombre] = precio * cantidad
    return items

def eliminar_items(nombre):
    items.pop(nombre)
    return items

def crear_pdf(items):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    

    factura = """
    Factura de Compra \n
    -----------------

    vaca lola
"""


    pdf.cell(200, 10, txt=factura, ln=1, align="L")
    crear_pdf = pdf.output("factura.pdf")

items = {}

print ("=== Sistema de Factura ===")

while True:
    try:
        eleccion = int(input("Seleccione la operación a realizar.\n1.Añadir Productos.\n2.Eliminar Productos.\n3.Imprimir Factura.\n4.Salir.\n\n"))

        match eleccion:
            case 1:
                print(" ---- Añadir productos a la factura ----")
                nombre = input("Ingrese el nombre del producto:\t")
                precio = float(input("Ingrese su precio unitario:\t"))
                cantidad = int(input("Ingrese la cantidad de productos:\t"))

                items = anadir_items(nombre, precio, cantidad)
                print("-" * 40)
                print(f"Producto {nombre}: S/{precio}. {cantidad} unidades.\nAñadido con existo a la factura.")
                print("-" * 40)
                
            case 2:
                print("\n ---- Eliminar productos de la factura ----")
                nombre = input("Ingrese el nombre del producto:\t")

                if nombre in items:
                    eliminar_items(nombre)
                    print(f"Producto: {nombre} eliminado de la factura.\n")
                    print("-" * 40)
                    
                else: 
                    print("Producto no encontrado.\nProductos en la lista:\n")
                    for i in items:
                        print(f"- {i}")
                    print(("-" * 40) + "\n")
            
            case 3:
                print(" ---- Imprimir factura ----")
                crear_pdf(items)

                

            case 4:
                break

    except:
        print("Operación inválida.")