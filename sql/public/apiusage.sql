CREATE TABLE IF NOT EXISTS public.apiusage
(
    time timestamp NOT NULL DEFAULT now(),
    userid bigint NOT NULL,
    func text NOT NULL,
    response text,
    args text,
    kwargs text,
    PRIMARY KEY (time, func, userid),
    CONSTRAINT usage_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.apiusage
    OWNER to postgres;
COMMENT ON TABLE public.apiusage
    IS 'The usage a user has to each api function..';