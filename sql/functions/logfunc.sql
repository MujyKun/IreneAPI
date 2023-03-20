create or replace function public.logfunc(t_userid bigint, t_func text, t_response text, t_args text, t_kwargs text)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO public.apiusage(userid, func, response, args, kwargs)
    VALUES(t_userid, t_func, t_response, t_args, t_kwargs);
end;
$$;