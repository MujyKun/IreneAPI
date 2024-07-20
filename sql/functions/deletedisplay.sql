create or replace function groupmembers.deletedisplay(t_display_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.displays WHERE displayid = t_display_id;
end;
$$;
