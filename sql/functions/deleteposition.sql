create or replace function groupmembers.deleteposition(t_position_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.position WHERE positionid = t_position_id;
end;
$$;