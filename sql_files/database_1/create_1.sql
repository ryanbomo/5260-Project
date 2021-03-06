/*
 * SQLite Examples
 * Made for CSE 5260/4020
 * Feel free to use/modify as you wish
 * Ryan Bomalaski
 */


--Create Doctors Table
CREATE TABLE doctors (
  id INTEGER PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL
);

-- Create Patients Table
CREATE TABLE patients (
  id INTEGER PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  phone INTEGER NOT NULL,
  address TEXT NOT NULL,
  city TEXT NOT NULL,
  notes TEXT
);


-- Create illnesses Table
CREATE TABLE illnesses (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  treatment TEXT NOT NULL,
  symptoms TEXT NOT NULL
);

-- Create check_up Table
CREATE TABLE check_up (
  id INTEGER PRIMARY KEY,
  date_time TEXT NOT NULL,
  patient_id INTEGER,
  doctor_id INTEGER,
  weight INTEGER,
  bp_sys INTEGER,
  bp_dia INTEGER,
  height INTEGER,
  pulse INTEGER,
  FOREIGN KEY(patient_id) REFERENCES patients(id),
  FOREIGN KEY(doctor_id) REFERENCES doctors(id)
);

-- Create specialty Table
CREATE TABLE specialty (
  id INTEGER PRIMARY KEY,
  doctor_id INTEGER,
  illness_id INTEGER,
  FOREIGN KEY(doctor_id) REFERENCES doctors(id),
  FOREIGN KEY(illness_id) REFERENCES illnesses(id)
);

-- Create infected Table
CREATE TABLE infected (
  id INTEGER PRIMARY KEY,
  patient_id INTEGER,
  illness_id INTEGER,
  FOREIGN KEY(patient_id) REFERENCES patients(id),
  FOREIGN KEY(illness_id) REFERENCES illnesses(id)
);