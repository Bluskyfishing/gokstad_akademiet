#1
SELECT * 
FROM Kunde
LEFT JOIN Reservasjon ON Kunde.KNr = Reservasjon.KNr;

#2
SELECT * 
FROM Rom
INNER JOIN RomReservasjon ON Rom.RomNr = RomReservasjon.RomNr
INNER JOIN Reservasjon ON RomReservasjon.ResNr = Reservasjon.ResNr;

#3
SELECT * 
FROM Reservasjon
INNER JOIN RomReservasjon ON Reservasjon.ResNr = RomReservasjon.ResNr
WHERE Betalt = 0;

#4
SELECT *
FROM Rom
WHERE RomType = "Dobbeltrom" AND Havutsikt = 1;

#5
SELECT Fornavn, Etternavn
FROM Kunde
ORDER BY Etternavn;

#6
SELECT RomNr, FraDato, TilDato 
FROM RomReservasjon
WHERE FraDato = "2008-12-05"
ORDER BY RomNr;

#7
SELECT RomReservasjon.RomNr, count(*) as Antall
FROM RomReservasjon
JOIN Rom ON RomReservasjon.RomNr = Rom.RomNr 
GROUP BY RomReservasjon.RomNr;

#8
SELECT avg(DøgnPris) as GjennomsnittsPris, RomType
FROM Rom
GROUP BY Rom.RomType;

#9
SELECT ResNr, Fornavn, Etternavn
FROM Reservasjon
INNER JOIN Kunde ON Reservasjon.KNr = Kunde.KNr;

#10
SELECT DISTINCT Fornavn, Etternavn, FraDato, TilDato
FROM Kunde
LEFT JOIN Reservasjon ON Kunde.KNr = Reservasjon.KNr
LEFT JOIN RomReservasjon ON Reservasjon.ResNr = RomReservasjon.ResNr;

#11
SELECT * 
FROM Rom
LEFT JOIN RomReservasjon ON Rom.RomNr = RomReservasjon.RomNr;

#12
SELECT * 
FROM Rom
LEFT JOIN RomReservasjon ON Rom.RomNr = RomReservasjon.RomNr
WHERE RomReservasjon.FraDato IS NULL;

#13
SELECT * 
FROM RomReservasjon
WHERE RomReservasjon.RomNr IS NULL;

#14 
SELECT Fornavn, Etternavn, Rom.RomNr, DøgnPris, RomType
FROM Kunde
INNER JOIN Reservasjon ON Kunde.KNr = Reservasjon.KNr
INNER JOIN RomReservasjon ON Reservasjon.ResNr = RomReservasjon.ResNr
INNER JOIN Rom ON RomReservasjon.RomNr = Rom.RomNr;

#15
SELECT Kunde.KNr, Kunde.Fornavn, Kunde.Etternavn, COUNT(Reservasjon.ResNr) AS Antall
FROM Kunde
LEFT JOIN Reservasjon ON Kunde.KNr = Reservasjon.KNr
LEFT JOIN RomReservasjon ON Reservasjon.ResNr = RomReservasjon.ResNr
GROUP BY Kunde.KNr, Kunde.Fornavn, Kunde.Etternavn;

#16
SELECT * 
FROM Rom
WHERE RomType = "Dobbeltrom" and Havutsikt = 1
ORDER BY DøgnPris;

#17
SELECT Fornavn, Etternavn, RomReservasjon.ResNr, RomReservasjon.RomNr
FROM Kunde
INNER JOIN Reservasjon ON Kunde.KNr = Reservasjon.KNr
INNER JOIN RomReservasjon ON Reservasjon.ResNr = RomReservasjon.ResNr
WHERE Etternavn LIKE "Ha%";

#18
SELECT RomReservasjon.RomNr, Reservasjon.Betalt, RomReservasjon.FraDato, RomReservasjon.TilDato, TilDato - FraDato as AntallFerieDager   
FROM RomReservasjon
JOIN Rom ON RomReservasjon.RomNr = Rom.RomNr
JOIN Reservasjon ON RomReservasjon.ResNr = Reservasjon.ResNr
WHERE Betalt = 0;

#19
UPDATE RomReservasjon
SET TilDato = "2008-12-09"
WHERE ResNr = 51 AND RomNr = 104 AND TilDato = "2008-12-08";

INSERT INTO Reservasjon(ResNr, KNr, Betalt)
VALUES
(53, 3, 0);

INSERT INTO RomReservasjon(ResNr, RomNr, FraDato, TilDato)
VALUES
(53, 102, "2008-12-05", "2008-12-07");

SELECT * 
FROM RomReservasjon;