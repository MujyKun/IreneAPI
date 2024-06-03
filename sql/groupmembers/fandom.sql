CREATE TABLE IF NOT EXISTS groupmembers.fandom
(
    groupid integer,
    name text UNIQUE,
    PRIMARY KEY (groupid),
    CONSTRAINT fandom_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE groupmembers.fandom
    OWNER to postgres;
COMMENT ON TABLE groupmembers.fandom
    IS 'A group''s fandom name (if it exists).';