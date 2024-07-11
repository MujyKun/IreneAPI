create or replace function unscramblegame.addus(t_start_date timestamp, t_status_ids integer[], t_mode_id integer,
        t_difficulty_id integer)
    returns integer
    language plpgsql
as
$$
declare
    t_us_id integer;
begin

    INSERT INTO unscramblegame.games(startdate, statusids, modeid, difficultyid)
    VALUES (t_start_date, t_status_ids, t_mode_id, t_difficulty_id) returning gameid INTO t_us_id;
    return t_us_id;
end;
$$;

