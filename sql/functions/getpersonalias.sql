create or replace function groupmembers.getpersonalias(t_aliasid integer)
    returns table
            (
                t_alias text,
                t_personid integer,
                t_guildid bigint
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT alias, personid, guildid
                 FROM groupmembers.personaliases
                 WHERE aliasid = t_aliasid;
end;
$$;