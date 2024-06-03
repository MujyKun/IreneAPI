CREATE TABLE IF NOT EXISTS public.datamods
(
    userid bigint,
    PRIMARY KEY (userid),
    CONSTRAINT datamods_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.datamods
    OWNER to postgres;
COMMENT ON TABLE public.datamods IS 'Data moderators of the bot.';