CREATE TABLE IF NOT EXISTS guessinggame.games
(
    gameid serial,
    mediaids integer[],
    statusids integer[],
    modeid integer,
    difficultyid integer,
    isnsfw bool,
    startdate timestamp,
    enddate timestamp,
    PRIMARY KEY (gameid)
);

ALTER TABLE guessinggame.games
    OWNER to postgres;
COMMENT ON TABLE guessinggame.games
    IS 'Information about a guessing game.';