create or replace function groupmembers.gettagid(t_tagname text)
    returns table
            (
                t_tagid integer
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT tagid
                 FROM groupmembers.tag
                 WHERE name = t_tagname;
end;
$$;