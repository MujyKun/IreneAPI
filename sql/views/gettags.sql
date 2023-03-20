CREATE OR REPLACE VIEW groupmembers.gettags AS
    SELECT tagid, name FROM groupmembers.tag;