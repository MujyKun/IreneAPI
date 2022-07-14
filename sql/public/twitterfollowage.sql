CREATE TABLE IF NOT EXISTS public.twitterfollowage
(
    accountid bigint,
    channelid bigint,
    roleid bigint,
    posted bool,
    PRIMARY KEY (accountid, channelid)
);

ALTER TABLE public.twitterfollowage
    OWNER to postgres;
COMMENT ON TABLE public.twitterfollowage
    IS 'The discord text channels that are following a Twitter account.';


