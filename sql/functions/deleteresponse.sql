create or replace function public.deleteresponse(t_response_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.eightball WHERE responseid = t_response_id;
end;
$$;