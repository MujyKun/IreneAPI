create table IF NOT EXISTS translator
(
    userid bigint
        constraint translator_pk
            primary key,
    CONSTRAINT translator_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

comment on table translator is 'Users who are a translator.';
