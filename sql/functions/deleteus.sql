create or replace function unscramblegame.deleteus(t_us_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM unscramblegame.games WHERE gameid = t_us_id;
end;
$$;
