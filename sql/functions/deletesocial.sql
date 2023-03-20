create or replace function groupmembers.deletesocial(t_social_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.socialmedia WHERE socialid = t_social_id;
end;
$$;
