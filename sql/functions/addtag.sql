create or replace function groupmembers.addtag(t_name text)
    returns integer
    language plpgsql
as
$$
declare
    t_tag_id integer;
begin

    INSERT INTO groupmembers.tag(name)
    VALUES(t_name) returning tagid INTO t_tag_id;
    return t_tag_id;
end;
$$;
