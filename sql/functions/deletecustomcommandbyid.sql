create or replace function public.deletecustomcommandbyid(t_commandid integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.customcommands WHERE commandid = t_commandid;
end;
$$;