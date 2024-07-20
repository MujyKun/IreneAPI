create or replace function public.deletebanphrase(t_phraseid integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.banphrases WHERE phraseid = t_phraseid;
end;
$$;