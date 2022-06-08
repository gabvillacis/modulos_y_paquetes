from ui_utils import mostrar_menu, capturar_opcion_menu
from inventario.ui import mostrar_menu_inventario
from ventas.ui import mostrar_menu_ventas

def main() -> None:

    menu_principal = {  'A': 'INVENTARIO',
                        'B': 'VENTAS',
                        'C': 'SALIR' }

    mostrar_menu('MENÚ PRINCIPAL', '', menu_principal)
    opcion = capturar_opcion_menu(menu_principal.keys())
    
    if opcion == 'A':
        mostrar_menu_inventario()
    elif opcion == 'B':
        
    else:
        exit
        

if __name__ == "__main__":
    main()