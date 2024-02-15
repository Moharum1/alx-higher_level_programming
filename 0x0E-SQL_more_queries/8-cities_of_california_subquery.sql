-- a Script that list all the elements with a state name California
SELECT id, name FROM cities
    WHERE state_id = (
        SELECT id FROM states
        WHERE name = "California"
    )
    ORDER BY id
