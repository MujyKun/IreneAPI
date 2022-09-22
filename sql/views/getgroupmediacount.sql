CREATE OR REPLACE VIEW groupmembers.getgroupmediacount AS
    SELECT COUNT(*) AS mediacount, media.groupid FROM groupmembers.getmedia media GROUP BY media.groupid;