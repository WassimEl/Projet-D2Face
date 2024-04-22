CREATE TABLE IF NOT EXISTS
    USER (
        userID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        username TEXT,
        email TEXT,
        password TEXT,
        type_of_user TEXT
    );

CREATE TABLE IF NOT EXISTS
    CHARACTERS (
        characterID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        character_name TEXT,
        character_class TEXT,
        character_level INTEGER,
        align TEXT,
        race TEXT,
        xp INTEGER,
        strength INTEGER,
        dexterity INTEGER,
        constitution INTEGER,
        intelligence INTEGER,
        wisdom INTEGER,
        charisma INTEGER,
        acrobatics INTEGER,
        arcana INTEGER,
        athletics INTEGER,
        stealth INTEGER,
        animal_handling INTEGER,
        sleight_of_hand INTEGER,
        history INTEGER,
        intimidation INTEGER,
        investigation INTEGER,
        medicine INTEGER,
        nature INTEGER,
        perception INTEGER,
        insight INTEGER,
        persuasion INTEGER,
        religion INTEGER,
        performance INTEGER,
        survival INTEGER,
        deception INTEGER,
        initiative INTEGER,
        character_hp INTEGER,
        death_counter INTEGER,
        traits TEXT,
        ideal TEXT,
        links TEXT,
        defaults TEXT,
        sorts TEXT,
        equipments TEXT,
        capacity TEXT,
        userID INTEGER,
        FOREIGN KEY (userID) REFERENCES user(userID)
    );

CREATE TABLE IF NOT EXISTS
    CAMPAIGN (
        campaignID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        campaign_name TEXT,
        c_creation_time DATETIME,
        userID INTEGER,
        FOREIGN KEY (userID) REFERENCES user(userID)
    );

CREATE TABLE IF NOT EXISTS
    INSCRIPTION (
        inscriptionID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        i_creation_time DATETIME,
        userID INTEGER,
        campaignID INTEGER,
        FOREIGN KEY (userID) REFERENCES user(userID),
        FOREIGN KEY (campaignID) REFERENCES campaign(campaignID)
    );