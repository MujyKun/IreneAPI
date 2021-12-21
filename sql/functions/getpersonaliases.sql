create or replace function groupmembers.getpersonaliases(t_personid integer)
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
                 FROM groupmembers.personaliases
                 WHERE personid = t_personid;
end;
$$;