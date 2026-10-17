-- Q4: Venues with seating capacity > 50,000
SELECT venue_name, city, country, capacity FROM venues WHERE capacity > 50000 ORDER BY capacity DESC;