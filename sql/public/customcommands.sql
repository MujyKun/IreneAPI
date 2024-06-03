CREATE TABLE IF NOT EXISTS public.customcommands
(
    commandid serial,
    guildid bigint,
    name text,
    content text,
    PRIMARY KEY (commandid),
    CONSTRAINT customcommands_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.customcommands
    OWNER to postgres;
COMMENT ON TABLE public.customcommands
    IS 'Custom commands for a guild.';