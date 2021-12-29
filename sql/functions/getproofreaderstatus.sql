create or replace function public.getproofreaderstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_proofreader boolean;
begin
    SELECT COUNT(*) INTO t_user_is_proofreader FROM public.proofreader WHERE userid = t_userid;
    return t_user_is_proofreader;
end;
$$;
