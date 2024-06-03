CREATE OR REPLACE VIEW groupmembers.persons_full AS
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
        WHERE pa.personid = p.personid),
   coalesce(media.mediacount, 0) AS mediacount
   FROM groupmembers.persons p LEFT OUTER JOIN groupmembers.getpersonmediacount media ON p.personid = media.personid;
