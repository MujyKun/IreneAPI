CREATE TABLE IF NOT EXISTS guessinggame.filtered
(
    userid bigint,
    groupids integer[],
    personids integer[],
    PRIMARY KEY (userid),
    CONSTRAINT filteredgroups_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE guessinggame.filtered
    OWNER to postgres;
COMMENT ON TABLE guessinggame.filtered
    IS 'The groups/persons a user has filtered to show in the guessing game.';