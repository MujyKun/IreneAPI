create table if not exists groupmembers.persontags
(
    tagid   int,
    personid int,
    primary key (tagid, personid)
);

ALTER TABLE groupmembers.persontags
    OWNER to postgres;
COMMENT ON TABLE groupmembers.persontags
    IS 'The tags for persons.';