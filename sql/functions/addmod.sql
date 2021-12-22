create or replace function public.addmod(t_userid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.mods WHERE userid = t_userid;

    IF t_already_exists = 0 THEN
        INSERT INTO public.mods(userid)
        VALUES(t_userid);
    END IF;
end;
$$;