CREATE TABLE IF NOT EXISTS groupmembers.names
(
    nameid serial,
    firstname text,
    lastname text,
    PRIMARY KEY (nameid),
    CONSTRAINT names_firstname_lastname_not_null CHECK (firstname IS NOT NULL AND lastname IS NOT NULL)
);

ALTER TABLE groupmembers.names
    OWNER to postgres;
COMMENT ON TABLE groupmembers.names
    IS 'Contains a first and last name. Useful for persons with several names.';