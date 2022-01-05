create or replace function public.gettwitterstatus(t_account_id bigint, t_channel_id bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_exists boolean;
begin
    SELECT COUNT(*) INTO t_exists
    FROM public.twitterfollowage
    WHERE channelid = t_channel_id
      AND t_account_id = accountid;
    return t_exists;
end;
$$;
