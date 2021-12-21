create or replace function groupmembers.getbloodtype(t_blood_id integer)
    returns table
            (
                t_name text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT name
                 FROM groupmembers.bloodtypes
                 WHERE t_blood_id = bloodid;
end;
$$;