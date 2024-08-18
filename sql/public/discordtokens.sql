CREATE TABLE IF NOT EXISTS public.discordtokens (
	session_id text NOT NULL,
	access_token text NOT NULL,
	refresh_token text NOT NULL,
	expires_at timestamp NOT NULL,
	"scope" text NOT NULL,
	CONSTRAINT sessionid PRIMARY KEY (session_id)
);

COMMENT ON COLUMN public.discordtokens.session_id IS 'The cookies';

ALTER TABLE public.discordtokens
    OWNER to postgres;