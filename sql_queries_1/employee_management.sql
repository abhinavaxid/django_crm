CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE salaries (
    employee_id INT,
    salary DECIMAL(10, 2),
    from_date DATE,
    to_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    PRIMARY KEY (employee_id, from_date), 
    CONSTRAINT chk_dates CHECK (from_date <= to_date) 
);

INSERT INTO departments (department_id, department_name) VALUES
(1, 'Engineering'),
(2, 'Sales'),
(3, 'Marketing'),
(4, 'Human Resources'),
(5, 'Finance');

INSERT INTO employees (employee_id, first_name, last_name, department_id, hire_date) VALUES
(1, 'John', 'Doe', 1, '2020-05-15'),
(2, 'Jane', 'Smith', 2, '2019-09-20'),
(3, 'Michael', 'Johnson', 1, '2021-03-10'),
(4, 'Emily', 'Davis', 3, '2018-11-05'),
(5, 'David', 'Brown', 4, '2022-01-25'),
(6, 'Sarah', 'Wilson', 2, '2023-02-12'),
(7, 'James', 'Lee', 3, '2022-08-30'),
(8, 'Anna', 'Clark', 1, '2023-01-10'),
(9, 'Daniel', 'Martinez', 4, '2022-11-18'),
(10, 'Sophia', 'Lopez', 5, '2023-04-25'),
(11, 'Emma', 'Wilson', 1, '2023-07-01'),   
(12, 'Oliver', 'Garcia', 2, '2023-10-15'),  
(13, 'Sophie', 'Rodriguez', 3, '2023-11-30'),
(14, 'Lucas', 'Gomez', 4, '2024-04-01');    


INSERT INTO salaries (employee_id, salary, from_date, to_date) VALUES
(6, 68000.00, '2023-02-12', '2024-02-11'),
(7, 76000.00, '2022-08-30', '2023-08-29'),
(8, 82000.00, '2023-01-10', '2024-01-09'),
(9, 70000.00, '2022-11-18', '2023-11-17'),
(10, 75000.00, '2023-04-25', '2024-04-24');

--SQL query
--1
SELECT *
FROM employees
WHERE hire_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 YEAR);
--2
SELECT d.department_name, SUM(s.salary) AS total_salary_expenditure
FROM departments d
JOIN employees e ON d.department_id = e.department_id
JOIN salaries s ON e.employee_id = s.employee_id
GROUP BY d.department_name;
--3
SELECT e.first_name, e.last_name, d.department_name, s.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN salaries s ON e.employee_id = s.employee_id
ORDER BY s.salary DESC
LIMIT 5;
