# -*- coding: utf-8 -*-
import io
from contextlib import closing
import mysql.connector as connector

config = {
        "user":"root",
        "password":"",
        "database":"cn_dbpedia",
        'raise_on_warnings':True
}

# initialization
"""
query = "SELECT name FROM city WHERE population <= 1000"

with closing(connector.connect(**config)) as cnx:
    with closing(cnx.cursor()) as cur:
        cur.execute(query)
        with closing(io.StringIO()) as output:
            for (name,) in cur:
                print(name, file=output)
            print(output.getvalue(), end='')

"""
DB_NAME = "cn_dbpedia"
TABLES = {}
TABLES["triples"] = (
"""
        CREATE TABLE triples (
                id int NOT NULL AUTO_INCREMENT,
                entity1 varchar(100),
                relation varchar(100),
                entity2 varchar(2000),
                PRIMARY KEY(id)
        )
"""
        )

def create_database():
        with closing(connector.connect(**config)) as cnx:
                with closing(cnx.cursor()) as cur:
                        try:
                                cur.execute(
                                        "CREATE DATABASE {} DEFAULT CHARACTER SET UTF8MB4".format(DB_NAME))
                        except connector.Error as err:
                                print("Failed creating database: {}".format(err))
                                exit(1)
                        try:
                                cur.execute("USE {}".format(DB_NAME))
                        except connector.Error as err:
                                print("Database {} does not exists.".format(DB_NAME))
                        for table_name in TABLES:
                                table_desc = TABLES[table_name]
                                cur.execute(table_desc)
                                

def update():
        query = ("""
                INSERT INTO triples (entity1, relation, entity2) VALUES(%s,%s,%s)
                        """)
        with closing(connector.connect(**config)) as cnx:
                with closing(cnx.cursor()) as cur:
                        with open(".\\dataset\\baike_triples.txt", "r", encoding="utf-8") as f:
                                for ind, (e1, r, e2) in enumerate(map(lambda line: line.split("\t"), f)):
                                        if len(e2) >= 2000 or len(e1) >= 100 or len(r) >= 100:
                                                print(e1, r, e2)
                                                continue
                                        cur.execute(query, (e1, r, e2))
                                        if ind % 1000 == 0:
                                                    cnx.commit()


#create_database()
update()
