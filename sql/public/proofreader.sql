create table IF NOT EXISTS proofreader
(
    userid bigint
        constraint proofreader_pk
            primary key
);

comment on table proofreader is 'Users who are a proofreader.';