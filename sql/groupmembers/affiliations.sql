CREATE TABLE IF NOT EXISTS groupmembers.affiliations
(
    affiliationid serial UNIQUE,
    personid integer NOT NULL,
    groupid integer NOT NULL,
    stagename text,
    active boolean DEFAULT true,
    PRIMARY KEY (affiliationid, personid, groupid)
);

ALTER TABLE groupmembers.affiliations
    OWNER to postgres;
COMMENT ON TABLE groupmembers.affiliations
    IS 'The affiliation of a person to a group.';