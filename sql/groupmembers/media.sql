CREATE TABLE IF NOT EXISTS groupmembers.media
(
    mediaid serial,
    link text,
    faces integer,
    filetype text,
    affiliationid integer,
    enabled boolean,
    nsfw boolean,
    PRIMARY KEY (mediaid),
    CONSTRAINT media_affiliationid FOREIGN KEY (affiliationid) REFERENCES groupmembers.affiliations(affiliationid) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (link, affiliationid)
);

ALTER TABLE groupmembers.media
    OWNER to postgres;
COMMENT ON TABLE groupmembers.media
    IS 'The information about a media file.';