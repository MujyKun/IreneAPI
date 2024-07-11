CREATE TABLE IF NOT EXISTS groupmembers.groupaliases
(
    aliasid serial,
    alias text,
    groupid integer,
    guildid bigint,
    PRIMARY KEY (aliasid),
    UNIQUE (alias, groupid, guildid)
);

ALTER TABLE groupmembers.groupaliases
    OWNER to postgres;
COMMENT ON TABLE groupmembers.groupaliases
    IS 'The aliases of a group.';