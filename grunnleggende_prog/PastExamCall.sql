CALL RegisterMedlem ('Beate', 'Rasmussen', '65465465', @MedlemsNumber);

SELECT MNr as 'MedlemsNumber', Fornavn, Etternavn
FROM Medlem
WHERE MNr = @MedlemsNumber