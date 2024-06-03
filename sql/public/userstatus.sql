CREATE TABLE IF NOT EXISTS userstatus
(
    statusid serial,
    userid bigint,
    score integer,
    PRIMARY KEY (statusid, userid),
    CONSTRAINT gg_userstatus_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT us_userstatus_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE userstatus
    OWNER to postgres;
COMMENT ON TABLE userstatus
    IS 'The status of a user during a specific game.';