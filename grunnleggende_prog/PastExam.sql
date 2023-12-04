DROP DATABASE IF EXISTS gokstadtur;
CREATE DATABASE IF NOT EXISTS gokstadtur;

use gokstadtur;

#Medlem tabel
#pk mnr auto
CREATE TABLE IF NOT EXISTS Medlem
(
	MNr int PRIMARY KEY AUTO_INCREMENT,
    Fornavn VARCHAR(50),
    Etternavn VARCHAR(50),
    Tlf VARCHAR(8)
);

INSERT INTO Medlem(Fornavn, Etternavn, Tlf)
VALUES ('Ola','Hansen','12345678'),
('Kari','Mo','87654321'),
('Anette','Lien','12341234'),
('Johan','Åsen','87658765');

#Hytte tabel
#pk hnr
#navn required
#hyttetype 
CREATE TABLE IF NOT EXISTS Hytte
(
	HNr INT PRIMARY KEY AUTO_INCREMENT,
    Navn VARCHAR(50) NOT NULL,
    AntSenger TINYINT UNSIGNED, #max 255
    HytteType ENUM('Betjent', 'Selvbetjent', 'Ubetjent')
);
INSERT INTO Hytte (Navn, AntSenger, HytteType)
VALUES ('Furubu', 25, 'Betjent'),
('Blåbergstua', 40, 'Selvbetjent'),
('Steinbua', 10, 'Ubetjent');

#Tur Tabel
#pk tnr
CREATE TABLE IF NOT EXISTS Tur
(
	TNr INT PRIMARY KEY AUTO_INCREMENT,
    Beskrivelse VARCHAR(255),
    Pris DECIMAL,
    StartDato DATE,
    StartHytte INT,
    
    FOREIGN KEY (StartHytte) REFERENCES Hytte(HNr)
);

INSERT INTO Tur (TNr,Beskrivelse, Pris, StartDato, StartHytte) #Can insert auto increment if u want
VALUES (1, 'Krevende topptur', 7500.00, '2022-04-22', 2),
(2, 'Kort familietur', 4200.00, '2022-07-15', 1),
(3, 'Brevandring', 9400.00, '2022-08-02', 2),
(4, 'Klassisk fjelltur', 6400.00,'2022-08-14', 1);

#Påmelding tabel
#pk fk tnr og mnr

CREATE TABLE IF NOT EXISTS Påmelding 
(
	TNr INT NOT NULL,
    MNr INT NOT NULL,
    
    PRIMARY KEY(TNr, MNr),
    
    FOREIGN KEY(TNr) REFERENCES Tur(Tnr),
    FOREIGN KEY(MNr) REFERENCES Medlem(MNr)
);

INSERT INTO Påmelding(TNr, MNr)
VALUES (3,1),
(4,1),
(1,2),
(4,2),
(1,3),
(2,3),
(4,3);