create or replace function guessinggame.deletegg(t_gg_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM guessinggame.games WHERE gameid = t_gg_id;
end;
$$;
