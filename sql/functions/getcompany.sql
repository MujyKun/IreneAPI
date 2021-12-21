create or replace function groupmembers.getcompany(t_company_id integer)
    returns table
            (
                t_name text,
                t_description text,
                t_dateid integer
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT name, description, dateid
                 FROM groupmembers.company
                 WHERE companyid = t_company_id;
end;
$$;