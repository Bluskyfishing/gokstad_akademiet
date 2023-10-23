SELECT packageName, duration, price
FROM Packages
JOIN Destinations ON Packages.destinationID = Destinations.destinationID
where country = "Japan";

SELECT DISTINCT firstName, lastName
FROM Bookings 
JOIN Packages ON Bookings.packageID = Bookings.bookingID
JOIN Travelers ON Bookings.travelerID = Travelers.travelerID
WHERE destinationID = 1;

SELECT *
FROM Bookings
JOIN Packages ON Bookings.packageID = Bookings.bookingID