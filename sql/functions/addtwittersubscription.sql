
create or replace function public.addtwittersubscription(t_accountid bigint, t_channelid bigint, t_roleid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists
        FROM public.twitterfollowage
        WHERE t_accountid = accountid AND t_channelid = channelid;

    IF t_already_exists = 0 THEN
        INSERT INTO public.twitterfollowage(accountid, channelid, roleid)
        VALUES(t_accountid, t_channelid, t_roleid);
    END IF;
end;
$$;