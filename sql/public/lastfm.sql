CREATE TABLE IF NOT EXISTS public.lastfm
(
    userid bigint,
    username text,
    PRIMARY KEY (userid),
    CONSTRAINT lastfm_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.lastfm
    OWNER to postgres;
COMMENT ON TABLE public.lastfm
    IS 'The LastFM usernames of a user.';