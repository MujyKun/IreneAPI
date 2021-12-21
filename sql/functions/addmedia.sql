create or replace function groupmembers.addmedia(t_link text, t_faces integer, t_filetype text, t_affiliationid integer, t_enabled boolean)
    returns integer
    language plpgsql
as
$$
declare
    t_media_id integer;
begin

    INSERT INTO groupmembers.media(link, faces, filetype, affiliationid, enabled)
    VALUES(t_link, t_faces, t_filetype, t_affiliationid, t_enabled) returning mediaid INTO t_media_id;
    return t_media_id;
end;
$$;