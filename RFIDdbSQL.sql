CREATE TABLE Store (
	StoreID int NOT NULL,
	Name varchar(255) NOT NULL,
	Address varchar(255) NOT NULL,
	PRIMARY KEY (StoreID),
);

CREATE TABLE Customer (
	CustomerID int NOT NULL,
	Name varchar(255) NOT NULL,
	PhoneNum varchar(255) NOT NULL,
	COVIDStatus varchar(255) NOT NULL,
	PRIMARY KEY (CustomerID),
);

CREATE TABLE Checkin (
	CheckinID int NOT NULL,
	StoreID int NOT NULL,
	CustomerID int NOT NULL,
	Date varchar(255) NOT NULL,
	Time varchar(255) NOT NULL,
	PRIMARY KEY (CheckinID),
	FOREIGN KEY (StoreID) REFERENCES Store(StoreID),
	FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE Dashboard (
	CheckinID int NOT NULL,
	Username int NOT NULL,
	Password int NOT NULL,
	FOREIGN KEY (CheckinID) REFERENCES Checkin(CheckinID)
);

CREATE TABLE user (
	id INTEGER NOT NULL, 
	username VARCHAR(30) NOT NULL, 
	email_address VARCHAR(50) NOT NULL, 
	password_hash VARCHAR(60) NOT NULL, 
	budget INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email_address)
);

CREATE TABLE item (
	id INTEGER NOT NULL, 
	name VARCHAR(30) NOT NULL, 
	price INTEGER NOT NULL, 
	barcode VARCHAR(12) NOT NULL, 
	description VARCHAR(200) NOT NULL, 
	owner INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	UNIQUE (barcode), 
	UNIQUE (description), 
	FOREIGN KEY(owner) REFERENCES user (id)
);

CREATE TABLE Tag (
	Tag_ID_number varchar(50) DEFAULT NULL,
	Time_recorded datetime DEFAULT NULL,
	Information varchar(20) DEFAULT NULL
);
