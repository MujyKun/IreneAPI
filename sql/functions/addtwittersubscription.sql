
create or replace function public.addtwittersubscription(t_accountid bigint, t_channelid bigint, t_roleid bigint,
        t_posted bool)
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
        INSERT INTO public.twitterfollowage(accountid, channelid, roleid, posted)
        VALUES(t_accountid, t_channelid, t_roleid, t_posted);
    END IF;
end;
$$;
