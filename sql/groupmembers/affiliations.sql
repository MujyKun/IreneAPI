CREATE TABLE IF NOT EXISTS groupmembers.affiliations
(
    affiliationid serial UNIQUE,
    personid integer NOT NULL,
    groupid integer NOT NULL,
    stagename text,
    active boolean DEFAULT true,
    PRIMARY KEY (affiliationid, personid, groupid),
    CONSTRAINT affiliation_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT affiliation_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE groupmembers.affiliations
    OWNER to postgres;
COMMENT ON TABLE groupmembers.affiliations
    IS 'The affiliation of a person to a group.';