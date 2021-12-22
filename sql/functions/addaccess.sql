create or replace function public.addaccess(t_name text)
    returns integer
    language plpgsql
as
$$
declare
    t_id integer;
begin

    INSERT INTO public.apiaccess(name)
    VALUES(t_name) returning accessid INTO t_id;
    return t_id;
end;
$$;