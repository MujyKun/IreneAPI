CREATE OR REPLACE VIEW public.gettwitterchannels AS
SELECT c.accountid, username, guildid, c.channelid, posted, roleid
FROM public.twitterfollowage c
    LEFT JOIN public.channels ch on c.channelid = ch.channelid
    LEFT JOIN public.twitteraccounts ta ON c.accountid = ta.accountid;