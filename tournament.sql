-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE TABLE players (playerID serial not null primary key, playerName text);

CREATE TABLE playerstandings (playerID serial references players, playerName text, wins integer default 0, matches integer default 0);

CREATE TABLE matchoutcomes (matchID serial, winner integer references players, loser integer references players);
