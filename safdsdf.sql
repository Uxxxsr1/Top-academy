use UniversityDB;
go

-- select * from Groups;
-- select * from Marks;
-- select * from Subjects;
-- select * from TEachers;
-- select * from Students;

select s.FullName, g.GroupId
from Students s
join Groups g on s.GroupId = g.GroupId

SELECT s.FullName, sub.SubjectName, m.Mark
FROM Marks m
JOIN Students s ON s.StudentId = m.StudentId
JOIN Subjects sub ON m.SubjectId = sub.SubjectId;

select s.Fullname, avg(m.Mark) as [средняя оценка]
from Students s
join Marks m on s.StudentId = m.StudentId
group by s.FullName

select t.FullName as [Учителя], sub.SubjectName as [предмет]
from TEachers t
join Subjects sub on sub.TeacherId = t.TeacherId

select distinct s.FullName
from Students s
join Marks m on s.StudentId = m.StudentId
where m.Mark = 5

SELECT s.FullName,
    s.BirthDate,
    DATEDIFF(YEAR, s.BirthDate, GETDATE()) AS Age
FROM Students s
WHERE DATEDIFF(YEAR, s.BirthDate, GETDATE()) > 20
ORDER BY Age DESC, s.FullName;

SELECT t.Fullname
FROM TEachers t
WHERE DATEDIFF(YEAR, t.HireDate, GETDATE()) > 5
ORDER BY t.Fullname;

SELECT s.FullName AS [Имя студента],
g.GroupName AS [Название группы],
g.YearStart AS [Год начала группы]
FROM Students s
JOIN Groups g ON s.GroupId = g.GroupId
ORDER BY s.FullName;

SELECT s.FullName, AVG(m.Mark) AS AverageMark
FROM Students s
JOIN Marks m ON s.StudentId = m.StudentId
GROUP BY s.FullName
HAVING AVG(m.Mark) > 4;

