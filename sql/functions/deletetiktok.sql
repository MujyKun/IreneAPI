create or replace function public.deletetiktok(t_username text, t_channel_id bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.tiktokfollowage WHERE username = t_username AND channelid = t_channel_id;
end;
$$;
