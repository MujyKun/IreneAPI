create or replace function public.getdatamodstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_datamod boolean;
begin
    SELECT COUNT(*) INTO t_user_is_datamod FROM public.datamods WHERE userid = t_userid;
    return t_user_is_datamod;
end;
$$;
