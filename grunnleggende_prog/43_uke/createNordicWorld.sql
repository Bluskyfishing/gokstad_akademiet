Use world; 

Drop table if exists ncity; 
Drop table if exists ncountrylanguage; 
Drop table if exists ncountry; 


Create table ncountry 
( 
Code char(3) not null unique, 
Name char(52) not null, 
Population int not null, 
Capital int, 
Primary key(Code) 
); 

Create table ncity 

( 
ID int not null auto_increment, 
Name char(35) not null unique, 
CountryCode char(3) not null, 
Population int not null, 
Primary key(ID), 
Foreign key(CountryCode) references ncountry(Code) 
); 

Create table ncountrylanguage 
( 
CountryCode char(3), 
CountryLanguage char(30), 
IsOfficial Enum('T','F'), 
Percentage decimal(4,1), 
Primary key(CountryCode, CountryLanguage), 
Foreign key(CountryCode) references ncountry(Code) 
); 


# Insert data into ncountry 

Insert into ncountry 
Select code, name, population, capital 
From country where region= 'nordic countries'; 
 
# Insert data into ncity 
Insert into ncity 
Select ID, Name, CountryCode, Population 
From city where countrycode in (select code from ncountry); 
 
INSERT INTO ncountrylanguage 
Select CountryCode, Language, IsOfficial, Percentage 
From countrylanguage where CountryCode in (select code from ncountry); 