create or replace function groupmembers.addlocation(t_country text, t_city text)
    returns integer
    language plpgsql
as
$$
declare
    t_location_id integer;
begin

    INSERT INTO groupmembers.location(country, city)
    VALUES(t_country, t_city) returning locationid INTO t_location_id;
    return t_location_id;
end;
$$;