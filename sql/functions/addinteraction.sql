create or replace function interactions.addinteraction(t_type_id integer, t_url text)
    returns void
    language plpgsql
as
$$
begin

    INSERT INTO interactions.media(url, typeid)
    VALUES(t_url, t_type_id) ON CONFLICT DO NOTHING;
end;
$$;