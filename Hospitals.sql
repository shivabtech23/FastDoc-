CREATE DATABASE HOSPITALS;
use HOSPITALS;
CREATE TABLE hospitals (
    hospital_id INT PRIMARY KEY AUTO_INCREMENT,
    hospital_name VARCHAR(255),
    location VARCHAR(255)
);
CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    doctor_name VARCHAR(255),
    years_of_experience INT,
    speciality VARCHAR(255),
    rating DECIMAL(2, 1),
    education VARCHAR(255),
    hospital_name VARCHAR(255),
    hospital_id INT,
    FOREIGN KEY (hospital_id) REFERENCES hospitals(hospital_id)
);
INSERT INTO hospitals (hospital_name, location) VALUES
('Sri Ramakrishna Hospital', 'Bangalore'),
('Narayana Health', 'Bangalore'),
('Fortis Hosiptal','Bangalore'),
('Apollo Hosiptal','Banaglore');

INSERT INTO doctors (doctor_name, years_of_experience, speciality, rating, education, hospital_name, hospital_id) VALUES
('Dr. Rajesh Sharma', 15, 'Cardiology', 4.8, 'MBBS, MD', 'Sri Ramakrishna Hospital', 1),
('Dr. Meena Iyer', 10, 'Neurology', 4.6, 'MBBS, DM', 'Sri Ramakrishna Hospital', 1),
('Dr. Aarav Patel', 8, 'Orthopedics', 4.4, 'MBBS, MS', 'Sri Ramakrishna Hospital', 1),
('Dr. Sneha Desai', 12, 'Dermatology', 4.7, 'MBBS, MD', 'Sri Ramakrishna Hospital', 1),
('Dr. Vikram Singh', 20, 'Pediatrics', 4.9, 'MBBS, DCH', 'Sri Ramakrishna Hospital', 1),
('Dr. Anjali Kapoor', 7, 'Ophthalmology', 4.3, 'MBBS, MS', 'Sri Ramakrishna Hospital', 1),
('Dr. Siddharth Jain', 18, 'Urology', 4.8, 'MBBS, MCh', 'Sri Ramakrishna Hospital', 1),
('Dr. Neha Verma', 9, 'Gynecology', 4.5, 'MBBS, MD', 'Sri Ramakrishna Hospital', 1),
('Dr. Karan Gupta', 14, 'General Surgery', 4.7, 'MBBS, MS', 'Sri Ramakrishna Hospital', 1),
('Dr. Priya Nair', 6, 'ENT', 4.2, 'MBBS, MS', 'Sri Ramakrishna Hospital', 1);

INSERT INTO doctors (doctor_name, years_of_experience, speciality, rating, education, hospital_name, hospital_id) VALUES
('Dr. Ashok Khanna', 11, 'Cardiology', 4.6, 'MBBS, MD', 'Narayana Health', 2),
('Dr. Manisha Rao', 13, 'Neurology', 4.7, 'MBBS, DM', 'Narayana Health', 2),
('Dr. Shubham Mishra', 9, 'Orthopedics', 4.5, 'MBBS, MS', 'Narayana Health', 2),
('Dr. Pallavi Kulkarni', 17, 'Dermatology', 4.8, 'MBBS, MD', 'Narayana Health', 2),
('Dr. Harish Malhotra', 25, 'Pediatrics', 5.0, 'MBBS, DCH', 'Narayana Health', 2),
('Dr. Reema Singh', 6, 'Ophthalmology', 4.4, 'MBBS, MS', 'Narayana Health', 2),
('Dr. Mohit Rana', 19, 'Urology', 4.8, 'MBBS, MCh', 'Narayana Health', 2),
('Dr. Kavita Pandey', 8, 'Gynecology', 4.6, 'MBBS, MD', 'Narayana Health', 2),
('Dr. Piyush Agarwal', 16, 'General Surgery', 4.7, 'MBBS, MS', 'Narayana Health', 2),
('Dr. Vandana Joshi', 5, 'ENT', 4.3, 'MBBS, MS', 'Narayana Health', 2);


INSERT INTO Doctors (doctor_name, years_of_experience, speciality, rating, education, hospital_name,hospital_id)
VALUES
('Dr. Ravi Nair', 12, 'Cardiology',4.8,'MBBS', 'Fortis Hospital',3),
('Dr. Meera Iyer', 9, 'Neurology',4.7,'MBBS,MD', 'Fortis Hospital',3),
('Dr. Sunil Singh', 15, 'Orthopedics',4.2,'MBBS,MD', 'Fortis Hospital',3),
('Dr. Kavita Joshi', 10, 'Pediatrics',4.9,'MBBS,BDS', 'Fortis Hospital',3),
('Dr. Vikram Desai', 7, 'Dermatology',4.8,'MBBS','Fortis Hospital',3),
('Dr. Neha Gupta', 8, 'Gastroenterology',4.3,'MBBS', 'Fortis Hospital',3),
('Dr. Pankaj Sethi', 11, 'Oncology',4.1,'MBBS', 'Fortis Hospital',3),
('Dr. Aarti Malhotra', 14, 'Radiology',3.9,'MBBS,BAMS', 'Fortis Hospital',3),
('Dr. Sanjay Mehta', 6, 'Psychiatry',4.2,'MBBS,MD', 'Fortis Hospital',3),
('Dr. Vishal Kumar', 13, 'Endocrinology',5,'MBBS', 'Fortis Hospital',3);

INSERT INTO Doctors (doctor_name, years_of_experience, speciality, rating , education ,hospital_name ,hospital_id)
VALUES
('Dr. Anjali Reddy', 10, 'Cardiology',4.9,'MBBS,MS','Apollo Hospitals',4),
('Dr. Rohit Agarwal', 8, 'Neurology',4.8,'MBBS','Apollo Hospitals',4),
('Dr. Preeti Mishra', 14, 'Orthopedics',4.6,'MBBS,BAMS','Apollo Hospitals',4),
('Dr. Manish Kapoor', 12, 'Pediatrics',4.3,'MBBS','Apollo Hospitals',4),
('Dr. Shweta Menon', 7, 'Dermatology',4.4,'MBBS,MS','Apollo Hospitals',4),
('Dr. Kiran Raj', 6, 'Gastroenterology',4.5,'MBBS,MD','Apollo Hospitals',4),
('Dr. Snehal Sharma', 13, 'Oncology',4.1,'MBBS,BAMS','Apollo Hospitals',4),
('Dr. Arvind Gupta', 9, 'Radiology',4.5,'MBBS','Apollo Hospitals',4),
('Dr. Rakesh Jain', 15, 'Psychiatry',4.7,'MBBS,MS','Apollo Hospitals',4),
('Dr. Lakshmi Pillai', 11, 'Endocrinology',4.2,'MBBS,MD','Apollo Hospitals',4);

select * from doctors;