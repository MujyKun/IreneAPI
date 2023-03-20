create or replace function guessinggame.upsertggfilterpersons(user_id bigint, person_ids integer[])
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO guessinggame.filtered(userid, personids) VALUES (user_id, person_ids)
    ON CONFLICT (userid) DO UPDATE SET personids = person_ids WHERE guessinggame.filtered.userid = user_id;
end;
$$;