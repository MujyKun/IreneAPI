create or replace function groupmembers.deleteperson(t_person_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.persons WHERE personid  = t_person_id;
end;
$$;
