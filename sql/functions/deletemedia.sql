create or replace function groupmembers.deletemedia(t_media_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.media WHERE mediaid = t_media_id;
end;
$$;
