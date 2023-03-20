create or replace function public.getbanstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_banned boolean;
begin
    SELECT COUNT(*) INTO t_user_is_banned FROM public.botbanned WHERE userid = t_userid;
    return t_user_is_banned;
end;
$$;
