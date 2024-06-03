CREATE TABLE IF NOT EXISTS public.selfassignroles
(
    roleid bigint,
    channelid bigint,
    name text,
    PRIMARY KEY (roleid),
    CONSTRAINT selfassignroles_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.selfassignroles
    OWNER to postgres;
COMMENT ON TABLE public.selfassignroles
    IS 'Roles that can be self assigned in a channel.';