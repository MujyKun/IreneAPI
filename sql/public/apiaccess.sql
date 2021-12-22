CREATE TABLE IF NOT EXISTS public.apiaccess
(
    accessid serial,
    name text UNIQUE,
    PRIMARY KEY (accessid)
);

ALTER TABLE public.apiaccess
    OWNER to postgres;