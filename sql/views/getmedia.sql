CREATE OR REPLACE VIEW groupmembers.getmedia AS
    SELECT mediaid, link, faces, filetype, media.affiliationid, a.personid, a.groupid, enabled, nsfw
        FROM groupmembers.media LEFT JOIN
            groupmembers.affiliation a on media.affiliationid = a.affiliationid;
