-- 🏥 Hospital Billing Database Project
-- Complete SQL Script (Single File)

-- Step 1: Create Database
CREATE DATABASE HospitalBillingDB;
USE HospitalBillingDB;

-- Step 2: Create Patients Table
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,
    PatientName VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    ContactNumber VARCHAR(15),
    Address VARCHAR(200)
);

-- Step 3: Create Services Table
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,
    ServiceName VARCHAR(100),
    ServiceCost DECIMAL(10,2)
);

-- Step 4: Create Bills Table
CREATE TABLE Bills (
    BillID INT PRIMARY KEY AUTO_INCREMENT,
    PatientID INT,
    ServiceID INT,
    Quantity INT,
    DateOfService DATE,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Step 5: Insert Sample Data into Patients Table
INSERT INTO Patients (PatientName, Age, Gender, ContactNumber, Address)
VALUES
('John Doe', 45, 'Male', '9876543210', 'Hyderabad'),
('Priya Sharma', 32, 'Female', '9123456780', 'Mumbai'),
('Rahul Verma', 28, 'Male', '9988776655', 'Delhi');

-- Step 6: Insert Sample Data into Services Table
INSERT INTO Services (ServiceName, ServiceCost)
VALUES
('General Checkup', 500.00),
('Blood Test', 800.00),
('X-Ray', 1200.00),
('MRI Scan', 5000.00),
('Surgery', 15000.00);

-- Step 7: Insert Sample Data into Bills Table
INSERT INTO Bills (PatientID, ServiceID, Quantity, DateOfService)
VALUES
(1, 1, 1, '2025-11-01'),
(1, 2, 1, '2025-11-01'),
(2, 3, 2, '2025-11-02'),
(3, 4, 1, '2025-11-05'),
(3, 5, 1, '2025-11-06');

-- Step 8: Query - Calculate Total Bill for Each Patient
SELECT 
    P.PatientID,
    P.PatientName,
    SUM(S.ServiceCost * B.Quantity) AS TotalBill
FROM 
    Patients P
JOIN 
    Bills B ON P.PatientID = B.PatientID
JOIN 
    Services S ON B.ServiceID = S.ServiceID
GROUP BY 
    P.PatientID, P.PatientName;

-- ✅ Sample Output:
-- | PatientID | PatientName  | TotalBill |
-- |------------|---------------|-----------|
-- | 1          | John Doe      | 1300.00   |
-- | 2          | Priya Sharma  | 2400.00   |
-- | 3          | Rahul Verma   | 20000.00  |

-- Optional Enhancements:
-- ALTER TABLE Bills ADD COLUMN PaymentStatus VARCHAR(20) DEFAULT 'Pending';
-- ALTER TABLE Bills ADD COLUMN BillDate DATE;
-- CREATE VIEW PatientBillSummary AS
-- SELECT P.PatientName, SUM(S.ServiceCost * B.Quantity) AS TotalBill
-- FROM Patients P
-- JOIN Bills B ON P.PatientID = B.PatientID
-- JOIN Services S ON B.ServiceID = S.ServiceID
-- GROUP BY P.PatientName;
