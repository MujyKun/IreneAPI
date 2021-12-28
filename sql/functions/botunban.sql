create or replace function public.botunban(t_userid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_user_banned integer;
begin
    SELECT COUNT(*) INTO t_user_banned FROM public.botbanned WHERE userid = t_userid;

    IF t_user_banned = 1 THEN
        DELETE FROM public.botbanned
        WHERE userid = t_userid;
    END IF;
end;
$$;