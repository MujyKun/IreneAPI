create or replace function public.gettokenexists(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_token_exists boolean;
begin
    SELECT COUNT(*) INTO t_token_exists FROM public.apitokens WHERE userid = t_userid;
    return t_token_exists;
end;
$$;
