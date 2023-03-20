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
       hasbot,
        (SELECT array_agg(t_gp.prefix)
        FROM public.guildprefixes t_gp WHERE g.guildid = t_gp.guildid) AS prefixes
FROM public.guilds g;