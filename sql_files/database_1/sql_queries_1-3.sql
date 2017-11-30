SELECT
    patients.first_name, patients.last_name
FROM
    patients
    INNER JOIN
        check_up
ON
    check_up.patient_id = patients.id 
    INNER JOIN
        infected
ON
    patients.id = infected.patient_id
    INNER JOIN
        illnesses
ON
    infected.illness_id = illnesses.id
    INNER JOIN
        doctors
ON
    check_up.doctor_id = doctors.id
WHERE
    doctors.last_name = "HARMON" AND illnesses.name = "MALARIA" and (check_up.weight*.45) / ((check_up.height*.025) * (check_up.height*.025)) > 25;