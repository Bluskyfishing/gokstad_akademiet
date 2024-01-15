#4: Produce the result pictured below by using world.city and world.country.
#Isak Mikalsen

SELECT Name, population #selects name and population of cities
FROM city #from the city table 
WHERE city.id in #finds the city-id for the capitals in the country table. With the help of a subquery.
(Select capital from country 
WHERE Region= "nordic countries"); #Finds the countries tagged with the "Nordic countries"-tag.
