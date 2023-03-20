create or replace function public.deletepersonalias(t_aliasid integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.personaliases WHERE aliasid = t_aliasid;
end;
$$;
