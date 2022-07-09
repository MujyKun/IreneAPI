create or replace function guessinggame.updatemediaandstatus(t_game_id int, t_media_ids integer[], t_status_ids integer[])
    returns void
    language plpgsql
as
$$
begin
    UPDATE guessinggame.games SET mediaids = t_media_ids, statusids = t_status_ids WHERE gameid = t_game_id;
end;
$$;