CREATE OR REPLACE VIEW groupmembers.getmedia AS
    SELECT mediaid, link, faces, filetype, affiliationid, enabled FROM groupmembers.media;