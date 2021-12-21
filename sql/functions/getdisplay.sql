create or replace function groupmembers.getdisplay(t_displayid integer)
    returns table
            (
                t_avatar text,
                t_banner text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT avatar, banner
                 FROM groupmembers.display
                 WHERE displayid = t_displayid;
end;
$$;