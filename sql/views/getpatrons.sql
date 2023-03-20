CREATE OR REPLACE VIEW getpatrons AS
SELECT p.userid FROM public.patron p
UNION DISTINCT
SELECT sp.userid FROM public.superpatron sp
UNION DISTINCT
SELECT t.userid FROM public.translator t
UNION DISTINCT
SELECT pr.userid FROM public.proofreader pr
UNION DISTINCT
SELECT mod.userid FROM public.mods mod
UNION DISTINCT
SELECT dmod.userid FROM public.datamods dmod
ORDER BY userid DESC;