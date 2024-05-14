CREATE EXTENSION postgis;


CREATE TABLE points_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    geom GEOMETRY(Point, 4326)
);

INSERT INTO points_table (name, geom) VALUES
('Parkside A&H', ST_SetSRID(ST_Point(-118.289610, 34.018681), 4326)),
('Gerontology School', ST_SetSRID(ST_Point(-118.29041892558192, 34.02013502826645), 4326)),
('Viterbi Sign', ST_SetSRID(ST_Point(-118.288936, 34.020651), 4326)),
('Grace Ford Salviatori Hall', ST_SetSRID(ST_Point(-118.2881135913076, 34.02118740298529), 4326)),
('Annenberg', ST_SetSRID(ST_Point(-118.28700845126231, 34.02090340000862), 4326)),
('Bookstore', ST_SetSRID(ST_Point(-118.28646572186534, 34.02082003336179), 4326)),
('RTC', ST_SetSRID(ST_Point(-118.28643418699752, 34.02014121693685), 4326)),
('Price School', ST_SetSRID(ST_Point(-118.28346830086919, 34.01937242422081), 4326)),
('Nazarian Pavilion', ST_SetSRID(ST_Point(-118.2834716143121, 34.02004556499485), 4326)),
('McCarthy Quad', ST_SetSRID(ST_Point(-118.28313712062688, 34.0206046847122), 4326)),
('Fountain', ST_SetSRID(ST_Point(-118.28347289409271, 34.02218573743973), 4326)),
('Amazon', ST_SetSRID(ST_Point(-118.28518893073844, 34.02554602178926), 4326)),
('Lyon', ST_SetSRID(ST_Point(-118.28783964877957, 34.02424504483151), 4326));


SELECT ST_AsText(ST_ConvexHull(ST_Collect(geom))) AS convex_hull
FROM points_table;

SELECT id, name, ST_Distance(geom, (SELECT geom FROM points_table WHERE id = 1)) AS distance
FROM points_table
WHERE id != 1
ORDER BY geom <-> (SELECT geom FROM points_table WHERE id = 1)
LIMIT 4;

