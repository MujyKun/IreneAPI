CREATE TABLE IF NOT EXISTS groupmembers.socialmedia
(
    socialid serial,
    twitter text,
    youtube text,
    melon text,
    instagram text,
    vlive text,
    spotify text,
    fancafe text,
    facebook text,
    tiktok text,
    PRIMARY KEY (socialid)
--     CONSTRAINT unique_social_media UNIQUE (twitter, youtube, melon, instagram, vlive, spotify, fancafe, facebook, tiktok),
--     CONSTRAINT non_empty_columns CHECK (
--         twitter <> '' AND
--         youtube <> '' AND
--         melon <> '' AND
--         instagram <> '' AND
--         vlive <> '' AND
--         spotify <> '' AND
--         fancafe <> '' AND
--         facebook <> '' AND
--         tiktok <> '')
);

ALTER TABLE groupmembers.socialmedia
    OWNER to postgres;
COMMENT ON TABLE groupmembers.socialmedia
    IS 'Contains information about social media. Will be linked to an entity. ';