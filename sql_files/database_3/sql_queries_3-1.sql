/*
 * SQLITE Queries for project
 * Made for CSE5260/4020
 * Ryan Bomalaski and Stuart Hernandez
 */

/* Query One*/

SELECT 
    patients.first_name AS patient_first_name, patients.last_name AS patient_last_name, doctors.first_name AS doctor_first_name, doctors.last_name AS doctor_last_name, illnesses.name, vitals.bp_sys, vitals.bp_dia
FROM
    patients 
    INNER JOIN 
        check_up 
ON 
        patients.id = check_up.patient_id
    INNER JOIN
        doctors
ON
        doctors.id = check_up.doctor_id
    INNER JOIN
        vitals
ON
        check_up.id = vitals.appointment_id
    INNER JOIN
        infected
on
        infected.patient_id = patients.id
    INNER JOIN
        illnesses
on
        infected.illness_id = illnesses.id
WHERE
    check_up.date_time = '09/30/2008 09:00 AM';



