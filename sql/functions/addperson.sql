create or replace function groupmembers.addperson(t_dateid integer, t_nameid integer, t_formernameid integer,
                                                  t_gender character(1), t_description text, t_height integer, t_displayid integer, t_socialid integer,
                                                  t_locationid integer, t_tagids integer[], t_bloodid integer, t_callcount integer)
    returns integer
    language plpgsql
as
$$
declare
    t_person_id integer;
begin

    INSERT INTO groupmembers.person(dateid, nameid, formernameid, gender, description, height, displayid, socialid,
                                    locationid, bloodid, callcount)
    VALUES (t_dateid, t_nameid, t_formernameid, t_gender, t_description, t_height,
            t_displayid, t_socialid, t_locationid, t_bloodid, t_callcount) returning personid INTO t_person_id;

    return t_person_id;
end;
$$;