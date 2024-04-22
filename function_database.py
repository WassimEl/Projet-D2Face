import sqlite3
import os


# FIND DB NAME
def get_db_n():
    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)
    db_name = f"{work_dir}/database.db"
    return db_name


# FIND SQL SCRIPTS
def get_sql_s():
    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)
    sql_init = f"{work_dir}/sql-scripts/init_database.sql"
    return sql_init


# INIT DATABASE
def init_db(db_name, sql_init):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name) as sqliteConnection:
            print(f"Connected to the {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                with open(sql_init, "r") as sqlite_file:
                    try:
                        sql_script = sqlite_file.read()
                    except Exception as error:
                        print(f"Error while reading the SQL script: {error}")
                        return
            except Exception as error:
                print(f"Error while opening the SQL file: {error}")
                return
            try:
                cursor.executescript(sql_script)
                print("SQLite script executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


# ============================================================#
#                    DELETE CHARACTERS                       #
# ============================================================#


# EXECUTE SQL AFFICHER CHARACTERS
def fn_read_char(db_name):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(
                    f"SELECT characterID, character_name, character_class, character_level, race FROM CHARACTERS;"
                )
                data = cursor.fetchall()
                print("SQLite script executed successfully")
                print(f"\nExecution du SELECT :")
                for line in data:
                    print(line)
                print()
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


# EXECUTE SQL SUPPRIMER CHARACTER
def delete_char(db_name, characterID):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(
                    f"DELETE FROM CHARACTER WHERE characterID = {characterID};"
                )
                print("SQLite command executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite command: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


# INIT MENU SUPPRIMER CHARACTER
def init_delete_char_menu():
    print(f"\n----Menu Supression----")
    q_choix_1 = "[1] Supprimer un personnage"
    q_choix_2 = "[2] Quitter"
    list_menu = [q_choix_1, q_choix_2]
    return list_menu


# CHOIX MENU SUPPRIMER CHARACTER
def delete_char_menu(list_menu):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer le choix : "
    status = int(input(q_status))
    match status:
        case 1:
            db_name = get_db_n()
            fn_read_char(db_name)
            q_id_status = "Entrer le choix : "
            characterID = input(q_id_status)
            delete_char(db_name, characterID)
            return True
        case 2:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True


# SUPPRIMER CHARACTER
def fn_delete_character():
    try:
        list_menu = init_delete_char_menu()
        delete_db_out = delete_char_menu(list_menu)
    except Exception as error:
        print(f"{error}")
    finally:
        return delete_db_out


# ============================================================#
#                      DELETE USER                            #
# ============================================================#


# EXECUTE SQL SUPPRIMER USER
def delete_user(db_name, user_id):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(f"DELETE FROM USER WHERE userID = {user_id};")
                print("SQLite command executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite command: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


# INIT MENU SUPPRIMER USER
def init_delete_user_menu():
    print(f"\n----Menu Supression----")
    q_choix_1 = "[1] Supprimer un utilisateur"
    q_choix_2 = "[2] Quitter"
    list_menu = [q_choix_1, q_choix_2]
    return list_menu


# CHOIX MENU SUPPRIMER USER
def delete_user_menu(list_menu):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer le choix : "
    status = int(input(q_status))
    match status:
        case 1:
            db_name = get_db_n()
            fn_read_user(db_name)
            q_id_status = "Entrer le choix : "
            user_id = input(q_id_status)
            delete_user(db_name, user_id)
            return True
        case 2:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True


# SUPPRIMER USER
def fn_delete_user():
    try:
        list_menu = init_delete_user_menu()
        delete_db_out = delete_user_menu(list_menu)
    except Exception as error:
        print(f"{error}")
    finally:
        return delete_db_out


# ============================================================#
#                      USER-CHARACTER                        #
# ============================================================#

# ============================================================#
#                      CREATE CHARACTER                      #
# ============================================================#


# EXECUTE CREATE CHARACTER FROM USER
def insert_set_character(
    db_name,
    user_id,
    character_name,
    character_class,
    character_level,
    align,
    race,
    xp,
    strength,
    dexterity,
    constitution,
    intelligence,
    wisdom,
    charisma,
    acrobatics,
    arcana,
    athletics,
    stealth,
    animal_handling,
    sleight_of_hand,
    history,
    intimidation,
    investigation,
    medicine,
    nature,
    perception,
    insight,
    persuasion,
    religion,
    performance,
    survival,
    deception,
    initiative,
    character_hp,
    death_counter,
    traits,
    ideal,
    links,
    defaults,
    sorts,
    equipments,
    capacity,
):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(
                    f"INSERT INTO CHARACTERS (character_name, character_class, character_level, align, race, xp, strength, dexterity, constitution, intelligence, wisdom, charisma, acrobatics, arcana, athletics, stealth, animal_handling, sleight_of_hand, history, intimidation, investigation, medicine, nature, perception, insight, persuasion, religion, performance, survival, deception, initiative, character_hp, death_counter, traits, ideal, links, defaults, sorts, equipments, capacity, userID) "
                    f"VALUES('{character_name}','{character_class}',{character_level},'{align}','{race}',{xp},{strength},{dexterity},{constitution},{intelligence},{wisdom},{charisma},{acrobatics},{arcana},{athletics},{stealth},{animal_handling},{sleight_of_hand},{history},{intimidation},{investigation},{medicine},{nature},{perception},{insight},{persuasion},{religion},{performance},{survival},{deception},{initiative},{character_hp},{death_counter},'{traits}','{ideal}','{links}','{defaults}','{sorts}','{equipments}','{capacity}',{user_id})"
                )
                print(f"Character created for userID : {user_id}")
            except sqlite3.Error as error:
                print(
                    f"Character not created. Error while executing SQLite script: {error}"
                )
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


# CREATE CHARACTER FROM USER
def fn_create_character(db_name, user_id):
    print(f"\n----Encoder un personnage----")
    character_name = input("Entrez le nom du personnage : ")
    character_class = input("Entrez la classe du personnage : ")
    character_level = input("Entrez le niveau du personnage : ")
    align = input("Entrez l'alignement du personnage : ")
    race = input("Entrez la race du personnage : ")
    xp = input("Entrez les points d'expérience du personnage : ")
    strength = input("Entrez les points de force du personnage : ")
    dexterity = input("Entrez les points de dextérité du personnage : ")
    constitution = input("Entrez les points de constitution du personnage : ")
    intelligence = input("Entrez les points d'intelligence du personnage : ")
    wisdom = input("Entrez les points de sagesse du personnage : ")
    charisma = input("Entrez les points de charisme du personnage : ")
    acrobatics = input("Entrez les points d'acrobatie du personnage : ")
    arcana = input("Entrez les points d'arcane du personnage : ")
    athletics = input("Entrez les points d'athlétisme du personnage : ")
    stealth = input("Entrez les points de discrétion du personnage : ")
    animal_handling = input("Entrez les points de dressage du personnage : ")
    sleight_of_hand = input("Entrez les points d'escamotage du personnage : ")
    history = input("Entrez les points d'histoire du personnage : ")
    intimidation = input("Entrez les points d'intimidation du personnage : ")
    investigation = input("Entrez les points d'investigation du personnage : ")
    medicine = input("Entrez les points de médecine du personnage : ")
    nature = input("Entrez les points de nature du personnage : ")
    perception = input("Entrez les points de perception du personnage : ")
    insight = input("Entrez les points d'acuité du personnage : ")
    persuasion = input("Entrez les points de persuasion du personnage : ")
    religion = input("Entrez les points de religion du personnage : ")
    performance = input("Entrez les points de performance du personnage : ")
    survival = input("Entrez les points survie du personnage : ")
    deception = input("Entrez les points tromperie du personnage : ")
    initiative = input("Entrez les points d'initiative du personnage : ")
    character_hp = input("Entrez les points de vie du personnage : ")
    death_counter = input("Entrez le nombre jet contre-mort du personnage : ")
    traits = input("Entrez les traits du personnage : ")
    ideal = input("Entrez les ideaux du personnage : ")
    links = input("Entrez les liens du personnage : ")
    defaults = input("Entrez les défauts du personnage : ")
    sorts = input("Entrez les attaques et sorts du personnage : ")
    equipments = input("Entrez l'équipement du personnage : ")
    capacity = input("Entrez la capacité du personnage : ")
    insert_set_character(
        db_name,
        user_id,
        character_name,
        character_class,
        character_level,
        align,
        race,
        xp,
        strength,
        dexterity,
        constitution,
        intelligence,
        wisdom,
        charisma,
        acrobatics,
        arcana,
        athletics,
        stealth,
        animal_handling,
        sleight_of_hand,
        history,
        intimidation,
        investigation,
        medicine,
        nature,
        perception,
        insight,
        persuasion,
        religion,
        performance,
        survival,
        deception,
        initiative,
        character_hp,
        death_counter,
        traits,
        ideal,
        links,
        defaults,
        sorts,
        equipments,
        capacity,
    )


# EXECUTE SQL AFFICHER LES USERS
def fn_read_user(db_name):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(f"SELECT userID, username, email, password FROM USER;")
                data = cursor.fetchall()
                print("SQLite script executed successfully")
                print(f"\nExecution du SELECT :")
                for line in data:
                    print(line)
                print()
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


# EXECUTE SQL AFFICHER LES CHARACTERS D'UN USER
def fn_read_user_character(db_name, user_id):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(
                    f"SELECT character_name, character_class, character_level, race FROM CHARACTERS WHERE userID = {user_id}"
                )
                data = cursor.fetchall()
                print("SQLite script executed successfully")
                print(f"\n Liste de(s) personnge(s) de l'utilisateur :")
                for line in data:
                    print(line)
                print()
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


# INIT MENU CHARACTER FROM USER
def init_user_menu_character():
    print(f"\n----Menu Personnage d'utilisateur----")
    q_choix_1 = "[1] Afficher les personnages de l'utilisateur"
    q_choix_2 = "[2] Ajouter un personnage"
    q_choix_3 = "[3] Supprimer un personnage"
    q_choix_4 = "[4] Quitter"
    list_menu = [q_choix_1, q_choix_2, q_choix_3, q_choix_4]
    return list_menu


# CHOIX MENU CHARACTER FROM USER
def set_user_menu_character(list_menu, user_id):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer le choix : "
    status = int(input(q_status))
    match status:
        case 1:
            db_name = get_db_n()
            fn_read_user_character(db_name, user_id)
        case 2:
            db_name = get_db_n()
            fn_create_character(db_name, user_id)
        case 3:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True


# OPTION CHARACTER FROM USER
def fn_menu_user_character(user_id):
    try:
        list_menu = init_user_menu_character()
        select_db_out = set_user_menu_character(list_menu, user_id)
    except Exception as error:
        print(f"{error}")
    finally:
        return select_db_out


# INIT SELECT USER FOR CHARACTER MENU
def init_user_menu_select():
    print(f"\n----Menu Selection Utilisateur----")
    q_choix_1 = "[1] Selectionner un utilisateur"
    q_choix_2 = "[2] Quitter"
    list_menu = [q_choix_1, q_choix_2]
    return list_menu


# CHOIX MENU SELECT USER FOR CHARACTER MENU
def set_user_menu(list_menu):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer le choix : "
    status = int(input(q_status))
    match status:
        case 1:
            db_name = get_db_n()
            fn_read_user(db_name)
            q_id_status = "Entrer le choix : "
            user_id = input(q_id_status)
            fn_menu_user_character(user_id)
            return True
        case 2:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True


# MENU SELECT USER FOR CHARACTER MENU
def fn_menu_user_select():
    try:
        list_menu = init_user_menu_select()
        user_menu_db_out = set_user_menu(list_menu)
    except Exception as error:
        print(f"{error}")
    finally:
        return user_menu_db_out


# ============================================================#
#                       CREATE USER                          #
# ============================================================#


# EXECUTE SQL CREATE USER
def insert_set_user(db_name, username, email, password):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(
                    f"INSERT INTO USER ( username, email, password) VALUES (?, ?, ?)",
                    (username, email, password),
                )
                print("User has been created")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


# INPUT OF 'CREATE USER'
def fn_create_user():
    print(f"\n----Encoder un utilisateur----")
    username = input("Entrer le nom d'utilisateur : ")
    email = input("Entrer l'adresse mail : ")
    password = input("Entrer le mot de passe : ")
    db_name = get_db_n()
    insert_set_user(db_name, username, email, password)


# ============================================================#
#                       MENU USER                            #
# ============================================================#


# INIT MENU USER
def init_menu_user():
    print("\n----Menu Utilisateur----")
    choix_1 = "[1] Créer un utilisateur"
    choix_2 = "[2] Supprimer un utilisateur"
    choix_3 = "[3] Afficher le(s) utilisateur(s)"
    choix_4 = "[4] Menu personnage de l'utilisateur"
    choix_5 = "[5] Quitter"
    list_menu = [choix_1, choix_2, choix_3, choix_4, choix_5]
    return list_menu


# CHOIX USER MENU
def set_menu_user(menu_user):
    for item in menu_user:
        print(f"{item}")
    q_status = "Entrer le choix (1-4) : "
    status = int(input(q_status))

    match status:
        case 1:
            boucle = True
            while boucle:
                boucle = fn_create_user()
            return True
        case 2:
            boucle = True
            while boucle:
                boucle = fn_delete_user()
            return True
        case 3:
            db_name = get_db_n()
            fn_read_user(db_name)
            return True
        case 4:
            boucle = True
            while boucle:
                boucle = fn_menu_user_select()
            return True
        case 5:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True


# MENU USER
def menu_user():
    try:
        list_menu = init_menu_user()
        set_user = set_menu_user(list_menu)
    except Exception as error:
        print(f"{error}")
    finally:
        return set_user


# ============================================================#
#                     DELETE CAMPAIGN                        #
# ============================================================#

# EXECUTE SQL AFFICHER LES CAMPAGNES D'UN USER
def fn_read_user_campaign(db_name, user_id):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(
                    f"SELECT campaignID, campaign_name FROM CAMPAIGN WHERE userID = {user_id}"
                )
                data = cursor.fetchall()
                print("SQLite script executed successfully")
                print(f"\n Liste de(s) campagne(s) de l'utilisateur :")
                for line in data:
                    print(line)
                print()
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


# EXECUTE SQL SUPPRIMER CHARACTER
def delete_campaign(db_name, campaign_id, user_id):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(
                    f"DELETE FROM CAMPAIGN WHERE campaignID = {campaign_id};"
                )
                print("SQLite command executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite command: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


# INIT MENU SUPPRIMER CHARACTER
def init_delete_campaign_menu():
    print(f"\n----Menu Supression----")
    q_choix_1 = "[1] Supprimer une campagne"
    q_choix_2 = "[2] Quitter"
    list_menu = [q_choix_1, q_choix_2]
    return list_menu


# CHOIX MENU SUPPRIMER CHARACTER
def delete_campaign_menu(list_menu, db_name,user_id):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer le choix : "
    status = int(input(q_status))
    match status:
        case 1:
            db_name = get_db_n()
            fn_read_user_campaign(db_name)
            q_id_status = "Entrer le choix : "
            campaign_id = input(q_id_status)
            delete_campaign(db_name, campaign_id,user_id)
            return True
        case 2:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True

# SUPPRIMER CAMPAIGN
def fn_delete_campaign(db_name, user_id):
    try:
        list_menu = init_delete_campaign_menu()
        delete_db_out = delete_campaign_menu(list_menu,db_name, user_id)
    except Exception as error:
        print(f"{error}")
    finally:
        return delete_db_out

# ============================================================#
#                     MENU CAMPAIGN                           #
# ============================================================#


# EXECUTE SQL CREATE USER
def insert_set_campaign(db_name, user_id, cpn_name):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(
                    f"INSERT INTO CAMPAIGN (campaign_name, userID) VALUES ('{cpn_name}', {user_id})"
                )
                print(f"Campaign created for userID : {user_id}")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def fn_create_campaign(db_name, user_id):
    print(f"\n----Encoder une campagne----")
    cpn_name = input("Entrez le nom de la campagne : ")
    insert_set_campaign(db_name, user_id, cpn_name)

# INIT MENU CAMPAIGN
def init_menu_campaign():
    print("\n----Menu Campagne----")
    choix_1 = "[1] Créer une campagne"
    choix_2 = "[2] Supprimer une campagne"
    choix_3 = "[3] Afficher le(s) campagne(s)"
    choix_4 = "[4] Quitter"
    list_menu = [choix_1, choix_2, choix_3, choix_4]
    return list_menu


# CHOIX MENU CAMPAIGN FROM USER
def set_user_menu_campaign(list_menu, user_id):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer le choix : "
    status = int(input(q_status))
    match status:
        case 1:
            db_name = get_db_n()
            fn_create_campaign(db_name, user_id)
        case 2:
            db_name = get_db_n()
            fn_delete_campaign(db_name, user_id)
        case 3:
            db_name = get_db_n()
            fn_read_user_campaign(db_name, user_id)
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True


# OPTION CHARACTER FROM USER
def fn_menu_user_campaign(user_id):
    try:
        list_menu = init_menu_campaign()
        select_db_out = set_user_menu_campaign(list_menu, user_id)
    except Exception as error:
        print(f"{error}")
    finally:
        return select_db_out


# INIT SELECT USER FOR CHARACTER MENU
def init_menu_campaign_select():
    print(f"\n----Menu Selection Utilisateur----")
    q_choix_1 = "[1] Selectionner un utilisateur"
    q_choix_2 = "[2] Quitter"
    list_menu = [q_choix_1, q_choix_2]
    return list_menu


# CHOIX MENU SELECT USER FOR CHARACTER MENU
def set_menu_campaign(list_menu):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer le choix : "
    status = int(input(q_status))
    match status:
        case 1:
            db_name = get_db_n()
            fn_read_user(db_name)
            q_id_status = "Entrer le choix : "
            user_id = input(q_id_status)
            fn_menu_user_campaign(user_id)
            return True
        case 2:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True


# MENU SELECT USER FOR CHARACTER MENU
def menu_campaign():
    try:
        list_menu = init_menu_campaign_select()
        user_menu_db_out = set_menu_campaign(list_menu)
    except Exception as error:
        print(f"{error}")
    finally:
        return user_menu_db_out