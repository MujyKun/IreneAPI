CREATE TABLE IF NOT EXISTS biasgame.winners
(
    personid integer,
    userid bigint,
    wins integer,
    CONSTRAINT bg_personid_userid PRIMARY KEY (personid, userid),
    CONSTRAINT winners_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT winners_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE biasgame.winners
    OWNER to postgres;
COMMENT ON TABLE biasgame.winners
    IS 'The amount of wins a user has on a person.';