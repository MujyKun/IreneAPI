CREATE OR REPLACE VIEW groupmembers.getmedia AS
    SELECT m.mediaid, link, faces, filetype, m.affiliationid, a.personid, a.groupid, enabled, nsfw, d.failed, d.correct
        FROM groupmembers.media m LEFT JOIN
            groupmembers.affiliation a on m.affiliationid = a.affiliationid
            LEFT JOIN guessinggame.difficulty d on d.mediaid = m.mediaid;
