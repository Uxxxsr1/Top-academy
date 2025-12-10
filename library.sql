

-- CREATE DATABASE UniversityDB;
-- go
USE UniversityDB;
GO
CREATE TABLE Groups
(
    GroupId int IDENTITY(1,1) PRIMARY KEY,
    GroupName NVARCHAR(200) NOT NULL,
    YearStart int NOT NULL
);
GO
CREATE TABLE Students
(
    StudentId int IDENTITY(1,1) PRIMARY KEY,
    FullName nvarchar(100) NOT NULL,
    BirthDate date NOT NULL,
    GroupId int NOT NULL,
    FOREIGN KEY (GroupId) REFERENCES Groups(GroupId)
);
GO

create table TEachers(
    TeacherId int identity(1,1) primary key,
    Fullname nvarchar(200) not null,
    HireDate date not null
);
go
 
create table Subjects(
    SubjectId int identity(1,1) primary key,
    SubjectName nvarchar(200) not null,
    TeacherId int not null,
    foreign key (TeacherId) references TEachers(TeacherId)
);
go

create table Marks(
    MarkId int identity(1,1) primary key,
    StudentId int not null,
    Mark int not null check(Mark between 1 and 5),
    SubjectId int not null,
    FOREIGN KEY (StudentId) references Students(StudentId),
    foreign key (SubjectId) references Subjects(SubjectId)
)