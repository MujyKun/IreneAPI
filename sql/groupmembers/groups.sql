CREATE TABLE IF NOT EXISTS groupmembers.groups
(
    groupid serial,
    name text,
    dateid integer,
    description text,
    companyid integer,
    displayid integer,
    website text,
    socialid integer,
    PRIMARY KEY (groupid),
    CONSTRAINT group_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT group_companyid FOREIGN KEY (companyid) REFERENCES groupmembers.companies(companyid) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT group_displayid FOREIGN KEY (displayid) REFERENCES groupmembers.displays(displayid) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT group_socialid FOREIGN KEY (socialid) REFERENCES groupmembers.socialmedia(socialid) ON DELETE SET NULL ON UPDATE CASCADE
);

ALTER TABLE groupmembers.groups
    OWNER to postgres;
COMMENT ON TABLE groupmembers.groups
    IS 'A general group.';