
import mysql.connector as connector

config = {
    "user":"root",
    "password": "Ly123456789",
    "database": "db_project",
    "host":'localhost',
    "auth_plugin":'mysql_native_password',
    "raise_on_warnings": True
}

cnx = connector.connect(**config)
