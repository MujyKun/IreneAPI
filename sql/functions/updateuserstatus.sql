create or replace function public.updateuserstatus(t_user_id bigint, t_score int)
    returns void
    language plpgsql
as
$$
begin
    UPDATE public.userstatus SET score = t_score WHERE userid = t_user_id;
end;
$$;