create or replace function interactions.deleteinteractiontype(t_type_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM interactions.media WHERE typeid = t_type_id;
    DELETE FROM interactions.interactiontypes WHERE typeid = t_type_id;
end;
$$;