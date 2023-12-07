SELECT * 
FROM container_type
WHERE max_vekt > 5000 AND dagpris < 1800;

SELECT * 
FROM oppdrag
INNER JOIN kunde ON oppdrag.tlf = kunde.tlf
WHERE fra_dato = "2022-06-17" OR til_dato = "2022-06-17"
ORDER BY adresse;

SELECT container_type.type_id, 
type_navn, count(container.type_id) as antall
FROM container_type
INNER JOIN container ON container_type.type_id = container.type_id
GROUP BY container_type.type_id, type_navn;

INSERT INTO kunde(tlf, adresse)
VALUES
("69696969","lolveien 49");

INSERT INTO oppdrag(tlf, container_id, fra_dato, til_dato)
VALUES
("69696969", 5, "2022-12-12", "2022-12-24" );

CREATE VIEW FakturertKunde AS 
SELECT oppdrag.tlf, 
SUM(DATEDIFF(til_dato, fra_dato)) as AntallDager, 
SUM(dagpris * DATEDIFF(til_dato, fra_dato)) as TotalBeløp
FROM oppdrag
INNER JOIN container ON oppdrag.container_id = container.container_id
INNER JOIN container_type ON container.type_id = container_type.type_id
GROUP BY oppdrag.tlf;