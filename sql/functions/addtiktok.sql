create or replace function public.addtiktok(t_username text, t_user_id bigint,
t_channel_id bigint, t_role_id bigint)
    returns void
    language plpgsql
as
$$
begin

    INSERT INTO public.tiktokfollowage(username, userid, channelid, roleid)
    VALUES(t_username, t_user_id, t_channel_id, t_role_id);
end;
$$;
