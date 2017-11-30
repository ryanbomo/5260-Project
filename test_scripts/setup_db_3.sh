#!/bin/bash
cd ../
cd sql_files
cd database_1
sqlite3 ~/School/fall_2017/cse_5260/project/sql_files/database_3/db_3.db ".read create_1.sql"
sqlite3 ~/School/fall_2017/cse_5260/project/sql_files/database_3/db_3.db ".read insert_1.sql"
sqlite3 ~/School/fall_2017/cse_5260/project/sql_files/database_3/db_3.db ".read update_to_db_3.sql"
