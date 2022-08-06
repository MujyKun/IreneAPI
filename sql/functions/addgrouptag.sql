create or replace function groupmembers.addgrouptag(t_tag_id integer, t_group_id integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO groupmembers.grouptags(tagid, groupid) VALUES (t_tag_id, t_group_id) ON CONFLICT DO NOTHING;
end;
$$;