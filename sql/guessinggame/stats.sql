CREATE TABLE IF NOT EXISTS guessinggame.stats
(
    userid bigint,
    modeid integer,
    difficultyid integer,
    value integer,
    PRIMARY KEY (userid),
    CONSTRAINT gg_stats_modeid FOREIGN KEY (modeid) REFERENCES modes(modeid) ON DELETE SET NULL ON UPDATE CASCADE
);

ALTER TABLE guessinggame.stats
    OWNER to postgres;
COMMENT ON TABLE guessinggame.stats
    IS 'Stats a user has in every mode of the guessing game.';