CREATE TABLE IF NOT EXISTS groupmembers.groupaliases
(
    aliasid serial,
    alias text,
    groupid integer,
    guildid bigint,
    PRIMARY KEY (aliasid),
    CONSTRAINT ensure_groupalias CHECK (alias <> ''),
    CONSTRAINT unique_group_alias UNIQUE (alias, groupid, guildid),
    CONSTRAINT groupaliases_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT groupaliases_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE SET NULL ON UPDATE CASCADE
);

ALTER TABLE groupmembers.groupaliases
    OWNER to postgres;
COMMENT ON TABLE groupmembers.groupaliases
    IS 'The aliases of a group.';