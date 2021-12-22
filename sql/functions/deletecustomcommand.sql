create or replace function public.deletecustomcommand(t_guildid bigint, t_name text)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.customcommands WHERE guildid = t_guildid AND name = t_name;
end;
$$;