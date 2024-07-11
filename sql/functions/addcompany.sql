create or replace function groupmembers.addcompany(t_name text, t_description text, t_startdate date, t_enddate date)
    returns integer
    language plpgsql
as
$$
declare
    t_company_id integer;
begin

    INSERT INTO groupmembers.companies(name, description, startdate, enddate)
    VALUES(t_name, t_description, t_startdate, t_enddate) returning companyid INTO t_company_id;
    return t_company_id;
end;
$$;
