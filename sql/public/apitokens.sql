CREATE TABLE IF NOT EXISTS public.apitokens
(
    userid bigint,
    hashed text NOT NULL,
    accessid integer NOT NULL,
    PRIMARY KEY (userid)
);

ALTER TABLE public.apitokens
    OWNER to postgres;
COMMENT ON TABLE public.apitokens
    IS 'User IDs to their hashed API tokens';