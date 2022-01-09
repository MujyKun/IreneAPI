CREATE OR REPLACE VIEW groupmembers.getgroups AS
SELECT
       g.groupid,
       g.name,
       g.dateid,
       g.description,
       g.companyid,
       g.displayid,
       g.website,
       g.socialid,
    (SELECT array_agg(gt.tagid) AS tagids
    FROM groupmembers.grouptags gt
    WHERE gt.groupid = g.groupid),
   (SELECT array_agg(aliasid) AS aliasids
    FROM groupmembers.groupaliases ga
    WHERE ga.groupid = g.groupid)
FROM groupmembers.groups g;