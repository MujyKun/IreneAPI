CREATE TABLE IF NOT EXISTS public.reminders
(
    id serial,
    userid bigint,
    reason text,
    dateid integer,
    PRIMARY KEY (id),
    CONSTRAINT reminders_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT reminders_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.reminders
    OWNER to postgres;
COMMENT ON TABLE public.reminders
    IS 'All reminders that have or will be sent to a user.';