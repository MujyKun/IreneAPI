create or replace function public.deletesuperpatron(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.superpatron WHERE userid = t_userid;
end;
$$;