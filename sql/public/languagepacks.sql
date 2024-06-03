CREATE TABLE IF NOT EXISTS public.languagepacks
(
    languageid int,
    label text,
    message text,
   PRIMARY KEY (languageid, label),
   CONSTRAINT pack_language FOREIGN KEY (languageid) REFERENCES public.languages(languageid) ON DELETE SET NULL ON UPDATE CASCADE
);

ALTER TABLE public.languagepacks
    OWNER to postgres;
COMMENT ON TABLE public.languagepacks
    IS 'The content for each language.';