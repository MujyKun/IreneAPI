create or replace function public.deletegroupalias(t_aliasid integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.groupaliases WHERE aliasid = t_aliasid;
end;
$$;
