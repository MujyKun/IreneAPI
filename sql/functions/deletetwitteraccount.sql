create or replace function public.deletetwitteraccount(t_accountid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.twitteraccounts WHERE accountid = t_accountid;
end;
$$;
