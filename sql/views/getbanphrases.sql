CREATE OR REPLACE VIEW public.getbanphrases AS
    SELECT phraseid, guildid, logchannelid, phrase, punishment FROM public.banphrases;