CREATE OR REPLACE VIEW public.getchannels AS
SELECT channelid, guildid
FROM public.channels c;