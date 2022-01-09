CREATE OR REPLACE VIEW groupmembers.getdisplays AS
    SELECT displayid, avatar, banner FROM groupmembers.display;