CREATE TABLE IF NOT EXISTS modes
(
    modeid serial,
    name text,
    PRIMARY KEY (modeid)
);

ALTER TABLE modes
    OWNER to postgres;
COMMENT ON TABLE modes
    IS 'The modes available for entities.';