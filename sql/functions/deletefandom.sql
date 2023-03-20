create or replace function groupmembers.deletefandom(t_group_id integer, t_name text)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.fandom WHERE groupid = t_group_id AND name = t_name ;
end;
$$;