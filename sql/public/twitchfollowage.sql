CREATE TABLE IF NOT EXISTS public.twitchfollowage
(
    username text,
    channelid bigint,
    posted boolean,
    roleid bigint,
    PRIMARY KEY (username, channelid),
    CONSTRAINT twitchfollowage_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.twitchfollowage
    OWNER to postgres;
COMMENT ON TABLE public.twitchfollowage
    IS 'The channels/guilds that follow a twitch channel.';