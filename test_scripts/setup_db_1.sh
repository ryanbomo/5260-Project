#!/bin/bash
cd ../
cd sql_files
cd database_1
sqlite3 db_1.db ".read create_1.sql"
sqlite3 db_1.db ".read insert_1.sql"