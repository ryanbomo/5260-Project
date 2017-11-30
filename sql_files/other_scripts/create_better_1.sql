 CREATE TABLE check_up_new (
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


INSERT INTO check_up_new (id,date_time,patient_id,doctor_id)
SELECT id, date_time,patient_id,doctor_id
FROM check_up
ORDER BY id;

UPDATE check_up_new
SET 
    weight = ( SELECT vitals.weight
                FROM vitals
                where vitals.appointment_id = check_up_new.id)
    ,bp_sys = ( SELECT vitals.bp_sys
                FROM vitals
                where vitals.appointment_id = check_up_new.id)
    ,bp_dia = ( SELECT vitals.bp_dia
                FROM vitals
                where vitals.appointment_id = check_up_new.id)
    ,height = ( SELECT vitals.height
                FROM vitals
                where vitals.appointment_id = check_up_new.id)
    ,pulse = ( SELECT vitals.pulse
                FROM vitals
                where vitals.appointment_id = check_up_new.id)
WHERE
    EXISTS (
        SELECT *
        FROM vitals
        where vitals.appointment_id = check_up_new.id
);




