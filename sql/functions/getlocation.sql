create or replace function groupmembers.getlocation(t_locationid integer)
    returns table
            (
                t_country text,
                t_city integer
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT country, city
                 FROM groupmembers.location
                 WHERE locationid = t_locationid;
end;
$$;
