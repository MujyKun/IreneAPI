create or replace function public.addtwittersubscription(t_accountid bigint, t_channelid bigint, t_roleid bigint)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO public.twitterfollowage(accountid, channelid, roleid)
        VALUES(t_accountid, t_channelid, t_roleid) ON CONFLICT DO NOTHING;
end;
$$;
