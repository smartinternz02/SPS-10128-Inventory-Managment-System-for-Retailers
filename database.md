# DBMS : MySQL Server 8.0

# Tables Used In Project JobPortal
1. Users
2. Contacts
3. IMS

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

Create table Inventory(
    inventoryid int not null primary key auto_increment,
    username varchar(30) not null,
    name varchar(100) not null,
    description varchar(50)  not null,
    unitprice int not null,
    qtystock int not null,
    totalvalue int not null,
)auto_increment=1001;


# Inserting Values Into Jobs Table

insert into inventory( inventoryid, username, name, description,unitprice, qtystock, totalvalue) 
values(101, 'newuser', 'Juicer', 'description', 10, 10, 100);

