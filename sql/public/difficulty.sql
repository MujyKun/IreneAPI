CREATE TABLE IF NOT EXISTS public.difficulty
(
    difficultyid serial,
    name text UNIQUE,
    PRIMARY KEY (difficultyid)
);

ALTER TABLE public.difficulty
    OWNER to postgres;