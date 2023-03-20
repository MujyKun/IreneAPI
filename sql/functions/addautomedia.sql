create or replace function groupmembers.addautomedia(t_channel_id bigint, t_aff_id integer, t_hours_after integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO groupmembers.automedia(channelid, affiliationid, hoursafter)
    VALUES(t_channel_id, t_aff_id, t_hours_after) ON CONFLICT DO NOTHING;
end;
$$;