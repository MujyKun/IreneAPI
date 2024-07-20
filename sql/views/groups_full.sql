CREATE OR REPLACE VIEW groupmembers.groups_full AS
SELECT
       g.groupid,
       g.name,
       g.debutdate,
       g.disbanddate,
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
    WHERE ga.groupid = g.groupid),
    coalesce(media.mediacount, 0) AS mediacount
FROM groupmembers.groups g LEFT OUTER JOIN groupmembers.getgroupmediacount media ON g.groupid = media.groupid;

