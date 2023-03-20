CREATE TABLE IF NOT EXISTS public.eightball
(
    responseid serial,
    response text,
    PRIMARY KEY (responseid)
);

ALTER TABLE public.eightball
    OWNER to postgres;
COMMENT ON TABLE public.eightball
    IS 'Eight Ball Responses';