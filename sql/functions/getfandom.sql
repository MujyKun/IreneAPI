create or replace function groupmembers.getfandom(t_groupid integer)
    returns table
            (
                t_name text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT name
                 FROM groupmembers.fandom
                 WHERE t_groupid = groupid;
end;
$$;