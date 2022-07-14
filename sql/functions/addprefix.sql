create or replace function public.addprefix(t_guild_id bigint, t_prefix text)
    returns integer
    language plpgsql
as
$$
begin

    INSERT INTO public.guildprefixes(guildid, prefix) VALUES(t_guild_id, t_prefix);
end;
$$;


