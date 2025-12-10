use Company
drop table if exists Emploees
create table Emploees(
    EmpId int primary key identity(1,1),
    FullName nvarchar(200),
    Salary decimal(10,2)
);
drop table if exists SalaryLog
CREATE TABLE SalaryLog
(
    LogId INT IDENTITY(1,1) PRIMARY KEY,
    EmpId INT NOT NULL,
    OldSalary DECIMAL(10,2),
    NewSalary DECIMAL(10,2),
    ChangedBy NVARCHAR(128),
    ChangeDate DATETIME DEFAULT GETDATE()
);

insert into Emploees(FullName, Salary)
values 
('Иван Иванов', 5000)
