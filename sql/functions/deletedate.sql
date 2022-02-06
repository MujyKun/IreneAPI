create or replace function groupmembers.deletedate(t_date_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.dates WHERE dateid = t_date_id;
end;
$$;
