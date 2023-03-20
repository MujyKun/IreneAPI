create or replace function groupmembers.deletegroup(t_group_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.groups WHERE groupid = t_group_id;
end;
$$;
