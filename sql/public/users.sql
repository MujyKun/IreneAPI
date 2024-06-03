CREATE TABLE IF NOT EXISTS public.users
(
    userid bigint,
    balance text DEFAULT '0',
    timezoneid integer DEFAULT NULL,
    ggfilteractive boolean DEFAULT false,
    languageid integer DEFAULT 8,
    xp integer DEFAULT 0,
    PRIMARY KEY (userid),
    CONSTRAINT users_timezone FOREIGN KEY (timezoneid) REFERENCES public.timezones(id) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT users_language FOREIGN KEY (languageid) REFERENCES public.languages(languageid) ON DELETE SET NULL ON UPDATE CASCADE
);

ALTER TABLE public.users
    OWNER to postgres;
COMMENT ON TABLE public.users
    IS 'User Information';