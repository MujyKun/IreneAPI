create or replace function guessinggame.addgg(t_startdate timestamp, t_media_ids integer[], t_status_ids integer[],
                                                    t_mode_id integer, t_difficulty_id integer, t_is_nsfw bool)
    returns integer
    language plpgsql
as
$$
declare
    t_gg_id integer;
begin

    INSERT INTO guessinggame.games(startdate, mediaids, statusids, modeid, difficultyid, isnsfw)
    VALUES (t_startdate, t_media_ids, t_status_ids, t_mode_id, t_difficulty_id, t_is_nsfw) returning gameid INTO t_gg_id;
    return t_gg_id;
end;
$$;