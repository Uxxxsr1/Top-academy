DROP DATABASE School;
CREATE DATABASE School;
GO

USE School;
GO


CREATE TABLE Students
(
    Id INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(50) NOT NULL
);
GO

CREATE TABLE Grades
(
    Id INT PRIMARY KEY IDENTITY(1,1),
    StudentId INT NOT NULL,
    Subject NVARCHAR(50) NOT NULL,
    Grade INT NOT NULL,

    FOREIGN KEY (StudentId) REFERENCES Students(Id)
);
GO

INSERT INTO Students
    (Name)
VALUES
    ('Иван'),
    ('Мария'),
    ('Петр');
GO

INSERT INTO Grades
    (StudentId, Subject, Grade)
VALUES
    (1, 'Математика', 5),
    (1, 'Физика', 4),
    (2, 'Математика', 3),
    (2, 'Физика', 5),
    (3, 'Математика', 4);
GO

SELECT
    s.Name AS Студент,
    g.Subject AS Предмет,
    g.Grade AS Оценка
FROM Students s
    JOIN Grades g ON s.Id = g.StudentId;
GO