create or replace function public.getbotban(t_userid bigint)
    returns integer
    language plpgsql
as
$$
declare
    t_user_banned integer;
begin
    SELECT COUNT(*) INTO t_user_banned FROM public.botbanned WHERE userid = t_userid;
    return t_user_banned;
end;
$$;
