CREATE DATABASE IF NOT EXISTS ga_container_firma;
USE ga_container_firma;

DROP TABLE IF EXISTS oppdrag;
DROP TABLE IF EXISTS kunde;
DROP TABLE IF EXISTS container;
DROP TABLE IF EXISTS container_type;

CREATE TABLE container_type
(	type_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	type_navn VARCHAR(40) NOT NULL,
    max_vekt SMALLINT UNSIGNED,
    ant_kubikk SMALLINT UNSIGNED,
    dagpris FLOAT(7,2),
    
    PRIMARY KEY (type_id)
);

CREATE TABLE container
(	container_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	type_id INT UNSIGNED NOT NULL,
    
    PRIMARY KEY (container_id),
    
    FOREIGN KEY (type_id) 
    REFERENCES container_type (type_id)
);

CREATE TABLE kunde
(	tlf VARCHAR(12), 
	adresse VARCHAR(50),
    
    PRIMARY KEY (tlf)
);

CREATE TABLE oppdrag 
(	oppdrag_nr INT UNSIGNED NOT NULL AUTO_INCREMENT,
	tlf VARCHAR(12), 
    container_id INT UNSIGNED,
    fra_dato DATE,
    til_dato DATE,
    
    PRIMARY KEY (oppdrag_nr),
    
    FOREIGN KEY (tlf)
    REFERENCES kunde (tlf),
    
    FOREIGN KEY (container_id)
    REFERENCES container (container_id)
    );


INSERT INTO container_type(type_navn, max_vekt, ant_kubikk, dagpris)
VALUES
("Mini", 3000, 8, 750.00),
("Stor åpen", 6000, 25, 1500.00),
("Stor lukket", 7500, 20, 2000.00);

INSERT INTO container(type_id)
VALUES
(1),
(2),
(2),
(3),
(3);

INSERT INTO kunde(tlf, adresse)
VALUES
("11223344", "Kongenes gate 1"),
("12341234", "Jernbanealen 27"),
("88776655", "Hansegata 3");

INSERT INTO oppdrag(tlf, container_id, fra_dato, til_dato)
VALUES
("12341234", 2, "2022-06-15", "2022-06-17"),
("12341234", 3, "2022-06-15", "2022-06-17"),
("88776655", 4, "2022-06-17", "2022-06-19"),
("11223344", 2, "2022-06-18", "2022-06-19");
