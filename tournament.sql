-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file,
-- also 'create view' statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Creates vagrant.

\c vagrant;

-- Will drop the database tournament, if it exists.

DROP DATABASE IF EXISTS tournament;

-- Creates the tournament database and connects to it.

CREATE DATABASE tournament;
\c tournament;

-- Creates table called players.

CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  name TEXT
);

-- Creates table called matches with Foreign Keys to players.id.

CREATE TABLE matches (
  id SERIAL PRIMARY KEY,
  winner INTEGER REFERENCES players(id),
  loser INTEGER REFERENCES players(id)
);

-- Creates view for matches played that is sorted by win count.

CREATE VIEW standings AS
SELECT p.id as id, p.name,
(SELECT COUNT(*) FROM matches WHERE p.id = matches.winner) as win_count,
(SELECT COUNT(*) FROM matches WHERE p.id in (winner, loser)) as played_matches
FROM players p
GROUP BY p.id
ORDER BY win_count DESC;
