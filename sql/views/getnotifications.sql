CREATE OR REPLACE VIEW public.getnotifications AS
    SELECT notiid, guildid, userid, phrase FROM public.notifications;