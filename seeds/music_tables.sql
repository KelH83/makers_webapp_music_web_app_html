DROP TABLE IF EXISTS albums;

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year int,
    artist_id int
);

INSERT INTO albums (title, release_year, artist_id) VALUES ('Vulgar display of power', 1992, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Cowboys from hell', 1990, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Follow the leader', 1998, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Untouchables', 2002, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Bloody kisses', 1993, 3);

DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255)
    
);

INSERT INTO artists (name, genre) VALUES ('Korn', 'Metal');
INSERT INTO artists (name, genre) VALUES ('Pantera', 'Metal');
INSERT INTO artists (name, genre) VALUES ('Type O Negative', 'Metal');
INSERT INTO artists (name, genre) VALUES ('Pentatonix', 'Pop');