create or replace function public.addtwitteraccount(t_accountid bigint, t_username text)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.twitteraccounts WHERE t_accountid = accountid;

    IF t_already_exists = 0 THEN
        INSERT INTO public.twitteraccounts(accountid, username)
        VALUES(t_accountid, t_username);
    END IF;
end;
$$;