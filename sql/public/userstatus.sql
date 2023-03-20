CREATE TABLE IF NOT EXISTS userstatus
(
    statusid serial,
    userid bigint,
    score integer,
    PRIMARY KEY (statusid, userid)
);

ALTER TABLE userstatus
    OWNER to postgres;
COMMENT ON TABLE userstatus
    IS 'The status of a user during a specific game.';