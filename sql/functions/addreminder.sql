create or replace function public.addreminder(t_user_id bigint, t_reason text, t_notify_date timestamp)
    returns integer
    language plpgsql
as
$$
declare
    t_remind_id integer;
begin

    INSERT INTO public.reminders(userid, reason, notifydate)
    VALUES(t_user_id, t_reason, t_notify_date) returning id INTO t_remind_id;
    return t_remind_id;
end;
$$;