create table if not exists groupmembers.grouptags
(
    tagid   int,
    groupid int,
    primary key (tagid, groupid),
    CONSTRAINT tags_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT tags_tag_id FOREIGN KEY (tagid) REFERENCES groupmembers.tags(tagid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE groupmembers.grouptags
    OWNER to postgres;
COMMENT ON TABLE groupmembers.grouptags
    IS 'The tags for groups.';