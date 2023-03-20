create or replace function groupmembers.deletename(t_name_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.name WHERE nameid = t_name_id;
end;
$$;
