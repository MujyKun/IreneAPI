CREATE OR REPLACE VIEW groupmembers.getgroupaliases AS
    SELECT aliasid, alias, groupid, guildid FROM groupmembers.groupaliases;