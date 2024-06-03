CREATE TABLE IF NOT EXISTS groupmembers.displays
(
    displayid serial,
    avatar text,
    banner text,
    PRIMARY KEY (displayid),
    CONSTRAINT unique_display UNIQUE (avatar, banner)
);

ALTER TABLE groupmembers.displays
    OWNER to postgres;
COMMENT ON TABLE groupmembers.displays
    IS 'Contains the URL to an avatar and banner';