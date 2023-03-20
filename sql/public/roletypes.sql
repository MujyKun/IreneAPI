CREATE TABLE IF NOT EXISTS public.roletypes
(
    typeid serial,
    name text,
    PRIMARY KEY (typeid)
);

ALTER TABLE public.roletypes
    OWNER to postgres;
COMMENT ON TABLE public.roletypes
    IS 'The types of role (ex: muted, patron, super patron, mod, data mod)';