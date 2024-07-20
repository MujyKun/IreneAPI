create or replace function groupmembers.addposition(t_name text)
    returns integer
    language plpgsql
as
$$
declare
    t_position_id integer;
begin

    INSERT INTO groupmembers.positions(name)
    VALUES(t_name) returning positionid INTO t_position_id;
    return t_position_id;
end;
$$;