-- SELECT the details of Doctor(s) who has got Admissions.
SELECT DISTINCT d.doctor_id, d.first_name, d.last_name, d.specialty
FROM Doctors d
JOIN Admissions a ON d.doctor_id = a.attending_doctor_id;


-- SELECT the details of Doctor(s) for whom there is no Admissions.
SELECT d.doctor_id, d.first_name, d.last_name, d.specialty
FROM Doctors d
LEFT JOIN Admissions a ON d.doctor_id = a.attending_doctor_id
WHERE a.attending_doctor_id IS NULL;


-- SELECT the details of Patient(s) whose Admission can’t be completed due to missing doctor details
SELECT p.patient_id, p.first_name, p.last_name, p.gender, p.birth_date, p.city, p.province_id, p.allergies, p.height, p.weight
FROM Patients p
LEFT JOIN Admissions a ON p.patient_id = a.patient_id
WHERE a.attending_doctor_id IS NULL;