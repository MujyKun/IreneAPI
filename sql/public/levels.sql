CREATE TABLE IF NOT EXISTS public.levels
(
    userid bigint,
    rob integer,
    daily integer,
    beg integer,
    profile integer,
    PRIMARY KEY (userid),
    CONSTRAINT levels_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.levels
    OWNER to postgres;
COMMENT ON TABLE public.levels
    IS 'The levels of a user.';