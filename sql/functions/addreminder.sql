create or replace function public.addreminder(t_user_id bigint, t_reason text, t_date_id integer)
    returns integer
    language plpgsql
as
$$
declare
    t_remind_id integer;
begin

    INSERT INTO public.reminders(userid, reason, dateid)
    VALUES(t_user_id, t_reason, t_date_id) returning id INTO t_remind_id;
    return t_remind_id;
end;
$$;