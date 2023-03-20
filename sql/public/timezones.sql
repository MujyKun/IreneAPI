CREATE TABLE IF NOT EXISTS public.timezones
(
    id serial,
    shortname text,
    name text UNIQUE,
    PRIMARY KEY (id)
);

ALTER TABLE public.timezones
    OWNER to postgres;
COMMENT ON TABLE public.timezones
    IS 'A list of timezones (used to be locale_by_timezones.json)';