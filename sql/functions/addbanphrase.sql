create or replace function public.addbanphrase(t_guildid bigint,
                                t_logchannelid bigint, t_phrase text, t_punishment text)
    returns integer
    language plpgsql
as
$$
declare
    t_phrase_id integer;
begin

    INSERT INTO public.banphrases(guildid, logchannelid, phrase, punishment)
    VALUES(t_guildid, t_logchannelid, t_phrase, t_punishment) returning phraseid INTO t_phrase_id;
    return t_phrase_id;
end;
$$;