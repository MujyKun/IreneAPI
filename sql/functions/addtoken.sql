create or replace function public.addtoken(t_userid bigint, t_hashed text, t_accessid integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO public.apitokens(userid, hashed, accessid)
    VALUES(t_userid, t_hashed, t_accessid);
end;
$$;