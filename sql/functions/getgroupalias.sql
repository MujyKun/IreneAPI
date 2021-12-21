create or replace function groupmembers.getgroupalias(t_aliasid integer)
    returns table
            (
                t_alias text,
                t_groupid integer,
                t_guildid bigint
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT alias, groupid, guildid
                 FROM groupmembers.groupaliases
                 WHERE aliasid = t_aliasid;
end;
$$;