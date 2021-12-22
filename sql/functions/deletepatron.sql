create or replace function public.deletepatron(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.patron WHERE userid = t_userid;
end;
$$;
