create table IF NOT EXISTS translator
(
    userid bigint constraint translator_pk primary key
);

comment on table translator is 'Users who are a translator.';
