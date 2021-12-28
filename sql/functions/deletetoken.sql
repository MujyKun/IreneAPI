create or replace function public.deletetoken(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.apitokens WHERE userid = t_userid;
end;
$$;