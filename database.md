# DBMS : MySQL Server 8.0

# Tables Used In Project JobPortal
1. Users
2. Contacts
3. Jobs

# MySQL Command To Create Table User

Create table Users(
    userid int not null primary key auto_increment,
    username varchar(50) unique not null,
    name varchar(50) not null,
    email varchar(50) not null,
    contact char(10) not null,
    address varchar(150),
    password varchar(20),
    agree varchar(5) #agree for t&c
    is_applied boolean;
    jobid int;
);

Alter table Users add auto_increment=1000;

# MySQL Command To Create Table Contacts

Create table Contacts(
    cid int not null primary key auto_increment,
    name varchar(50) not null,
    email varchar(50) not null,
    subject varchar(50) not null,
    messsage varchar(300) not null,
    date datetime not null
);

Alter table contacts add auto_increment=100;

# MySQL Command To Create Table Jobs

Create table Jobs(
    jobid int not null primary key auto_increment,
    userid int,
    category varchar(100) not null,
    jobtitle varchar(50)  not null,
    company varchar(50) not null,
    recruiter varchar(50) not null,
    email varchar(50) not null,
    contact char(10) not null,
    address varchar(150),
    password varchar(20),
    agree varchar(5),
    about varchar(200) not null,
    desc1 varchar(500) not null,
    desc2 varchar(500),
    desc3 varchar(500),
    salary int
)auto_increment=1001;


# Inserting Values Into Jobs Table

insert into jobs(category, jobtitle, company, recruiter, email, contact, about, desc1, salary) 
values('CS & IT', 'Python Developer', 'Pythonista', 'Kaushal Kumar Roy', 'abc123@gmail.com', '9876543210', 'Lorem ipsum dolor emet', 'Good reputed company', 100000);

insert into jobs(category, jobtitle, company, recruiter, email, contact, about, desc1, salary) 
values('ECE', 'Network Engineer', 'SmartCommunication Pvt. Ltd.', 'Ritaka Roy', 'abcd456@gmail.com', '9876543111', 'Lorem ipsum dolor emet', 'Lead in telecommuncation', 1000000);
