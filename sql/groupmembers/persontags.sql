create table if not exists groupmembers.persontags
(
    tagid   int,
    personid int,
    primary key (tagid, personid),
    CONSTRAINT p_tags_tag_id FOREIGN KEY (tagid) REFERENCES groupmembers.tags(tagid) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT tags_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE groupmembers.persontags
    OWNER to postgres;
COMMENT ON TABLE groupmembers.persontags
    IS 'The tags for persons.';