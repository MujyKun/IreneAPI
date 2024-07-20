CREATE TABLE IF NOT EXISTS public.notifications
(
    notiid serial,
    guildid bigint NOT NULL,
    userid bigint NOT NULL,
    phrase text,
    PRIMARY KEY (notiid)
);

ALTER TABLE public.notifications
    OWNER to postgres;
COMMENT ON TABLE public.notifications
    IS 'The user phrases to notify a user about.';