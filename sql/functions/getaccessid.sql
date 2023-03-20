create or replace function public.getaccessid(t_userid bigint)
    returns integer
    language plpgsql
as
$$
declare
    t_access_id integer;
begin
    SELECT accessid INTO t_access_id FROM public.apitokens WHERE userid = t_userid;
    return t_access_id;
end;
$$;