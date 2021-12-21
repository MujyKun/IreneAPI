create or replace function groupmembers.getposition(t_positionid integer)
    returns table
            (
                t_name text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT name
                 FROM groupmembers.position
                 WHERE positionid = t_positionid;
end;
$$;