/* Query Two */

SELECT
    doctors.first_name, doctors.last_name
FROM
    doctors
    INNER JOIN
        specialty
ON
    specialty.doctor_id = doctors.id
    INNER JOIN
        infected
ON
    infected.illness_id = specialty.illness_id
    INNER JOIN
        patients
ON
    patients.id = infected.patient_id
WHERE
    patients.first_name = 'SAMANTHA';