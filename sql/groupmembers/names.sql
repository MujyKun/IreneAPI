CREATE TABLE IF NOT EXISTS groupmembers.names
(
    nameid serial,
    firstname text,
    lastname text,
    PRIMARY KEY (nameid),
    CONSTRAINT unique_name UNIQUE (firstname, lastname)
);

ALTER TABLE groupmembers.names
    OWNER to postgres;
COMMENT ON TABLE groupmembers.names
    IS 'Contains a first and last name. Useful for people with several names. ';