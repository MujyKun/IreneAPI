create or replace function public.updateuserstatus(t_status_id integer, t_score int)
    returns void
    language plpgsql
as
$$
begin
    UPDATE public.userstatus SET score = t_score WHERE statusid = t_status_id;
end;
$$;