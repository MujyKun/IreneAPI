create or replace function public.getsuperpatronstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_super_patron boolean;
begin
    SELECT COUNT(*) INTO t_user_is_super_patron FROM public.getsuperpatrons WHERE userid = t_userid;
    return t_user_is_super_patron;
end;
$$;
