CREATE TABLE IF NOT EXISTS groupmembers.personaliases
(
    aliasid serial,
    alias text,
    personid integer,
    guildid bigint,
    PRIMARY KEY (aliasid),
    UNIQUE (alias, personid, guildid)
);

ALTER TABLE groupmembers.personaliases
    OWNER to postgres;
COMMENT ON TABLE groupmembers.personaliases
    IS 'The aliases of a person.';