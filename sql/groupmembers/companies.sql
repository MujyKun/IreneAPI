CREATE TABLE IF NOT EXISTS groupmembers.companies
(
    companyid serial,
    name text,
    description text,
    dateid integer,
    PRIMARY KEY (companyid),
    CONSTRAINT unique_company_name UNIQUE (name),
    CONSTRAINT company_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE
);

ALTER TABLE groupmembers.companies
    OWNER to postgres;
COMMENT ON TABLE groupmembers.companies
    IS 'An enterprise.';