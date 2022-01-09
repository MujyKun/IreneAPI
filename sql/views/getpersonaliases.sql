CREATE OR REPLACE VIEW groupmembers.getpersonaliases AS
    SELECT aliasid, alias, personid, guildid FROM groupmembers.personaliases;