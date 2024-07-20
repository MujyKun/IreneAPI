CREATE TABLE IF NOT EXISTS public.stats
(
    name text,
    value bigint,
    time timestamp NOT NULL DEFAULT now(),
    PRIMARY KEY (name, time)
);

ALTER TABLE public.stats
    OWNER to postgres;
COMMENT ON TABLE public.stats
    IS 'Available Stats';