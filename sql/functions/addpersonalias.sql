create or replace function groupmembers.addpersonalias(t_alias text, t_personid integer, t_guildid bigint)
    returns integer
    language plpgsql
as
$$
declare
    t_alias_id integer;
begin

    INSERT INTO groupmembers.personaliases(alias, personid, guildid)
    VALUES(t_alias, t_personid, t_guildid) returning aliasid INTO t_alias_id;
    return t_alias_id;
end;
$$;
