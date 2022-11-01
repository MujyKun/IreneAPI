create or replace function groupmembers.deleteautomedia(t_channel_id bigint, t_aff_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.automedia WHERE channelid = t_channel_id AND affiliationid = t_aff_id;
end;
$$;