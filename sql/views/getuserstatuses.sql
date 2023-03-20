CREATE OR REPLACE VIEW public.getuserstatuses AS
    SELECT statusid, userid, score FROM public.userstatus;
