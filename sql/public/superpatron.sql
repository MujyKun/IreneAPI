create table IF NOT EXISTS superpatron
(
    userid bigint
        constraint superpatron_pk
            primary key
);

comment on table superpatron is 'Users who are a super patron.';

