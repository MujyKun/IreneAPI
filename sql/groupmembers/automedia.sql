CREATE TABLE IF NOT EXISTS groupmembers.automedia
(
    channelid bigint,
    affiliationid integer,
    hoursafter integer,
    PRIMARY KEY (channelid, affiliationid),
    CONSTRAINT automedia_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT automedia_affid FOREIGN KEY (affiliationid) REFERENCES groupmembers.affiliations(affiliationid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE groupmembers.automedia
    OWNER to postgres;
COMMENT ON TABLE groupmembers.automedia
    IS 'Automatically post a list of affiliation ids in a channel.';