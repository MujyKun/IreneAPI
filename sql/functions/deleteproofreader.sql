create or replace function public.deleteproofreader(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.proofreader WHERE userid = t_userid;
end;
$$;