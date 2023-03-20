create or replace function groupmembers.updatedate(t_date_id int, t_end_date timestamp)
    returns void
    language plpgsql
as
$$
begin
    UPDATE groupmembers.dates SET enddate = t_end_date WHERE dateid = t_date_id;
end;
$$;