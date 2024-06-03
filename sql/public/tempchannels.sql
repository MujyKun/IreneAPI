CREATE TABLE IF NOT EXISTS public.tempchannels
(
    channelid bigint,
    delay integer,
    PRIMARY KEY (channelid),
    CONSTRAINT tempchannels_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE public.tempchannels
    OWNER to postgres;
COMMENT ON TABLE public.tempchannels
    IS 'A self-destruct channel that removes messages after t seconds.';