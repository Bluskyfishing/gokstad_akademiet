#3: Which country has the largest city when only comparing the smallest city from each country?
#Isak Mikalsen

SELECT country.name # selects country name 
FROM country #from the country table
WHERE country.code IN #finds country code in subqueries.
(SELECT countrycode FROM city WHERE city.population IN  #finds the country code for the country with the smallest population,-
(SELECT MAX(minpop) AS maxpop FROM                      # and then the largest city in that country.     
(SELECT MIN(population) AS minpop
FROM city GROUP BY countrycode) AS largest_smallest)); #Just have to have an alias for the subquery.