create or replace function public.adduserstatus(t_user_id bigint, t_score int)
    returns integer
    language plpgsql
as
$$
declare
    t_status_id integer;
begin

    INSERT INTO public.userstatus(userid, score)
    VALUES(t_user_id, t_score) returning statusid INTO t_status_id;
    return t_status_id;
end;
$$;