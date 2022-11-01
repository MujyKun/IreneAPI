create or replace function groupmembers.addautomedia(t_channel_id bigint, t_aff_id integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO groupmembers.automedia(channelid, affiliationid)
    VALUES(t_channel_id, t_aff_id) ON CONFLICT DO NOTHING;
end;
$$;