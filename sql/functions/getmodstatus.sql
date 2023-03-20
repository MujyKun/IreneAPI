create or replace function public.getmodstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_mod boolean;
begin
    SELECT COUNT(*) INTO t_user_is_mod FROM public.mods WHERE userid = t_userid;
    return t_user_is_mod;
end;
$$;
