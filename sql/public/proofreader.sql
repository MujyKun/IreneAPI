create table IF NOT EXISTS proofreader
(
    userid bigint
        constraint proofreader_pk
            primary key,
    CONSTRAINT proofreader_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

comment on table proofreader is 'Users who are a proofreader.';