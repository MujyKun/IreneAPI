create table IF NOT EXISTS patron
(
    userid bigint
        constraint patron_pk
            primary key
);

comment on table patron is 'Users who are a patron.';

