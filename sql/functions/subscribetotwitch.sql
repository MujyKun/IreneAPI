create or replace function public.subscribetotwitch(t_username text, t_guild_id bigint, t_channel_id bigint,
            t_role_id bigint)
    returns void
    language plpgsql
as
$$
begin

    INSERT INTO public.twitchfollowage(username, guildid, channelid, posted, roleid) VALUES(t_username,
                                                                t_guild_id, t_channel_id, False, t_role_id);
end;
$$;