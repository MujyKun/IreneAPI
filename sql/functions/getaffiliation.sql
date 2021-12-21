create or replace function groupmembers.getaffiliation(t_affiliation_id integer)
    returns table
            (
                t_personid integer,
                t_groupid integer,
                t_positionids integer[],
                t_stagename text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT personid, groupid, positionids, stagename
                 FROM groupmembers.affiliation
                 WHERE affiliationid = t_affiliation_id;
end;
$$;