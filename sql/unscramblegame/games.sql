CREATE TABLE IF NOT EXISTS unscramblegame.games
(
    gameid serial,
    dateid integer,
    statusids integer[],
    modeid integer,
    difficultyid integer,
    PRIMARY KEY (gameid),
    CONSTRAINT us_games_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT us_games_modeid FOREIGN KEY (modeid) REFERENCES modes(modeid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE unscramblegame.games
    OWNER to postgres;
COMMENT ON TABLE unscramblegame.games
    IS 'Information about an unscramble game.';