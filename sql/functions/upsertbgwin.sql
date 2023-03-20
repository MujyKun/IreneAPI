create or replace function biasgame.upsertbgwin(t_user_id bigint, t_person_id integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO biasgame.winners(personid, userid, wins) VALUES (t_person_id, t_user_id, 1)
    ON CONFLICT (personid, userid) DO UPDATE SET wins = biasgame.winners.wins + 1 WHERE biasgame.winners.personid = t_person_id AND biasgame.winners.userid = t_user_id;

end;
$$;