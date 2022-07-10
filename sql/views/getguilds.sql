CREATE OR REPLACE VIEW public.getguilds AS
SELECT
       guildid,
       name,
       emojicount,
       afktimeout,
       icon,
       ownerid,
       banner,
       description,
       mfalevel,
       splash,
       nitrolevel,
       boosts,
       textchannelcount,
       voicechannelcount,
       categorycount,
       emojilimit,
       membercount,
       rolecount,
       shardid,
       createdate,
       hasbot
FROM public.guilds g;