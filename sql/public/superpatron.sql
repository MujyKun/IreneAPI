create table IF NOT EXISTS superpatron
(
    userid bigint
        constraint superpatron_pk
            primary key,
    CONSTRAINT super_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

comment on table superpatron is 'Users who are a super patron.';

