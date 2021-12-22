create or replace function public.addusage(t_userid bigint, t_endpoint text)
    returns integer
    language plpgsql
as
$$
declare
    t_old_count integer;
begin
    SELECT count INTO t_old_count FROM public.apiusage WHERE userid = t_userid AND endpoint = t_endpoint;

    IF t_old_count is null THEN
        INSERT INTO public.apiusage(userid, endpoint, count)
        VALUES(t_userid, t_endpoint, 1);
        return 1;
    ELSE
        UPDATE public.apiusage SET count = t_old_count + 1 WHERE userid = t_userid AND endpoint = t_endpoint;
        return t_old_count + 1;
    END IF;
end;
$$;