CREATE TABLE IF NOT EXISTS guessinggame.games
(
    gameid serial,
    dateid integer,
    mediaids integer[],
    statusids integer[],
    modeid integer,
    difficultyid integer,
    isnsfw bool,
    PRIMARY KEY (gameid),
    CONSTRAINT gg_games_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT gg_games_modeid FOREIGN KEY (modeid) REFERENCES modes(modeid) ON DELETE SET NULL ON UPDATE CASCADE
);

ALTER TABLE guessinggame.games
    OWNER to postgres;
COMMENT ON TABLE guessinggame.games
    IS 'Information about a guessing game.';