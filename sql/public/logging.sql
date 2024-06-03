CREATE TABLE IF NOT EXISTS public.logging
(
    guildid bigint,
    channelids bigint[],
    active boolean,
    sendall boolean,
    PRIMARY KEY (guildid),
    CONSTRAINT logging_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.logging
    OWNER to postgres;
COMMENT ON TABLE public.logging
    IS 'Guild Logging';