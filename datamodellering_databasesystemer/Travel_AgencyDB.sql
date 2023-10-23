CREATE DATABASE IF NOT EXISTS Travel_AgencyDB;
use Travel_AgencyDB;

DROP TABLE IF EXISTS Bookings;
DROP TABLE IF EXISTS Travelers;
DROP TABLE IF EXISTS Packages;
DROP TABLE IF EXISTS Destinations;


CREATE TABLE Destinations
(	destinationID INT NOT NULL AUTO_INCREMENT,
	name varchar(60),
    country varchar(60),
    description varchar(100),
    popularAttraction varchar(100),
    
    PRIMARY KEY (destinationID)
);

CREATE TABLE Packages
(	packageID INT NOT NULL AUTO_INCREMENT,
	destinationID INT,
    packageName varchar(50),
    duration varchar(30),
    price DECIMAL(10,2),
    inclusions varchar(200),
    
    PRIMARY KEY (packageID),
    
	FOREIGN KEY (destinationID)
	REFERENCES Destinations(destinationID)
	ON UPDATE CASCADE
	ON DELETE SET NULL
);

CREATE TABLE Travelers
(	travelerID INT NOT NULL AUTO_INCREMENT,
	firstName varchar(50),
    lastName varchar(50),
    email varchar(80),
    phone varchar(12),
    
    PRIMARY KEY (travelerID)
);

CREATE TABLE Bookings
(	bookingID INT NOT NULL AUTO_INCREMENT,
	travelerID INT,
    packageID INT,
    bookingDate DATE,
    travelDate DATE,
    
    PRIMARY KEY (bookingID),
    
    FOREIGN KEY (travelerID)
    REFERENCES Travelers(travelerID)
	ON UPDATE CASCADE
	ON DELETE SET NULL,
    
	FOREIGN KEY (packageID)
    REFERENCES Packages(packageID)
	ON UPDATE CASCADE
	ON DELETE SET NULL
);

####Adding Data#####

INSERT INTO Destinations (name, country, description, popularAttraction)

VALUES
	("Oslo", "Norway", "The capital of Norway", "The Oslo Oprah House"),
    ("London", "England", "The capital of England", "Big Ben"),
    ("Giza", "Egypt", "The thrid biggest city in Egypt ", "Great Pyramid of Giza"), 
    ("Paris", "France", "The capital of France", "The Eiffel Tower"), 
    ("Shizuoka", "Japan", "A mountianinous and green prefecture", "Mount Fuji");
    
INSERT INTO Packages (destinationID, packageName, duration, price, inclusions)

VALUES 
	(5, "Wild Japan ride!", "14 days", 1499.99,"Flight, hotel, car"),
    (3, "Pyramid hiking", "5 days", 1200.00, "Hiking guide, hotel"),
	(4, "Romantic Paris Getaway", "4 days", 2000.00, "Cruise on the Seine, Fine dining"),
	(5, "Tokyo Discovery", "6 days", 1800.00, "Sushi cooking class, Sumo wrestling"),
	(1, "Bergen Cultural Experience", "7 days", 1700.00, "Fish docks tour, fishingtrip"),
    (2, "Berkshire  Adventure", "3 days", 900.00, "Horseriding, Pubs, and a tour of the city"),
	(1, "Trondheim Down Under Tour", "8 days", 2500.00, "Fish resturant, fishingtrip, car and hotel"),
	(2, "London Romance", "5 days", 2200.00, "hotel, car, tourguide"),
	(5, "Osaka Foodie Delight", "4 days", 1400.00, "Street food tasting, Ramen workshop"),
	(3, "Giza Nature Experience", "6 days", 1700.00, "Tour of the city, along with 5 star resturante.");

INSERT INTO Travelers (firstName, lastName, email, phone)

VALUES
	('John', 'Doe', 'john@example.com', '123-456-7890'),
    ('Jane', 'Smith', 'jane@example.com', '987-654-3210'),
    ('Michael', 'Johnson', 'michael@example.com', '555-123-4567'),
    ('Emily', 'Davis', 'emily@example.com', '111-222-3333'),
    ('David', 'Wilson', 'david@example.com', '444-555-6666'),
    ('Linda', 'Martinez', 'linda@example.com', '999-888-7777'),
    ('Robert', 'Anderson', 'robert@example.com', '222-333-4444'),
    ('Jennifer', 'Taylor', 'jennifer@example.com', '777-999-1111'),
    ('William', 'Brown', 'william@example.com', '888-777-9999'),
    ('Karen', 'Lee', 'karen@example.com', '666-444-2222');

INSERT INTO Bookings (travelerID, packageID, bookingDate, travelDate)

VALUES
    (1, 1, '2023-10-01', '2023-11-01'),
    (2, 2, '2023-10-02', '2023-11-02'),
    (3, 3, '2023-10-03', '2023-11-03'),
    (4, 4, '2023-10-04', '2023-11-04'),
    (5, 5, '2023-10-05', '2023-11-05'),
    (6, 3, '2023-10-06', '2023-11-06'),
    (7, 2, '2023-10-07', '2023-11-07'),
    (8, 1, '2023-10-08', '2023-11-08'),
    (9, 4, '2023-10-09', '2023-11-09'),
    (10, 5, '2023-10-10', '2023-11-10');