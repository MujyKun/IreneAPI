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
    UNIQUE (link, affiliationid)
);

ALTER TABLE groupmembers.media
    OWNER to postgres;
COMMENT ON TABLE groupmembers.media
    IS 'The information about a media file.';