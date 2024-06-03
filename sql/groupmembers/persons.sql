CREATE TABLE IF NOT EXISTS groupmembers.persons
(
    personid serial,
    dateid integer,
    nameid integer,
    formernameid integer,
    gender character(1),
    description text,
    height integer,
    displayid integer,
    socialid integer,
    locationid integer,
    bloodtype bloodtypes,
    callcount integer,
    PRIMARY KEY (personid),
    CONSTRAINT person_displayid FOREIGN KEY (displayid) REFERENCES groupmembers.displays(displayid) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT person_socialid FOREIGN KEY (socialid) REFERENCES groupmembers.socialmedia(socialid) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT person_nameid FOREIGN KEY (nameid) REFERENCES groupmembers.names(nameid) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT person_formernameid FOREIGN KEY (formernameid) REFERENCES groupmembers.names(nameid) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT person_locationid FOREIGN KEY (locationid) REFERENCES groupmembers.locations(locationid) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT person_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE
);

ALTER TABLE groupmembers.persons
    OWNER to postgres;
COMMENT ON TABLE groupmembers.persons
    IS 'A general person';