create or replace function public.updatepostedtwitter(t_account_id int, channel_ids bigint[], t_posted bool)
    returns void
    language plpgsql
as
$$
begin
    UPDATE public.twitterfollowage SET posted = t_posted WHERE accountid = t_account_id AND channelid = any(channel_ids);
end;
$$;