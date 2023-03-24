CREATE TABLE IF NOT EXISTS public.tiktokfollowage
(
    username text,
    userid bigint,
    channelid bigint,
    roleid bigint,
    PRIMARY KEY (username, userid)
);

ALTER TABLE public.tiktokfollowage
    OWNER to postgres;
COMMENT ON TABLE public.tiktokfollowage
    IS 'The channels/guilds that follow a tiktok account. Each record belongs to a patron.';