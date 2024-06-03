CREATE TABLE IF NOT EXISTS interactions.media
(
    url text,
    typeid integer,
    PRIMARY KEY (url),
    CONSTRAINT media_typeid FOREIGN KEY (typeid) REFERENCES interactions.interactiontypes(typeid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE interactions.media
    OWNER to postgres;
COMMENT ON TABLE interactions.media
    IS 'Media URLs';