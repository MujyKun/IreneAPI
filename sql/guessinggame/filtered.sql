CREATE TABLE IF NOT EXISTS guessinggame.filtered
(
    userid bigint,
    groupids integer[],
    personids integer[],
    PRIMARY KEY (userid)
);

ALTER TABLE guessinggame.filtered
    OWNER to postgres;
COMMENT ON TABLE guessinggame.filtered
    IS 'The groups/persons a user has filtered to show in the guessing game.';