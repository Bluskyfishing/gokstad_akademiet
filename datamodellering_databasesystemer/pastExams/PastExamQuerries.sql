use gokstadtur;

SELECT * FROM Tur
WHERE Pris < 8000.00
AND StartDato like "%-07-%";

SELECT MNr, Fornavn from Medlem
WHERE MNr IN (
	SELECT MNr FROM Påmelding
	WHERE TNr IN 
		(SELECT TNr FROM Tur
		WHERE StartHytte =2)
	);
    
SELECT Tur.TNr, Beskrivelse, StartDato, COUNT(P.TNr) AS Påmeld, COUNT(P.TNr) * Tur.Pris AS Total
From Tur
JOIN Påmelding P on Tur.TNr = P.TNr
GROUP BY Tur.TNr;

SELECT CONCAT(Fornavn, ' ', Etternavn) AS Navn, MNr
FROM Medlem
WHERE MNr NOT IN 
(
	SELECT DISTINCT MNr FROM Påmelding
);

