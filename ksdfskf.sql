use UniversityDB;
go

insert into Groups(GroupName, YearStart)
values
('ИС-101', 2023),
('ИС-102', 2022),
('ИС-103', 2021);

insert into TEachers(Fullname, HireDate)
values
('ыжвадлывджалжыд', '2001-12-22'),
('ыжвадлывджалжы', '2001-11-13'),
('ыжвадлывджалж', '2004-12-15');

insert into Subjects(SubjectName, TeacherId)
values
('Теория баз данных', 1),
('Веб-разработка на JS', 2),
('Профильная математика', 3);

insert into Students(FullName, BirthDate, GroupId)
values
('ыжвдалждывал', '1997-12-31', 1),
('ыжвдалждыал', '1998-10-28', 1),
('ыжвдалжд', '1999-10-23', 3);

insert into Marks(StudentId, Mark, SubjectId)
values
(1, 5, 1),
(1, 4, 2),
(1, 3, 3);