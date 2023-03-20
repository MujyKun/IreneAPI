CREATE TABLE IF NOT EXISTS public.reactionroles
(
    messageid bigint,
    PRIMARY KEY (messageid)
);

ALTER TABLE public.reactionroles
    OWNER to postgres;
COMMENT ON TABLE public.customcommands
    IS 'Message IDs containing reaction roles.';
