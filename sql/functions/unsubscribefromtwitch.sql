create or replace function public.unsubscribefromtwitch(t_username text, t_channel_id bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.twitchfollowage WHERE username = t_username AND channelid = t_channel_id ;
end;
$$;
