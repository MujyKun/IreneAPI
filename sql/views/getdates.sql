CREATE OR REPLACE VIEW groupmembers.getdates AS
    SELECT dateid, startdate, enddate FROM groupmembers.dates;