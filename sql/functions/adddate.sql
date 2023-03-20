create or replace function groupmembers.adddate(t_startdate timestamp, t_enddate timestamp)
    returns integer
    language plpgsql
as
$$
declare
    t_date_id integer;
begin

    INSERT INTO groupmembers.dates(startdate, enddate)
    VALUES(t_startdate, t_enddate) returning dateid INTO t_date_id;
    return t_date_id;
end;
$$;