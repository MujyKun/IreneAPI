CREATE OR REPLACE VIEW public.getprefixes AS
SELECT
        DISTINCT (gp.guildid),
        (SELECT array_agg(t_gp.prefix)
        FROM public.guildprefixes t_gp WHERE gp.guildid = t_gp.guildid) as prefixes
FROM public.guildprefixes gp;