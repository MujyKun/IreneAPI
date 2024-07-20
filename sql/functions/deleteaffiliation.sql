create or replace function groupmembers.deleteaffiliation(t_affiliation_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.affiliations WHERE affiliationid = t_affiliation_id;
end;
$$;
