UPDATE Song
SET playCount = 1000000
WHERE songName = "Velvet Skies";

UPDATE Song
SET playcount = 6000000
WHERE songName = "Starry Nights";

#SELECT Artist.artistName, Artist.artistID, Song.songName, Song.playCount
#FROM Artist
#INNER JOIN Song ON Song.artistID = Artist.artistID
#ORDER BY playcount DESC
#LIMIT 10;

SELECT Artist.artistName, SUM(Song.playCount) AS totalPlays
FROM Artist
LEFT JOIN Song ON Artist.artistID = Song.artistID
GROUP BY Artist.artistID
ORDER BY totalPlays DESC
LIMIT 10;