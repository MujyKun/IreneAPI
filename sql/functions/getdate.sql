create or replace function groupmembers.getdate(t_dateid integer)
    returns table
            (
                t_startdate timestamp,
                t_enddate timestamp
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT startdate, enddate
                 FROM groupmembers.dates
                 WHERE dateid = t_dateid;
end;
$$;
