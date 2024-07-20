CREATE TABLE IF NOT EXISTS groupmembers.companies
(
    companyid serial,
    name text,
    description text,
    startdate timestamp,
    enddate timestamp,
    PRIMARY KEY (companyid),
    UNIQUE (name)
);

ALTER TABLE groupmembers.companies
    OWNER to postgres;
COMMENT ON TABLE groupmembers.companies
    IS 'An enterprise.';