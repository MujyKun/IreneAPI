CREATE OR REPLACE VIEW groupmembers.getlocations AS
    SELECT locationid, country, city FROM groupmembers.location;