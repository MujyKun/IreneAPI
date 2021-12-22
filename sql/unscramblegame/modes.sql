CREATE TABLE IF NOT EXISTS unscramblegame.modes
(
    modeid serial,
    name text,
    PRIMARY KEY (modeid)
);

ALTER TABLE unscramblegame.modes
    OWNER to postgres;
COMMENT ON TABLE unscramblegame.modes
    IS 'Modes of the unscramble game';