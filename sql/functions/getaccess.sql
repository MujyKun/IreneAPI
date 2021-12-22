create or replace function public.getaccess(t_userid bigint)
    returns text
    language plpgsql
as
$$
declare
    t_access text;
begin
    SELECT name INTO t_access FROM public.apiaccess aa, public.apitokens at WHERE userid = t_userid AND aa.accessid = at.accessid;
    return t_access;
end;
$$