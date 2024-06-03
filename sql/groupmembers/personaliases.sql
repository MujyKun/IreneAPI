CREATE TABLE IF NOT EXISTS groupmembers.personaliases
(
    aliasid serial,
    alias text,
    personid integer,
    guildid bigint,
    PRIMARY KEY (aliasid),
    CONSTRAINT ensure_personalias CHECK (alias <> ''),
    constraint unique_person_alias UNIQUE (alias, personid, guildid),
    constraint personaliases_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT personaliases_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE groupmembers.personaliases
    OWNER to postgres;
COMMENT ON TABLE groupmembers.personaliases
    IS 'The aliases of a person.';