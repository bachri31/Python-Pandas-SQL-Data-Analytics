#! /opt/homebrew/bin/python3

# author : Laroussi Bachri



import sqlite3




if __name__ == '__main__':   

    con = sqlite3.connect('./main.db')
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS ventes (
    orderID             INTEGER      NOT NULL,
    orderlinenumber     INTEGER      NOT NULL,                   
    quantity            INTEGER      NOT NULL CHECK (quantity >= 0),
    price               REAL         NOT NULL CHECK (price >= 0),
    sales               REAL         NOT NULL CHECK (sales >= 0),
    date                TEXT         NOT NULL,                   
    status              TEXT         NOT NULL,                   
    QTR_ID              INTEGER      CHECK (QTR_ID BETWEEN 1 AND 4),
    month               INTEGER      CHECK (month BETWEEN 1 AND 12),
    year                INTEGER      CHECK (year BETWEEN 1900 AND 2100),

    product_category    TEXT,                                    
    prix_ref            REAL         CHECK (prix_ref >= 0),      
    ref_prod            TEXT,                                    
    company_name        TEXT,
    phone               TEXT,
    adress              TEXT,                                    
    adress_comp         TEXT,                                    
    city                TEXT,
    state               TEXT,
    zipcode             TEXT,
    country             TEXT,
    territory           TEXT,                                    
    contact_last_name   TEXT,
    contact_first_name  TEXT,
    taille              TEXT CHECK (taille IN ('Small','Medium','Large')),

    
    PRIMARY KEY (orderID, orderlinenumber)
    );
    """)

    con.commit()

    # Vérifie la structure de 'ventes'
    cur.execute("PRAGMA table_info(ventes);")
    for col in cur.fetchall():
        print(col)
    con.close()



