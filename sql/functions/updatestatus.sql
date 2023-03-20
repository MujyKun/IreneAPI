create or replace function unscramblegame.updatestatus(t_game_id int, t_status_ids integer[])
    returns void
    language plpgsql
as
$$
begin
    UPDATE unscramblegame.games SET statusids = t_status_ids WHERE gameid = t_game_id;
end;
$$;