create or replace function public.addbanphrase(t_guildid bigint,
                                t_logchannelid bigint, t_phrase text, t_punishment text)
    returns void
    language plpgsql
as
$$
begin

    INSERT INTO public.banphrases(guildid, logchannelid, phrase, punishment)
    VALUES(t_guildid, t_logchannelid, t_phrase, t_punishment);
end;
$$;