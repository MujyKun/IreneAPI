CREATE TABLE IF NOT EXISTS public.notifications
(
    noti_id serial,
    guildid bigint NOT NULL,
    userid bigint NOT NULL,
    phrase text,
    PRIMARY KEY (noti_id)
);

ALTER TABLE public.notifications
    OWNER to postgres;
COMMENT ON TABLE public.notifications
    IS 'The user phrases to notify a user about.';