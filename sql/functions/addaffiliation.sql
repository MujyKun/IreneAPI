create or replace function groupmembers.addaffiliation(t_personid integer, t_groupid integer, t_position_ids integer[],
                                                       t_stagename text)
    returns integer
    language plpgsql
as
$$
declare
    t_affiliation_id integer;
begin

    INSERT INTO groupmembers.affiliations(personid, groupid, positionids, stagename)
    VALUES(t_personid, t_groupid, t_position_ids, t_stagename) returning affiliationid INTO t_affiliation_id;
    return t_affiliation_id;
end;
$$;


