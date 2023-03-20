create or replace function public.addchannel(t_channelid bigint, t_guildid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_channel_exists integer;
begin
    SELECT COUNT(*) INTO t_channel_exists FROM public.channels WHERE t_channelid = channelid;

    IF t_channel_exists = 0 THEN
        INSERT INTO public.channels(channelid, guildid)
        VALUES(t_channelid, t_guildid);
    END IF;
end;
$$;
