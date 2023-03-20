create or replace function groupmembers.getpositionid(t_positionname text)
    returns table
            (
                t_positionid integer
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT positionid
                 FROM groupmembers.position
                 WHERE name = t_positionname;
end;
$$;