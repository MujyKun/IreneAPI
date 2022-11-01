CREATE TABLE IF NOT EXISTS groupmembers.automedia
(
    channelid bigint,
    affiliationid integer,
    hoursafter integer,
    PRIMARY KEY (channelid, affiliationid)
);

ALTER TABLE groupmembers.automedia
    OWNER to postgres;
COMMENT ON TABLE groupmembers.automedia
    IS 'Automatically post a list of affiliation ids in a channel.';