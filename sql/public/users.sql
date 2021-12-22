CREATE TABLE IF NOT EXISTS public.users
(
    userid bigint,
    balance text,
    timezoneid integer,
    ggfilteractive boolean,
    languageid integer,
    xp integer,
    PRIMARY KEY (userid)
);

ALTER TABLE public.users
    OWNER to postgres;
COMMENT ON TABLE public.users
    IS 'User Information';