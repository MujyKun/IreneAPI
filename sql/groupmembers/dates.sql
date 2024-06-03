CREATE TABLE IF NOT EXISTS groupmembers.dates
(
    dateid serial,
    startdate timestamp,
    enddate timestamp,
    PRIMARY KEY (dateid),
    CONSTRAINT unique_dates UNIQUE (startdate, enddate)
);

ALTER TABLE groupmembers.dates
    OWNER to postgres;
COMMENT ON TABLE groupmembers.dates
    IS 'Contains a start and end date.';