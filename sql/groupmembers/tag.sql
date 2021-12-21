CREATE TABLE IF NOT EXISTS groupmembers.tag
(
    tagid serial,
    name text UNIQUE,
    PRIMARY KEY (tagid)
);

ALTER TABLE groupmembers.tag
    OWNER to postgres;
COMMENT ON TABLE groupmembers.tag
    IS 'A general list of tags. ';