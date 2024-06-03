CREATE TABLE IF NOT EXISTS unscramblegame.stats
(
    userid bigint,
    modeid integer,
    difficultyid integer,
    value integer,
    PRIMARY KEY (value),
    CONSTRAINT us_stats_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT us_stats_modeid FOREIGN KEY (modeid) REFERENCES modes(modeid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE unscramblegame.stats
    OWNER to postgres;
COMMENT ON TABLE unscramblegame.stats
    IS 'Stats a user has in every mode of the unscramble game.';