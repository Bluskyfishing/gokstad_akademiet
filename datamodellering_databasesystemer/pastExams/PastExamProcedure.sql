DROP PROCEDURE IF EXISTS RegisterMedlem;
DELIMITER // 
CREATE PROCEDURE RegisterMedlem (
				IN FornavnInput VARCHAR(50),
                IN EtternavnInput VARCHAR(50),
                IN TlfInput VARCHAR(8),
                OUT MNrInput INT
)
BEGIN 
	INSERT INTO Medlem (MNr, Fornavn, Etternavn, Tlf)
    VALUE (MNrInput, FornavnInput, EtternavnInput, TlfInput);
    SET MNrInput = LAST_INSERT_ID();
END //
DELIMITER ;