create or replace function public.deletenotification(t_noti_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.notifications WHERE notiid = t_noti_id;
end;
$$;