create or replace function public.addreactionrole(t_message_id bigint)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO public.reactionroles(messageid) VALUES(t_message_id);
end;
$$;