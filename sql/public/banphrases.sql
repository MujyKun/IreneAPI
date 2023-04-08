CREATE TABLE IF NOT EXISTS public.banphrases
(
    phraseid serial,
    guildid bigint NOT NULL,
    logchannelid bigint NOT NULL,
    phrase text,
    punishment text,
    PRIMARY KEY (phraseid)
);

ALTER TABLE public.banphrases
    OWNER to postgres;
COMMENT ON TABLE public.banphrases
    IS 'The ban phrases to punish a user for.';