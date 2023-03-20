CREATE TABLE IF NOT EXISTS guessinggame.games
(
    gameid serial,
    dateid integer,
    mediaids integer[],
    statusids integer[],
    modeid integer,
    difficultyid integer,
    isnsfw bool,
    PRIMARY KEY (gameid)
);

ALTER TABLE guessinggame.games
    OWNER to postgres;
COMMENT ON TABLE guessinggame.games
    IS 'Information about a guessing game.';