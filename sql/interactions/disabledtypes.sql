CREATE TABLE IF NOT EXISTS interactions.disabledtypes
(
    guildid bigint,
    interactionids integer[],
    PRIMARY KEY (guildid),
    CONSTRAINT interactions_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE interactions.disabledtypes
    OWNER to postgres;
COMMENT ON TABLE interactions.disabledtypes
    IS 'The interaction types disabled for a guild';