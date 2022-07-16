CREATE TABLE IF NOT EXISTS public.languages
(
    languageid serial,
    shortname text UNIQUE,
    name text UNIQUE,
    PRIMARY KEY (languageid)
);

ALTER TABLE public.languages
    OWNER to postgres;
COMMENT ON TABLE public.languages
    IS 'The languages the bot has content for.';