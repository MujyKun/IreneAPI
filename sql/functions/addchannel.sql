create or replace function public.addchannel(t_channelid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_channel_exists integer;
begin
    SELECT COUNT(*) INTO t_channel_exists FROM public.channels WHERE t_channelid = channelid;

    IF t_channel_exists = 0 THEN
        INSERT INTO public.channels(channelid)
        VALUES(t_channelid);
    END IF;
end;
$$;