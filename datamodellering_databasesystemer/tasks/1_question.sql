#1: I was born in a city named “Welkom” but I spent most of my life in a city name “Port Elizabeth”. 
#Which one is bigger? (Both are in South Africa)
#Isak Mikalsen

SELECT city.Name, city.Population #selects city name and population from the same colum.
FROM city #chooses the city table 
WHERE city.name = "Welkom" or city.name = "Port Elizabeth" #finds cities with the specified names in the name colum
ORDER BY city.Population DESC; #Sorts from most to least. 