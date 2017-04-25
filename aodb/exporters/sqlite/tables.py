

TN_FarmableItems = 'FarmableItems'

create_farmable_items = f'''
    CREATE TABLE IF NOT EXISTS {TN_FarmableItems} (
        uniqueName STRING PRIMARY KEY,
        tier INTEGER,
        activeFarmActionDurationSeconds INTEGER,
        activeFarmBonus FLOAT,
        activeFarmCycleLengthSeconds INTEGER,
        activeFarmFocusCost INTEGER,
        activeFarmMaxCycles INTEGER,
        animationId STRING,
        destroyable BOOLEAN,
        kind STRING,
        maxStackSize INTEGER,
        pickupable BOOLEAN,
        placeCost INTEGER,
        placeFame INTEGER,
        shopCategory STRING,
        shopSubCategory STRING,
        uiAtlas STRING,
        unloackedToCraft BOOLEAN,
        unlockedToPlace BOOLEAN,
        weight FLOAT
    )
'''

CREATE_TABLES = {
    TN_FarmableItems: create_farmable_items,
}
