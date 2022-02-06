create or replace function groupmembers.deletetag(t_tag_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.tag WHERE tagid = t_tag_id;
end;
$$;
