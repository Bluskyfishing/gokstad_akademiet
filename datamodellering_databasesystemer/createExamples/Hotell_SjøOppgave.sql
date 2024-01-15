CREATE DATABASE IF NOT EXISTS Hotell_Sjøluft;
use Hotell_Sjøluft;

DROP TABLE IF EXISTS RomReservasjon;
DROP TABLE IF EXISTS Reservasjon;
DROP TABLE IF EXISTS Rom;
DROP TABLE IF EXISTS Kunde;

CREATE TABLE Kunde
(	KNr INT UNSIGNED NOT NULL AUTO_INCREMENT,
	Fornavn VARCHAR(60) NOT NULL,
    Etternavn VARCHAR(60),
    Epost VARCHAR(100),

    PRIMARY KEY (KNr)
);

CREATE TABLE Rom
(	RomNr INT UNSIGNED NOT NULL,
	DøgnPris FLOAT(6,2) UNSIGNED,
    RomType ENUM("Enkeltrom", "Dobbeltrom", "Familierom", "Suite") NOT NULL,
    Havutsikt TINYINT NOT NULL,

    PRIMARY KEY (RomNr)
);

CREATE TABLE Reservasjon
(	ResNr INT UNSIGNED NOT NULL AUTO_INCREMENT,
	KNr INT UNSIGNED,
    Betalt TINYINT NOT NULL,

    PRIMARY KEY (ResNr),

    FOREIGN KEY (KNr)
    REFERENCES Kunde(KNr)
    ON UPDATE CASCADE
	ON DELETE SET NULL
);

CREATE TABLE RomReservasjon
(	ResNr INT UNSIGNED NOT NULL,
	RomNr INT UNSIGNED NOT NULL,
    FraDato DATE,
    TilDato DATE,
    
    PRIMARY KEY (ResNr,RomNr,FraDato),
    
    FOREIGN KEY (ResNr)
    REFERENCES Reservasjon(ResNr)
	ON UPDATE CASCADE
	ON DELETE CASCADE,
    
	FOREIGN KEY (RomNr)
    REFERENCES Rom(RomNr)
	ON UPDATE CASCADE
	ON DELETE CASCADE
);

INSERT INTO Kunde(Fornavn, Etternavn, Epost)
VALUES
("Per", "Hansen", "ph@xyz.no"),
("Lise", "Jensen", "lisej@abc.com"),
("Karianne", "Trondsen", "trondsen@xyz.no");

INSERT INTO Rom(RomNr, DøgnPris, RomType, Havutsikt)
VALUES
(101, 1250.00, "Dobbeltrom", 1),
(102, 1050.00, "Familierom", 0),
(103, 950.00, "Dobbeltrom", 1),
(104, 800.00, "Enkeltrom", 0),
(201, 1650.00, "Suite", 1);

INSERT INTO Reservasjon(ResNr, KNr, Betalt)
VALUES
(51, 2, 0),
(52, 1, 1);

INSERT INTO RomReservasjon(ResNr, RomNr, FraDato, TilDato)
VALUES
(51, 103, "2008-12-05", "2008-12-07"),
(51, 104, "2008-12-05", "2008-12-08"),
(52, 201, "2008-12-06", "2008-12-14");