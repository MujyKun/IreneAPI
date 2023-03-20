create or replace function public.deleteuserstatus(t_status_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.userstatus WHERE statusid = t_status_id;
end;
$$;
