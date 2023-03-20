CREATE TABLE IF NOT EXISTS groupmembers.fandom
(
    groupid integer,
    name text UNIQUE,
    PRIMARY KEY (groupid)
);

ALTER TABLE groupmembers.fandom
    OWNER to postgres;
COMMENT ON TABLE groupmembers.fandom
    IS 'A group''s fandom name (if it exists).';