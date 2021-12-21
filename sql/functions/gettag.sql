create or replace function groupmembers.gettag(t_tagid integer)
    returns table
            (
                t_name text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT name
                 FROM groupmembers.tag
                 WHERE tagid = t_tagid;
end;
$$;