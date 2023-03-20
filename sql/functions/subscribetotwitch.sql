create or replace function public.subscribetotwitch(t_username text, t_channel_id bigint, t_role_id bigint)
    returns void
    language plpgsql
as
$$
begin

    INSERT INTO public.twitchfollowage(username, channelid, posted, roleid) VALUES(t_username, t_channel_id,
                                                                                   False, t_role_id);
end;
$$;