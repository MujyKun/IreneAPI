create or replace function public.deletemod(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.mods WHERE userid = t_userid;
end;
$$;
