CREATE TABLE IF NOT EXISTS public.botbanned
(
    userid bigint,
    PRIMARY KEY (userid),
    CONSTRAINT botbanned_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.botbanned
    OWNER to postgres;
COMMENT ON TABLE public.botbanned IS 'Users that are currently banned from the bot.';
