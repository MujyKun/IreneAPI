create or replace function public.deleteprefix(t_guild_id bigint, t_prefix text)
    returns void
    language plpgsql
as
$$
begin

    DELETE FROM public.guildprefixes WHERE guildid = t_guild_id AND prefix = t_prefix;
end;
$$;
