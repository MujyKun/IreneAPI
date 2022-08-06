create or replace function interactions.addinteractionmedia(t_url text, type_id integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO interactions.media(url, typeid)
    VALUES(t_url, type_id) ON CONFLICT DO NOTHING;
end;
$$;