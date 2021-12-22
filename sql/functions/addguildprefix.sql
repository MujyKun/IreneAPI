create or replace function public.addguildprefix(t_guildid bigint, t_prefix text)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.guildprefixes WHERE guildid = t_guildid;
    IF t_already_exists = 0 THEN
        INSERT INTO public.guildprefixes(guildid, prefix)
        VALUES(t_guildid, t_prefix);
    ELSE
        UPDATE public.guildprefixes SET prefix = t_prefix WHERE guildid = t_guildid;
    END IF;
end;
$$;