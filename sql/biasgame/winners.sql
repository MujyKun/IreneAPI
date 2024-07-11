CREATE TABLE IF NOT EXISTS biasgame.winners
(
    personid integer,
    userid bigint,
    wins integer,
    PRIMARY KEY (personid, userid)
);

ALTER TABLE biasgame.winners
    OWNER to postgres;
COMMENT ON TABLE biasgame.winners
    IS 'The amount of wins a user has on a person.';