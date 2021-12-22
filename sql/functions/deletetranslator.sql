create or replace function public.deletetranslator(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.translator WHERE userid = t_userid;
end;
$$;