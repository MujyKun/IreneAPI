create or replace function groupmembers.addpersontag(t_tag_id integer, t_person_id integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO groupmembers.persontags(tagid, personid) VALUES (t_tag_id, t_person_id) ON CONFLICT DO NOTHING;
end;
$$;