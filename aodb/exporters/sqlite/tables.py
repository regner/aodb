

TN_FarmableItems = 'FarmableItems'

create_farmable_items = f'''
    CREATE TABLE IF NOT EXISTS {TN_FarmableItems} (
        uniquename STRING PRIMARY KEY,
        tier INTEGER
    )
'''

CREATE_TABLES = {
    TN_FarmableItems: create_farmable_items,
}
