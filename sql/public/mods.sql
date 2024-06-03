CREATE TABLE IF NOT EXISTS public.mods
(
    userid bigint,
    PRIMARY KEY (userid),
    CONSTRAINT mods_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.mods
    OWNER to postgres;
COMMENT ON TABLE public.mods IS 'General Moderators of the bot.';