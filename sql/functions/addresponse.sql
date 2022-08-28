create or replace function public.addresponse(t_response text)
    returns integer
    language plpgsql
as
$$
declare
    t_response_id integer;
begin

    INSERT INTO public.eightball(response)
    VALUES(t_response) returning responseid INTO t_response_id;
    return t_response_id;
end;
$$;
