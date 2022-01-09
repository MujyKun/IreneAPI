CREATE OR REPLACE VIEW groupmembers.getfandoms AS
    SELECT groupid, name FROM groupmembers.fandom;