create or replace function groupmembers.deletelocation(t_location_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.companies WHERE companyid = t_company_id;
end;
$$;
