use Company;
go
update Emploees
set Salary = 65000
where FullName = 'Иван Иванов';
select * from SalaryLog;