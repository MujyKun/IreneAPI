create or replace function groupmembers.getmedia(t_mediaid integer)
    returns table
            (
                t_link text,
                t_faces integer,
                t_filetype text,
                t_affiliationid integer,
                t_enabled boolean
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT link, faces, filetype, affiliationid, enabled
                 FROM groupmembers.media
                 WHERE mediaid = t_mediaid;
end;
$$;