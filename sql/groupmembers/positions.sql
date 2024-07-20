CREATE TABLE IF NOT EXISTS groupmembers."positions"
(
    positionid serial,
    name text UNIQUE,
    PRIMARY KEY (positionid)
);

ALTER TABLE groupmembers."positions"
    OWNER to postgres;
COMMENT ON TABLE groupmembers."positions"
    IS 'A position such as vocal, leader, dancer.';