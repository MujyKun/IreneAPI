create or replace function unscramblegame.addus(t_dateid integer, t_status_ids integer[], t_mode_id integer,
        t_difficulty_id integer)
    returns integer
    language plpgsql
as
$$
declare
    t_us_id integer;
begin

    INSERT INTO unscramblegame.games(dateid, statusids, modeid, difficultyid)
    VALUES (t_dateid, t_status_ids, t_mode_id, t_difficulty_id) returning gameid INTO t_us_id;
    return t_us_id;
end;
$$;

