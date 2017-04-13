-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
-- CREATE DATABASE tournament;
CREATE TABLE records ( id SERIAL primary key, name TEXT, wins smallint, matches smallint );
CREATE TABLE matches ( id SERIAL, winner INTEGER REFERENCES records(id),
                        loser INTEGER REFERENCES records(id) );

