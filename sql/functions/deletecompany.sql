create or replace function groupmembers.deletecompany(t_company_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.company WHERE companyid = t_company_id;
end;
$$;
