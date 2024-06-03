create or replace function groupmembers.addname(t_firstname text, t_lastname text)
    returns integer
    language plpgsql
as
$$
declare
    t_name_id integer;
begin

    INSERT INTO groupmembers.names(firstname, lastname)
    VALUES(t_firstname, t_lastname) returning nameid INTO t_name_id;
    return t_name_id;
end;
$$;