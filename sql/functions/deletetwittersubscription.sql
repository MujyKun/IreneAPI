
create or replace function public.deletetwittersubscription(t_accountid bigint, t_channelid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.twitterfollowage WHERE accountid = t_accountid AND channelid = t_channelid;
end;
$$;