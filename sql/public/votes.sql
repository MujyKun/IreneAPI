CREATE TABLE IF NOT EXISTS public.votes
(
    votedat timestamp without time zone,
    userid bigint,
    PRIMARY KEY (votedat, userid),
    CONSTRAINT votes_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.votes
    OWNER to postgres;