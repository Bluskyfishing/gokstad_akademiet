CREATE DATABASE IF NOT EXISTS lidl_spotifyDB;
use lidl_spotifyDB;

DROP TABLE IF EXISTS Song;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;

CREATE TABLE Artist 
(
    artistID int NOT NULL AUTO_INCREMENT,
    artistName varchar(100),
    artistLocation varchar(100),
    agent varchar(60),
    agentcontact varchar(60),
    
    PRIMARY KEY (artistID)
);

CREATE TABLE Album 
(
	albumID int NOT NULL AUTO_INCREMENT,
    albumName varchar(100),
    genre varchar(50),
    artistID int, #FK
    
    PRIMARY KEY (albumID),
    
    FOREIGN KEY (artistID)
		REFERENCES Artist(artistID)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE Song 
(
	songID int NOT NULL AUTO_INCREMENT,
    songName varchar(100),
    playCount int,
    genre varchar(50),
    artistID int, #FK1
    albumID int, #FK2
    
    PRIMARY KEY (songID),
    
    FOREIGN KEY (albumID)
        REFERENCES Album(albumID)
        ON UPDATE CASCADE
        ON DELETE SET NULL,
        
	FOREIGN KEY (artistID)
        REFERENCES Artist(artistID)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

INSERT INTO Artist (artistName, artistLocation, agent, agentcontact)

VALUES
	("Tame Impala", "Australia","Real Manson","Sydney villers street 50"),
    ("John Smith", "123 Main Street, Cityville", "Smith & Associates", "john.smith@example.com"),
    ("Samantha Johnson", "456 Elm Avenue, Townsville", "Johnson Music Management", "samantha.johnson@example.com"),
    ("Michael Brown", "789 Oak Road, Villageton", "Brown Talent Agency", "michael.brown@example.com"),
    ("Emily Davis", "101 Pine Lane, Hamletville", "Davis Artists Group", "emily.davis@example.com"),
    ("Daniel Wilson", "234 Birch Street, Hamletville", "Wilson Entertainment", "daniel.wilson@example.com"),
    ("Olivia White", "567 Cedar Drive, Suburbia", "White Music Productions", "olivia.white@example.com"),
    ("Matthew Hall", "890 Maple Avenue, Townsville", "Hall Artist Management", "matthew.hall@example.com"),
    ("Sophia Green", "321 Oak Lane, Cityville", "Green Talent Agency", "sophia.green@example.com"),
    ("David Clark", "654 Elm Road, Suburbia", "Clark Entertainment", "david.clark@example.com"),
    ("Isabella Turner", "987 Pine Drive, Villageton", "Turner Music Group", "isabella.turner@example.com"),
	("William Adams", "111 Oak Street, Townsville", "Adams Music Management", "william.adams@example.com"),
    ("Ava Martinez", "222 Pine Road, Cityville", "Martinez Artists Group", "ava.martinez@example.com"),
    ("James Johnson", "333 Elm Avenue, Suburbia", "Johnson Entertainment", "james.johnson@example.com"),
    ("Charlotte Harris", "444 Cedar Lane, Villageton", "Harris Talent Agency", "charlotte.harris@example.com"),
    ("Benjamin Lewis", "555 Birch Drive, Hamletville", "Lewis Music Productions", "benjamin.lewis@example.com"),
    ("Mia Turner", "666 Maple Road, Suburbia", "Turner Artist Management", "mia.turner@example.com"),
    ("Ethan Walker", "777 Oak Lane, Villageton", "Walker Music Group", "ethan.walker@example.com"),
    ("Amelia Young", "888 Elm Drive, Cityville", "Young Artists Agency", "amelia.young@example.com"),
    ("Sophia King", "123 Cedar Road, Hamletville", "King Talent Management", "sophia.king@example.com");

INSERT INTO Album (albumName, genre, artistID)
VALUES
	("Slow Rush","Indie/Alternative",1),
    ("Midnight Echoes", "Pop", 2),
    ("Electric Dreamscape", "Rock", 3),
    ("Neon Fusion", "Electronic", 4),
    ("Jazz Reverie", "Jazz", 5),
    ("Urban Beats", "Hip-Hop", 6),
    ("Country Roads", "Country", 7),
    ("Blues Chronicles", "Blues", 8),
    ("R&B Grooves", "R&B", 9),
    ("Reggae Vibes", "Reggae", 10),
    ("Classical Serenity", "Classical", 11),
    ("Folk Tales", "Folk", 12),
    ("Metal Mayhem", "Metal", 13),
    ("Punk Riot", "Punk", 14),
    ("Soul Harmony", "Soul", 15),
    ("Gospel Praises", "Gospel", 16),
    ("Disco Fever", "Disco", 17),
    ("Techno Fusion", "Techno", 18),
    ("Funk Odyssey", "Funk", 19),
    ("Opera Fantasia", "Opera", 20);

INSERT INTO Song(songName, playCount, genre, artistID, albumID)
VALUES
	("Borderline",521000000,"Inde/Alternative", 1, 1),
    ("Dancing in the Rain", 850000, "Indie/Alternative", 1, 1),
    ("Electric Dreams", 720000, "Electronic", 2, 2),
    ("Under the Moonlight", 590000, "Indie/Alternative", 2, 2),
    ("Midnight Serenade", 450000, "Pop", 3, 3),
    ("Echoes of Eternity", 680000, "Rock", 3, 3),
    ("Whispers in the Wind", 540000, "Electronic", 4, 4),
    ("Neon Dreams", 670000, "Indie/Alternative", 4, 4),
    ("Starry Nights", 820000, "Pop", 5, 5),
    ("Sunset Melodies", 710000, "Rock", 5, 5),
    ("City Lights", 930000, "Electronic", 6, 6),
    ("Aurora Borealis", 600000, "Indie/Alternative", 6, 6),
    ("Lost in the Groove", 880000, "Pop", 7, 7),
    ("Crystal Reflections", 780000, "Rock", 7, 7),
    ("Rhythms of the Jungle", 720000, "Electronic", 8, 8),
    ("Ocean Serenity", 870000, "Indie/Alternative", 8, 8),
    ("Dreamscape", 790000, "Pop", 9, 9),
    ("Eternal Bliss", 680000, "Rock", 9, 9),
    ("Harmony of Hearts", 910000, "Electronic", 10, 10),
    ("Celestial Wanderer", 670000, "Indie/Alternative", 10, 10),
    ("Sonic Odyssey", 820000, "Pop", 11, 11),
    ("Velvet Skies", 940000, "Rock", 11, 11),
    ("Mystic Melodies", 700000, "Electronic", 12, 12),
    ("Twilight Reverie", 890000, "Indie/Alternative", 12, 12),
    ("Lunar Whispers", 760000, "Pop", 13, 13),
    ("Timeless Echo", 840000, "Rock", 13, 13),
    ("Astral Journeys", 720000, "Electronic", 14, 14),
    ("Enchanted Pathways", 910000, "Indie/Alternative", 14, 14),
    ("Serenading Stars", 780000, "Pop", 15, 15),
	("Summer Breeze", 720000, "Indie/Alternative", 15, 15),
    ("Starlight Serenade", 890000, "Indie/Alternative", 16, 16),
    ("Echoes of Love", 550000, "Indie/Alternative", 16, 16),
    ("City of Dreams", 620000, "Indie/Alternative", 17, 17),
    ("Whispers in the Night", 780000, "Indie/Alternative", 17, 17),
    ("Electric Dreams", 920000, "Indie/Alternative", 18, 18),
    ("Moonlit Melodies", 660000, "Indie/Alternative", 18, 18),
    ("Melancholy Moods", 740000, "Indie/Alternative", 19, 19),
    ("Soothing Sounds", 810000, "Indie/Alternative", 19, 19),
    ("Not a Starry Night", 910000, "Indie/Alternative", 20, 20),
    ("Waves of Wonder", 660000, "Rock", 20, 20);
