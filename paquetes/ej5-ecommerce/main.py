from ui_utils import mostrar_menu, capturar_opcion_menu

def main() -> None:

    menu_principal = {  'A': 'CREAR PRODUCTO',
                        'B': 'VENDER',
                        'C': 'SALIR' }

    mostrar_menu('MENÚ PRINCIPAL', 'Qué acción desea realizar?', menu_principal)
    capturar_opcion_menu(menu_principal.keys())


if __name__ == "__main__":
    main()