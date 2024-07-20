CREATE TABLE IF NOT EXISTS groupmembers.tags
(
    tagid serial,
    name text UNIQUE,
    PRIMARY KEY (tagid)
);

ALTER TABLE groupmembers.tags
    OWNER to postgres;
COMMENT ON TABLE groupmembers.tags
    IS 'A general list of tags. ';