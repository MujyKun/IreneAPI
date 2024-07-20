CREATE TABLE IF NOT EXISTS groupmembers.fandoms
(
    groupid integer,
    name text UNIQUE,
    PRIMARY KEY (groupid)
);

ALTER TABLE groupmembers.fandoms
    OWNER to postgres;
COMMENT ON TABLE groupmembers.fandoms
    IS 'A group''s fandom name (if it exists).';