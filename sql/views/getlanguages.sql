CREATE OR REPLACE VIEW public.getlanguages AS
    SELECT l.languageid, l.shortname, l.name,
           (SELECT json_agg(row_to_json(lp)) FROM public.languagepacks lp WHERE lp.languageid = l.languageid) AS pack
    FROM public.languages l;
