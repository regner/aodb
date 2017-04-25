

TN_FarmableItems = 'FarmableItems'

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

CREATE_TABLES = {
    TN_FarmableItems: create_farmable_items,
}
