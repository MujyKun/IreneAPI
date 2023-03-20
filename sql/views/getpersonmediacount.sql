CREATE OR REPLACE VIEW groupmembers.getpersonmediacount AS
    SELECT COUNT(*) AS mediacount, media.personid FROM groupmembers.getmedia media GROUP BY media.personid;
