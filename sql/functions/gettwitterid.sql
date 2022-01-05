create or replace function public.gettwitterid(t_username text)
    returns table
            (
                t_accountid bigint
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT accountid FROM public.twitteraccounts WHERE t_username = username;
end;
$$;