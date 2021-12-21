create or replace function groupmembers.addgroupalias(t_alias text, t_groupid integer, t_guildid bigint)
    returns integer
    language plpgsql
as
$$
declare
    t_alias_id integer;
begin

    INSERT INTO groupmembers.groupaliases(alias, groupid, guildid)
    VALUES(t_alias, t_groupid, t_guildid) returning aliasid INTO t_alias_id;
    return t_alias_id;
end;
$$;
