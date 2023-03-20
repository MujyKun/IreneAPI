CREATE OR REPLACE VIEW groupmembers.getnames AS
    SELECT nameid, firstname, lastname FROM groupmembers.name;