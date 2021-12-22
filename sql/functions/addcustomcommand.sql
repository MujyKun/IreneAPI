create or replace function public.addcustomcommand(t_guildid bigint, t_name text, t_content text)
    returns integer
    language plpgsql
as
$$
declare
    t_commandid integer;
begin
    INSERT INTO public.customcommands(guildid, name, content)
    VALUES (t_guildid, t_name, t_content) RETURNING commandid INTO t_commandid;
    return t_commandid;
end;
$$;