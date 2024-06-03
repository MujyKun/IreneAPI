create or replace function groupmembers.addcompany(t_name text, t_description text, t_dateid integer)
    returns integer
    language plpgsql
as
$$
declare
    t_company_id integer;
begin

    INSERT INTO groupmembers.companies(name, description, dateid)
    VALUES(t_name, t_description, t_dateid) returning companyid INTO t_company_id;
    return t_company_id;
end;
$$;
