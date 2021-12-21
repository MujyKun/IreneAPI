create or replace function groupmembers.getgroup(t_group_id integer)
    returns table
            (
                t_name        text,
                t_dateid      integer,
                t_description text,
                t_companyid   integer,
                t_displayid   integer,
                t_website     text,
                t_socialid    integer,
                t_tagids      integer[]
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT name, dateid, description, companyid, displayid, website, socialid, tagids
                 FROM groupmembers.groups
                 WHERE groupid = t_group_id;
end;
$$;