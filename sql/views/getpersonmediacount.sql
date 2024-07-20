CREATE OR REPLACE VIEW groupmembers.getpersonmediacount AS
    SELECT COUNT(*) AS mediacount, media.personid FROM groupmembers.media_full media GROUP BY media.personid;
