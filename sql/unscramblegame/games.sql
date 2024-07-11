CREATE TABLE IF NOT EXISTS unscramblegame.games
(
    gameid serial,
    statusids integer[],
    modeid integer,
    difficultyid integer,
    startdate timestamp,
    enddate timestamp,
    PRIMARY KEY (gameid)
);

ALTER TABLE unscramblegame.games
    OWNER to postgres;
COMMENT ON TABLE unscramblegame.games
    IS 'Information about an unscramble game.';