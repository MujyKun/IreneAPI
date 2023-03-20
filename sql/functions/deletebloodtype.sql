create or replace function groupmembers.deletebloodtype(t_blood_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.bloodtypes WHERE bloodid = t_blood_id;
end;
$$;
