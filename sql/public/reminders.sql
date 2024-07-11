CREATE TABLE IF NOT EXISTS public.reminders
(
    id serial,
    userid bigint,
    reason text,
    startdate timestamp DEFAULT (CURRENT_TIMESTAMP AT TIME ZONE 'UTC'),
    notifydate timestamp,
    PRIMARY KEY (id)
);

ALTER TABLE public.reminders
    OWNER to postgres;
COMMENT ON TABLE public.reminders
    IS 'All reminders that have or will be sent to a user.';