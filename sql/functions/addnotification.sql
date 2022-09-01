create or replace function public.addnotification(t_guildid integer,
                                t_userid integer, t_phrase text)
    returns integer
    language plpgsql
as
$$
declare
    t_noti_id integer;
begin

    INSERT INTO public.notifications(guildid, userid, phrase)
    VALUES(t_guildid, t_userid, t_phrase) returning notiid INTO t_noti_id;
    return t_noti_id;
end;
$$;
