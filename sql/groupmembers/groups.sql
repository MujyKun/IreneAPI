CREATE TABLE IF NOT EXISTS groupmembers.groups
(
    groupid serial,
    name text,
    description text,
    companyid integer,
    displayid integer,
    website text,
    socialid integer,
    debutdate date,
    disbanddate date,
    PRIMARY KEY (groupid)
);

ALTER TABLE groupmembers.groups
    OWNER to postgres;
COMMENT ON TABLE groupmembers.groups
    IS 'A general group.';