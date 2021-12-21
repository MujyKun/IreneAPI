create or replace function groupmembers.getgroupaliases(t_groupid integer)
    returns table
            (
                t_aliasid integer,
                t_alias text,
                t_guildid bigint
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT aliasid, alias, guildid
                 FROM groupmembers.groupaliases
                 WHERE groupid = t_groupid;
end;
$$;