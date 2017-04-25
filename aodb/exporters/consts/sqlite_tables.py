

TN_FarmableItems = 'FarmableItems'
TN_StackableItems = 'StackableItems'
TN_ConsumableItems = 'ConsumableItems'

create_farmable_items = f'''
    CREATE TABLE IF NOT EXISTS {TN_FarmableItems} (
        uniquename STRING PRIMARY KEY,
        tier INTEGER,
        craftfamegainfactor FLOAT,
        activefarmactiondurationseconds INTEGER,
        activefarmbonus FLOAT,
        activefarmcyclelengthseconds INTEGER,
        activefarmfocuscost INTEGER,
        activefarmmaxcycles INTEGER,
        animationid STRING,
        destroyable BOOLEAN,
        kind STRING,
        maxstacksize INTEGER,
        pickupable BOOLEAN,
        placecost INTEGER,
        placefame INTEGER,
        shopcategory STRING,
        shopsubcategory1 STRING,
        uiatlas STRING,
        unlockedtocraft BOOLEAN,
        unlockedtoplace BOOLEAN,
        weight FLOAT,
        prefabname STRING,
        prefabscale FLOAT,
        resourcevalue INTEGER,
        showinmarketplace BOOLEAN DEFAULT "true",
        tile STRING
    )
'''

create_stackable_items = f'''
    CREATE TABLE IF NOT EXISTS {TN_StackableItems} (
        uniquename STRING PRIMARY KEY,
        tier INTEGER,
        foodcategory STRING,
        maxstacksize INTEGER,
        nutrition INTEGER,
        resourcetype STRING,
        shopcategory STRING,
        shopsubcategory1 STRING,
        uiatlas STRING,
        weight FLOAT,
        uisprite STRING,
        unlockedtocraft BOOLEAN,
        craftfamegainfactor FLOAT,
        enchantmentlevel INTEGER,
        descriptionlocatag STRING,
        descvariable0 STRING,
        descvariable1 STRING,
        itemvalue INTEGER,
        salvageable BOOLEAN,
        showinmarketplace BOOLEAN DEFAULT "true"
    )
'''

create_consumeable_items = f'''
    CREATE TABLE IF NOT EXISTS {TN_ConsumableItems} (
        uniquename STRING PRIMARY KEY,
        tier INTEGER,
        abilitypower INTEGER,
        consumespell STRING,
        maxstacksize INTEGER,
        shopcategory STRING,
        shopsubcategory1 STRING,
        slottype STRING,
        uiatlas STRING,
        weight FLOAT,
        uisprite STRING,
        unlockedtocraft BOOLEAN,
        unlockedtoequip BOOLEAN,
        nutrition INTEGER
    )
'''

CREATE_TABLES = {
    TN_FarmableItems: create_farmable_items,
    TN_StackableItems: create_stackable_items,
    TN_ConsumableItems: create_consumeable_items,
}
