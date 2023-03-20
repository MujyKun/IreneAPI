CREATE OR REPLACE VIEW groupmembers.getcompanies AS
    SELECT companyid, name, description, dateid FROM groupmembers.company;