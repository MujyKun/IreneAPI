create or replace function public.addcommandusage(t_sessionid integer, t_commandname text)
    returns integer
    language plpgsql
as
$$
declare
    t_old_count integer;
begin
    SELECT count INTO t_old_count FROM public.commandusage WHERE sessionid = t_sessionid AND commandname = t_commandname;

    IF t_old_count is null THEN
        INSERT INTO public.commandusage(sessionid, commandname, count)
        VALUES(t_sessionid, t_commandname, 1);
        return 1;
    ELSE
        UPDATE public.commandusage SET count = t_old_count + 1 WHERE sessionid = t_sessionid AND commandname = t_commandname;
        return t_old_count + 1;
    END IF;
end;
$$;