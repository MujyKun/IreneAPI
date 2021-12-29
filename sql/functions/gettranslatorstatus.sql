create or replace function public.gettranslatorstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_translator boolean;
begin
    SELECT COUNT(*) INTO t_user_is_translator FROM public.translator WHERE userid = t_userid;
    return t_user_is_translator;
end;
$$;
