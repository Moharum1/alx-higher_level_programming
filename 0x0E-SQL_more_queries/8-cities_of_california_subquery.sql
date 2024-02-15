-- a Script that list all the elements with a state name California
SELECT id, name FROM hbtn_0d_usa.cities
    WHERE state_id = (
        SELECT id FROM hbtn_0d_usa.states
        WHERE name = "California"
    )
    ORDER BY id
