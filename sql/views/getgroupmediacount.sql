CREATE OR REPLACE VIEW groupmembers.getgroupmediacount AS
    SELECT COUNT(*) AS mediacount, media.groupid FROM groupmembers.media_full media GROUP BY media.groupid;