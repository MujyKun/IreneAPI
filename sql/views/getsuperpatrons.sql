CREATE OR REPLACE VIEW getsuperpatrons AS
SELECT sp.userid FROM public.superpatron sp
UNION DISTINCT
SELECT mod.userid FROM public.mods mod
ORDER BY userid DESC;