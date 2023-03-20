create or replace function public.getusage(t_userid bigint, t_endpoint text)
    returns integer
    language plpgsql
as
$$
declare
    t_count integer;
begin
    SELECT count into t_count FROM public.apiusage WHERE userid = t_userid AND endpoint = t_endpoint;
    return t_count;
end;
$$;