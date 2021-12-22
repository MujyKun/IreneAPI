CREATE TABLE IF NOT EXISTS public.apiusage
(
    userid bigint,
    endpoint text NOT NULL,
    count integer,
    PRIMARY KEY (endpoint, userid)
);

ALTER TABLE public.apiusage
    OWNER to postgres;
COMMENT ON TABLE public.apiusage
    IS 'The usage a user has to each api endpoint.';