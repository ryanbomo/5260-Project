SELECT 
    patients.first_name, patients.last_name
FROM
    patients
    INNER JOIN
        check_up
ON
    check_up.patient_id = patients.id
    INNER JOIN
        vitals
ON
    vitals.appointment_id = check_up.id
    INNER JOIN
        doctors
ON
    doctors.id = check_up.doctor_id
    INNER JOIN
        infected
ON
    patients.id =  infected.patient_id
    INNER JOIN
        illnesses
ON
    infected.illness_id = illnesses.id
WHERE
    doctors.last_name = "HARMON" AND illnesses.name = "MALARIA" AND (vitals.weight*.45) / ((vitals.height*.025) * (vitals.height*.025)) > 25;