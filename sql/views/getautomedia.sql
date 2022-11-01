CREATE OR REPLACE VIEW groupmembers.getautomedia AS
    SELECT channelid, affiliationid, hoursafter FROM groupmembers.automedia;