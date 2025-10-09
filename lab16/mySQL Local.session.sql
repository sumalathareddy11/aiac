CREATE DATABASE company;
USE company;
CREATE TABLE employee(
    id INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) ,
    last_name VARCHAR(100) ,
    department VARCHAR(100) ,
    salary DECIMAL(10, 2) ,
    hire_date DATE 
);

CREATE  TABLE IF EXISTS dept;


INSERT INTO employee(first_name, last_name, department, salary, hire_date) VALUES
('Amit','Sharma','HR',45000,'2020-05-20'),
('Priya','Patel','Finance',60000,'2021-02-10'),
('Ravi','Kumar','IT',55000,'2019-08-14'),
('Neha','Reddy','Marketing',48000,'2022-01-05'),
('Arjun','Singh','IT',62000,'2020-09-12');

CREATE TABLE dept (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100),
    location VARCHAR(100)
);

INSERT INTO dept (dept_name, location) VALUES
('HR', 'Hyderabad'),
('Finance', 'Mumbai'),
('IT', 'Bangalore'),
('Marketing', 'Chennai'),
('Operations', 'Delhi');
SELECT * FROM dept;
SELECT * FROM employee;

SELECT first_name,last_name, department FROM employee;

SELECT DISTINCT department FROM employee;

SELECT * 
FROM employee
WHERE salary > 50000;

SELECT * FROM employee WHERE department = 'IT';


SELECT * 
FROM employee
WHERE hire_date > '2020-12-31';


SELECT * 
FROM employee
ORDER BY salary ASC;


SELECT * 
FROM employee
ORDER BY salary DESC
LIMIT 3;

SELECT COUNT(*) AS total_employees 
FROM employee;

SELECT AVG(salary) AS average_salary 
FROM employee;


SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary 
FROM employee;

SELECT department, SUM(salary) AS total_salary 
FROM employee
GROUP BY department;


SELECT department, COUNT(*) AS employee_count
FROM employee
GROUP BY department
HAVING COUNT(*) > 1;

SELECT department, AVG(salary) AS avg_salary
FROM employee
GROUP BY department;

SELECT YEAR(hire_date) AS year, COUNT(*) AS total_hired
FROM employee
GROUP BY YEAR(hire_date);


SELECT e.first_name, e.last_name, e.department, d.location
FROM employee e
JOIN dept d ON e.department = d.dept_name;

SELECT e.first_name, e.last_name, e.department
FROM employee e
JOIN dept d ON e.department = d.dept_name
WHERE d.location = 'Bangalore';

SELECT e.first_name, e.last_name, e.department, d.location
FROM employee e
LEFT JOIN dept d ON e.department = d.dept_name;

SELECT d.dept_name, d.location
FROM dept d
LEFT JOIN employee e ON d.dept_name = e.department
WHERE e.id IS NULL;

SELECT department, COUNT(*) AS emp_count
FROM employee
GROUP BY department;

SELECT * 
FROM employee
WHERE salary > (SELECT AVG(salary) FROM employee);

SELECT department, AVG(salary) AS avg_salary
FROM employee
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1;

SELECT * 
FROM employee
ORDER BY hire_date DESC
LIMIT 1;

SELECT * 
FROM employee
WHERE salary = (
    SELECT DISTINCT salary
    FROM employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
);

SELECT * 
FROM employee
WHERE department = (
    SELECT department
    FROM employee
    WHERE first_name = 'Amit' AND last_name = 'Sharma'
);


UPDATE employee
SET salary = salary * 1.10
WHERE department = 'IT';


UPDATE employee
SET department = 'Marketing'
WHERE first_name = 'Ravi';

DELETE FROM employee
WHERE salary < 40000;

ALTER TABLE employee
ADD email VARCHAR(150);

UPDATE employee
SET email = CONCAT(LOWER(first_name), '.', LOWER(last_name), '@company.com');

SELECT department, AVG(salary) AS avg_salary
FROM employee
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 2;

SELECT d.location, COUNT(e.id) AS emp_count
FROM dept d
LEFT JOIN employee e ON d.dept_name = e.department
GROUP BY d.location;


SELECT COUNT(*) AS total_employees, SUM(salary) AS total_salary
FROM employee;

SELECT * 
FROM employee
WHERE first_name LIKE 'A%';


SELECT * 
FROM employee
WHERE last_name LIKE '%a';


SELECT * 
FROM employee
WHERE YEAR(hire_date) = 2020;

SELECT first_name, last_name, DATEDIFF(CURDATE(), hire_date) AS days_since_hired
FROM employee;

SELECT UPPER(first_name) AS first_name, UPPER(last_name) AS last_name
FROM employee;

SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employee;

SELECT * 
FROM employee
WHERE salary BETWEEN 45000 AND 60000;

CREATE VIEW high_salary_employees AS
SELECT * 
FROM employee
WHERE salary > 55000;

SELECT * FROM high_salary_employees;

ALTER TABLE employee
MODIFY department VARCHAR(100) NOT NULL;

DROP VIEW high_salary_employees;

RENAME TABLE employee TO staff;

SELECT * FROM staff;

CREATE TABLE employee_backup AS
SELECT * FROM staff;

SELECT * FROM employee_backup;

TRUNCATE TABLE staff;

SELECT * FROM staff;

DROP TABLE employee_backup;

CREATE INDEX idx_lastname ON staff(last_name);

SELECT * FROM staff WHERE last_name = 'Kumar';

DROP INDEX idx_lastname ON staff;