CREATE OR REPLACE VIEW public.gettwitchchannels AS
SELECT username, guildid, c.channelid, posted, roleid
FROM public.twitchfollowage c LEFT JOIN public.channels ch on c.channelid = ch.channelid;