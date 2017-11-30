# 5260-Project
Medical Records project for CSE 5260

## Authors
 - Ryan Bomalaski
 - Stuart Hernandez

## Goal

The goal of this project is to design, implement and test a simple medical records data base for CSE 5260 - Database Systems

## Design
The design of this database was performed by Stuart Hernandez. Not yet uploaded are the ER diagram to represent the layout of Database 1.

## Data Creation
In order to make the database workable, fake medical data needed to be generated. A quick python random generator was used to create our DML files for inserting data. The data is preserved through both Database 2 and Database 3.

## Implementation
One of the unspoken design philosophies of this project was to keep the implementation simple to allow for changes to be quickly rolled out. Rather than go for a server/client model, SQLite was chosen in order to allow the project to be quickly set up.

## Testing
The queries were scripted to run 1000 times, and timing was done with the linux command line program "time" as such:
```
time ./test_script_3-1.sql
```