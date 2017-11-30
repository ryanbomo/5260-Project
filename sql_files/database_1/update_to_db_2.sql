UPDATE illnesses
SET symptoms = 1
WHERE symptoms = 'SKIN IRRITATION';
UPDATE illnesses
SET symptoms = 2
WHERE symptoms = 'COUGHING';
UPDATE illnesses
SET symptoms = 3
WHERE symptoms = 'EXHAUSTION';
UPDATE illnesses
SET symptoms = 4
WHERE symptoms = 'UNRESPONSIVE';


--Set Symptoms from TEXT to INT on illnesses
BEGIN TRANSACTION;

ALTER TABLE illnesses RENAME TO temp_illnesses;

CREATE TABLE illnesses (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  treatment TEXT NOT NULL,
  symptom_id INT NOT NULL,
  FOREIGN KEY(symptom_id) REFERENCES symptoms(id)
);

INSERT INTO illnesses
SELECT
 id,name,treatment,symptoms
FROM
 temp_illnesses;
  
DROP TABLE temp_illnesses;

--Create symptoms Tables
Create Table symptoms (
  id INTEGER PRIMARY KEY,
  symptoms TEXT NOT NULL
);

/*
symptoms            int id
                    text symptoms
*/
INSERT INTO symptoms VALUES(1,'SKIN IRRITATION');
INSERT INTO symptoms VALUES(2,'COUGHING');
INSERT INTO symptoms VALUES(3,'EXHAUSTION');
INSERT INTO symptoms VALUES(4,'UNRESPONSIVE');