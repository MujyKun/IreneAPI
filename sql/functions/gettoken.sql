create or replace function public.gettoken(t_userid bigint)
    returns text
    language plpgsql
as
$$
declare
    t_hashed text;
begin
    SELECT hashed into t_hashed FROM public.apitokens WHERE userid = t_userid;
    return t_hashed;
end;
$$;