CREATE TABLE IF NOT EXISTS public.users
(
    userid bigint,
    balance text DEFAULT '0',
    timezoneid integer DEFAULT NULL,
    ggfilteractive boolean DEFAULT false,
    languageid integer DEFAULT 8,
    xp integer DEFAULT 0,
    PRIMARY KEY (userid)
);

ALTER TABLE public.users
    OWNER to postgres;
COMMENT ON TABLE public.users
    IS 'User Information';