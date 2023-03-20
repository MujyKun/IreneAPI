CREATE TABLE IF NOT EXISTS guessinggame.difficulty
(
    mediaid integer,
    failed integer,
    correct integer,
    PRIMARY KEY (mediaid)
);

ALTER TABLE guessinggame.difficulty
    OWNER to postgres;
COMMENT ON TABLE guessinggame.difficulty
    IS 'Difficulty of Media based on failed/correct guesses.';