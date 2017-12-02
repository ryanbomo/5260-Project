#!/bin/bash
cd ../
cd sql_files
cd database_1
sqlite3 ~/git/5260-Project/sql_files/database_2/db_2.db ".read create_1.sql"
sqlite3 ~/git/5260-Project/sql_files/database_2/db_2.db ".read insert_1.sql"
sqlite3 ~/git/5260-Project/sql_files/database_2/db_2.db ".read update_to_db_2.sql"
