CREATE TABLE IF NOT EXISTS public.commandusage
(
    sessionid integer,
    commandname text,
    count integer,
    PRIMARY KEY (sessionid, commandname),
    CONSTRAINT commandusage_sessionid FOREIGN KEY (sessionid) REFERENCES public.sessions(sessionid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.commandusage
    OWNER to postgres;
COMMENT ON TABLE public.commandusage
    IS 'The usage of every command during a session.';