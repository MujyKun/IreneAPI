CREATE OR REPLACE VIEW groupmembers.getaffiliations AS
    SELECT affiliationid, personid, groupid, positionids, stagename FROM groupmembers.affiliation;