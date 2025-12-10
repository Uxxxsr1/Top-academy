USE Company;
GO

-- DROP TRIGGER IF EXISTS trg_LogSalaryChatnges;
-- GO

CREATE TRIGGER trg_LogSalaryChanges
ON Emploees
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    IF UPDATE(Salary)
    BEGIN
        INSERT INTO SalaryLog
            (EmpId, OldSalary, NewSalary, ChangedBy)
        SELECT
            i.EmpId,
            d.Salary AS OldSalary,
            i.Salary AS NewSalary,
            SYSTEM_USER AS ChangedBy
        FROM inserted i
            JOIN deleted d ON i.EmpId = d.EmpId
        WHERE i.Salary <> d.Salary
    END
END;
GO