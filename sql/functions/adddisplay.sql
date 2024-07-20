create or replace function groupmembers.adddisplay(t_avatar text, t_banner text)
    returns integer
    language plpgsql
as
$$
declare
    t_display_id integer;
begin

    INSERT INTO groupmembers.displays(avatar, banner)
    VALUES(t_avatar, t_banner) returning displayid INTO t_display_id;
    return t_display_id;
end;
$$;