-- A Script that list city name and id and state id for all element in DB
SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id;