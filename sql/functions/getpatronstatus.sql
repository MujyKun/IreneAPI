create or replace function public.getpatronstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_patron boolean;
begin
    SELECT COUNT(*) INTO t_user_is_patron FROM public.getpatrons WHERE userid = t_userid;
    return t_user_is_patron;
end;
$$;
