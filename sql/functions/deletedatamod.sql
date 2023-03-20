create or replace function public.deletedatamod(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.datamods WHERE userid = t_userid;
end;
$$;
