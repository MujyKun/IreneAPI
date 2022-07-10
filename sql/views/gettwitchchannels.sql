CREATE OR REPLACE VIEW public.gettwitchchannels AS
SELECT username, guildid, channelid, posted, roleid
FROM public.twitchfollowage c;