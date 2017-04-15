-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
-- CREATE DATABASE tournament; , matches smallint


CREATE TABLE IF NOT EXISTS player ( id    SERIAL primary key,
                                    name  TEXT
                                  );

CREATE TABLE IF NOT EXISTS matches ( id     SERIAL,
                                     winner INTEGER REFERENCES player(id),
                                     loser  INTEGER REFERENCES player(id)
                                   );


CREATE VIEW player_win_info as
SELECT player.id as player_id, player.name as player_name, CASE WHEN inm.wins IS NULL THEN 0 ELSE inm.wins END as wins FROM
    (SELECT player.id as player_id, player.name as player_name, count(*) as wins
            FROM (player join matches
                on player.id = matches.winner)
                GROUP BY player.id) as inm
            RIGHT JOIN player
            on player.id = inm.player_id;

CREATE VIEW player_complete_info as
    SELECT player_win_info.player_id, player_win_info.player_name,
        player_win_info.wins, CASE WHEN fnl.match IS NULL THEN 0 ELSE fnl.match END as total_matches FROM
        (SELECT player.id as player_id, count(*) as match
            FROM (player join matches
                on player.id = matches.winner or player.id = matches.loser)
                GROUP BY player.id) as fnl
        RIGHT JOIN player_win_info
        on fnl.player_id = player_win_info.player_id
        ORDER BY wins;




