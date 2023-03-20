create or replace function public.toggleggfilter(t_userid bigint, active bool)
    returns void
    language plpgsql
as
$$
begin
    UPDATE public.users SET ggfilteractive = active WHERE userid = t_userid;
end;
$$;
