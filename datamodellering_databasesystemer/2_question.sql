#2: What is the average population of the first 10 cities ordered alphabetically from China?
#Isak Mikalsen

SELECT avg(Population) AS "Average" #Finds the average population from the subqueries.
FROM (SELECT city.CountryCode, city.Name, city.Population FROM city #Selects the countrycode, name and population from city table. 
WHERE CountryCode = "CHN" #find countrycode with the code CHN.
ORDER BY city.Name ASC #Orders every china city alphabetically
LIMIT 10) AS top10; #Shows only the 10 first rows.