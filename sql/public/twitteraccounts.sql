create table IF NOT EXISTS twitteraccounts
(
    accountid       bigint,
    username text,
    PRIMARY KEY (accountid)
);

comment on table twitteraccounts is 'Twitter account usernames associated with their ID.';

