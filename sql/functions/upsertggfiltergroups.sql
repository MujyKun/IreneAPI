create or replace function guessinggame.upsertggfiltergroups(user_id bigint, group_ids integer[])
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO guessinggame.filtered(userid, groupids) VALUES (user_id, group_ids)
    ON CONFLICT (userid) DO UPDATE SET groupids = group_ids WHERE guessinggame.filtered.userid = user_id;
end;
$$;