create or replace function groupmembers.getname(t_nameid integer)
    returns table
            (
                t_firstname text,
                t_lastname text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT firstname, lastname
                 FROM groupmembers.name
                 WHERE t_nameid = nameid;
end;
$$;