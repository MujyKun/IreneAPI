CREATE TABLE IF NOT EXISTS interactions.interactiontypes
(
    typeid serial,
    name text UNIQUE,
    PRIMARY KEY (typeid)
);

ALTER TABLE interactions.interactiontypes
    OWNER to postgres;
COMMENT ON TABLE interactions.interactiontypes
    IS 'Types of Interactions';