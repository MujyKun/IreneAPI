create or replace function groupmembers.addbloodtype(t_name text)
    returns integer
    language plpgsql
as
$$
declare
    t_blood_id integer;
begin

    INSERT INTO groupmembers.bloodtypes(name)
    VALUES(t_name) returning bloodid INTO t_blood_id;
    return t_blood_id;
end;
$$;


