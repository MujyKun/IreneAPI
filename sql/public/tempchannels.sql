CREATE TABLE IF NOT EXISTS public.tempchannels
(
    channelid bigint,
    delay integer,
    PRIMARY KEY (channelid)
);

ALTER TABLE public.tempchannels
    OWNER to postgres;
COMMENT ON TABLE public.tempchannels
    IS 'A self-destruct channel that removes messages after t seconds.';