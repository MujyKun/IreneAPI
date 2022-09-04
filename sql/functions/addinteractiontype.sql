create or replace function interactions.addinteractiontype(t_name text)
    returns integer
    language plpgsql
as
$$
declare
    t_type_id integer;
begin

    INSERT INTO interactions.interactiontypes(name)
    VALUES(t_name) returning typeid INTO t_type_id;
    return t_type_id;
end;
$$;