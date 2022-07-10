create or replace function public.updateposted(t_username text, channel_ids integer[], t_posted bool)
    returns void
    language plpgsql
as
$$
begin
    UPDATE public.twitchfollowage SET posted = t_posted WHERE username = t_username AND channelid IN(channel_ids);
end;
$$;