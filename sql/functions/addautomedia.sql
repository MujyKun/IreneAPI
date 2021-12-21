create or replace function groupmembers.addautomedia(t_channel_id bigint, t_personids integer[])
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO groupmembers.automedia(channelid, personids)
    VALUES(t_channel_id, t_personids);
end;
$$;