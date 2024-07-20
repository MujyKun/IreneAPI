CREATE TABLE IF NOT EXISTS groupmembers.persons
(
    personid serial,
    nameid integer,
    formernameid integer,
    gender character(1),
    description text,
    height integer,
    displayid integer,
    socialid integer,
    locationid integer,
    callcount integer,
    birthdate date,
    deathdate date,
    bloodtype bloodtypes,
    PRIMARY KEY (personid)
);

ALTER TABLE groupmembers.persons
    OWNER to postgres;
COMMENT ON TABLE groupmembers.persons
    IS 'A general person';