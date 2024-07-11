create table if not exists groupmembers.grouptags
(
    tagid   int,
    groupid int,
    primary key (tagid, groupid)
);

ALTER TABLE groupmembers.grouptags
    OWNER to postgres;
COMMENT ON TABLE groupmembers.grouptags
    IS 'The tags for groups.';