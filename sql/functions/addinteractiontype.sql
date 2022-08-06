create or replace function interactions.addinteractiontype(t_name text)
    returns void
    language plpgsql
as
$$
begin

    INSERT INTO interactions.interactiontypes(name)
    VALUES(t_name) ON CONFLICT DO NOTHING;
end;
$$;