CREATE TABLE IF NOT EXISTS public.roles
(
    roleid bigint,
    typeids integer[],
    guildid bigint,
    PRIMARY KEY (roleid),
    CONSTRAINT roles_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.roles
    OWNER to postgres;
COMMENT ON TABLE public.roles
    IS 'Roles with a bot purpose.';