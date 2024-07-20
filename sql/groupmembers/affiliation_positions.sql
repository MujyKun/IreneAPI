CREATE TABLE IF NOT EXISTS groupmembers.affiliation_positions (
    affiliationid int4 NOT NULL,
    positionid int4 NOT NULL,
    PRIMARY KEY (affiliationid, positionid)
);

ALTER TABLE groupmembers.affiliation_positions
    OWNER to postgres;
COMMENT ON TABLE groupmembers.affiliation_positions
    IS 'Links the positions to the affiliation.';