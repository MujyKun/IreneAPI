CREATE TABLE IF NOT EXISTS groupmembers.locations
(
    locationid serial,
    country text,
    city text,
    PRIMARY KEY (locationid),
    UNIQUE (country, city)
);

ALTER TABLE groupmembers.locations
    OWNER to postgres;
COMMENT ON TABLE groupmembers.locations
    IS 'Contains a country and city.';