CREATE TABLE IF NOT EXISTS public.apitokens
(
    userid bigint,
    hashed text NOT NULL,
    accessid integer NOT NULL,
    PRIMARY KEY (userid),
    CONSTRAINT token_accessid FOREIGN KEY (accessid) REFERENCES public.apiaccess(accessid) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT token_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.apitokens
    OWNER to postgres;
COMMENT ON TABLE public.apitokens
    IS 'User IDs to their hashed API tokens';