CREATE OR REPLACE VIEW public.gettiktokchannels AS
SELECT username, userid, channelid, roleid
FROM public.tiktokfollowage;