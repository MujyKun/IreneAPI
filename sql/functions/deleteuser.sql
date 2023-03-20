create or replace function public.deleteuser(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.users WHERE userid = t_userid;
end;
$$;
