CREATE TABLE groupmembers.affiliation_positions (
    affiliationid int4 NOT NULL,
    positionid int4 NOT NULL,
    CONSTRAINT pk_affiliation_positions PRIMARY KEY (affiliationid, positionid),
    CONSTRAINT fk_affiliation_positions_affiliation FOREIGN KEY (affiliationid) REFERENCES groupmembers.affiliations (affiliationid) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_affiliation_positions_position FOREIGN KEY (positionid) REFERENCES groupmembers.positions (positionid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE groupmembers.affiliation_positions
    OWNER to postgres;
COMMENT ON TABLE groupmembers.affiliation_positions
    IS 'Links the positions to the affiliation.';