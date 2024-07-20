create or replace function public.addstats(t_name text, t_value bigint)
    returns void
    language plpgsql
as
$$
begin

    INSERT INTO public.stats(name, value)
    VALUES(t_name, t_value);
end;
$$;
