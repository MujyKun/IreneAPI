create or replace function public.addtranslator(t_userid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.translator WHERE userid = t_userid;

    IF t_already_exists = 0 THEN
        INSERT INTO public.translator(userid)
        VALUES(t_userid);
    END IF;
end;
$$;