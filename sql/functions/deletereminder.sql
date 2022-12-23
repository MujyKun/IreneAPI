create or replace function public.deletereminder(t_remind_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.reminders WHERE id = t_remind_id;
end;
$$;
