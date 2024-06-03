create table IF NOT EXISTS patron
(
    userid bigint
        constraint patron_pk
            primary key,
    CONSTRAINT patron_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

comment on table patron is 'Users who are a patron.';

