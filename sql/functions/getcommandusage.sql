create or replace function public.getcommandusage(t_sessionid integer, t_commandname text)
    returns integer
    language plpgsql
as
$$
declare
    t_count integer;
begin
    SELECT count into t_count FROM public.commandusage WHERE sessionid = t_sessionid AND commandname = t_commandname;
    return t_count;
end;
$$;