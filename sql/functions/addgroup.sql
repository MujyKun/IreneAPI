create or replace function groupmembers.addgroup(t_name text, t_description text, t_companyid integer,
                t_displayid integer, t_website text, t_socialid integer, t_debutdate date, t_disbanddate date)
    returns integer
    language plpgsql
as
$$
declare
    t_group_id integer;
begin

    INSERT INTO groupmembers.groups(name, debutdate, disbanddate, description, companyid, displayid, website, socialid)
    VALUES(t_name, t_debutdate, t_disbanddate, t_description, t_companyid, t_displayid, t_website, t_socialid) returning groupid INTO t_group_id;
    return t_group_id;
end;
$$;