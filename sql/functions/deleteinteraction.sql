create or replace function interactions.deleteinteraction(t_type_id integer, t_url text)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM interactions.media WHERE url=t_url AND typeid=t_type_id;
end;
$$;