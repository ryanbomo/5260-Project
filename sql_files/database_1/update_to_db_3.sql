-- Create vitals Table
CREATE TABLE vitals (
  appointment_id INTEGER,
  weight INTEGER,
  bp_sys INTEGER,
  bp_dia INTEGER,
  height INTEGER,
  pulse INTEGER,
  FOREIGN KEY(appointment_id) REFERENCES check_up(id)
);

-- Update values in vitals Table
INSERT INTO vitals (appointment_id, weight, bp_sys, bp_dia, height,pulse) 
    SELECT id, weight, bp_sys, bp_dia, height,pulse
    FROM check_up
    ORDER BY id;

-- Create check_up_temp Table
CREATE TABLE check_up_temp (
  id INTEGER PRIMARY KEY,
  date_time TEXT NOT NULL,
  patient_id INTEGER,
  doctor_id INTEGER,
  FOREIGN KEY(patient_id) REFERENCES patients(id),
  FOREIGN KEY(doctor_id) REFERENCES doctors(id)
);

-- Update values in check_up_tmep Table
INSERT INTO check_up_temp (id, date_time, patient_id, doctor_id) 
    SELECT id, date_time, patient_id, doctor_id
    FROM check_up
    ORDER BY id;

DROP TABLE check_up;

-- Create check_up Table
CREATE TABLE check_up (
  id INTEGER PRIMARY KEY,
  date_time TEXT NOT NULL,
  patient_id INTEGER,
  doctor_id INTEGER,
  FOREIGN KEY(patient_id) REFERENCES patients(id),
  FOREIGN KEY(doctor_id) REFERENCES doctors(id)
);

-- Update values in check_up_tmep Table
INSERT INTO check_up (id, date_time, patient_id, doctor_id) 
    SELECT id, date_time, patient_id, doctor_id
    FROM check_up_temp
    ORDER BY id;

DROP TABLE check_up_temp;