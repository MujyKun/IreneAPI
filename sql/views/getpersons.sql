CREATE OR REPLACE VIEW groupmembers.getpersons AS
    SELECT
        p.personid,
        p.dateid,
        p.nameid,
        p.formernameid,
        p.displayid,
        p.socialid,
        p.locationid,
        p.bloodid,
        gender,
        description,
        height,
        callcount,
       (SELECT array_agg(pt.tagid) AS tagids
            FROM groupmembers.persontags pt
            WHERE pt.personid = p.personid),
       (SELECT array_agg(aliasid) AS aliasids
            FROM groupmembers.personaliases pa
            WHERE pa.personid = p.personid)
       FROM groupmembers.person p;