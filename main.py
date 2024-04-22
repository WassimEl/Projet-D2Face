import function_database


def init_menu_main():
    print("\n----Menu Principal----")
    q_choix_1 = "[1] Utilisateur"
    q_choix_2 = "[2] Campagne"
    q_choix_3 = "[3] Quitter"
    list_menu = [q_choix_1, q_choix_2, q_choix_3]
    return list_menu


def menu_main(list_menu):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer votre choix (1-4) : "
    answer = int(input(q_status))

    match answer:
        case 1:
            boucle = True
            while boucle:
                boucle = function_database.menu_user()
            return True
        case 2:
            boucle = True
            while boucle:
                boucle = function_database.menu_campaign()
            return True
        case 3:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True


def init_db():
    db_name = function_database.get_db_n()
    sql_init_script = function_database.get_sql_s()
    function_database.init_db(db_name, sql_init_script)


def fn_app():
    boucle = True
    list_menu = init_menu_main()
    while boucle:
        boucle = menu_main(list_menu)


if __name__ == "__main__":
    init_db()
    fn_app()

        