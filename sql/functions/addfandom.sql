create or replace function groupmembers.addfandom(t_groupid bigint, t_name text)
    returns void
    language plpgsql
as
$$
begin

    INSERT INTO groupmembers.fandom(groupid, name)
    VALUES(t_groupid, t_name);
end;
$$;