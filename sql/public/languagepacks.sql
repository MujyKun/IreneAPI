CREATE TABLE IF NOT EXISTS public.languagepacks
(
    languageid int,
    label text,
    message text,
   PRIMARY KEY (languageid, label)
);

ALTER TABLE public.languagepacks
    OWNER to postgres;
COMMENT ON TABLE public.languagepacks
    IS 'The content for each language.';