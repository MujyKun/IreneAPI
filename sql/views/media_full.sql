CREATE OR REPLACE VIEW groupmembers.media_full AS
    SELECT m.mediaid, link, faces, filetype, m.affiliationid, a.personid, a.groupid, enabled, nsfw, d.failed, d.correct
        FROM groupmembers.media m LEFT JOIN
            groupmembers.affiliations a on m.affiliationid = a.affiliationid
            LEFT JOIN guessinggame.difficulty d on d.mediaid = m.mediaid;
