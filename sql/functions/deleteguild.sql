create or replace function public.deleteguild(t_guildid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.guilds WHERE guildid = t_guildid;
end;
$$;
