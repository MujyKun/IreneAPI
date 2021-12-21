create or replace function groupmembers.getperson(t_person_id integer)
    returns table (
                      t_dateid integer,
                      t_nameid integer,
                      t_formernameid integer,
                      t_gender char,
                      t_description text,
                      t_height integer,
                      t_displayid integer,
                      t_socialid integer,
                      t_locationid integer,
                      t_tagids integer[],
                      t_bloodid integer,
                      t_callcount integer)
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT person.dateid, nameid, formernameid, gender, description, height, displayid, socialid,
                        locationid, tagids, bloodid, callcount
                 FROM groupmembers.person
                 WHERE personid = t_person_id;
end;
$$;