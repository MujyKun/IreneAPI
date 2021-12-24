create or replace function public.addaccess(t_name text)
    returns integer
    language plpgsql
as
$$
declare
    t_id integer;
begin

    INSERT INTO public.apiaccess(name)
    VALUES(t_name) returning accessid INTO t_id;
    return t_id;
end;
$$;create or replace function groupmembers.addaffiliation(t_personid integer, t_groupid integer, t_position_ids integer[],
                                                       t_stagename text)
    returns integer
    language plpgsql
as
$$
declare
    t_affiliation_id integer;
begin

    INSERT INTO groupmembers.affiliation(personid, groupid, positionids, stagename)
    VALUES(t_personid, t_groupid, t_position_ids, t_stagename) returning affiliationid INTO t_affiliation_id;
    return t_affiliation_id;
end;
$$;


create or replace function groupmembers.addautomedia(t_channel_id bigint, t_personids integer[])
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO groupmembers.automedia(channelid, personids)
    VALUES(t_channel_id, t_personids);
end;
$$;create or replace function public.addchannel(t_channelid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_channel_exists integer;
begin
    SELECT COUNT(*) INTO t_channel_exists FROM public.channels WHERE t_channelid = channelid;

    IF t_channel_exists = 0 THEN
        INSERT INTO public.channels(channelid)
        VALUES(t_channelid);
    END IF;
end;
$$;create or replace function public.addcommandusage(t_sessionid integer, t_commandname text)
    returns integer
    language plpgsql
as
$$
declare
    t_old_count integer;
begin
    SELECT count INTO t_old_count FROM public.commandusage WHERE sessionid = t_sessionid AND commandname = t_commandname;

    IF t_old_count is null THEN
        INSERT INTO public.commandusage(sessionid, commandname, count)
        VALUES(t_sessionid, t_commandname, 1);
        return 1;
    ELSE
        UPDATE public.commandusage SET count = t_old_count + 1 WHERE sessionid = t_sessionid AND commandname = t_commandname;
        return t_old_count + 1;
    END IF;
end;
$$;create or replace function groupmembers.addcompany(t_name text, t_description text, t_dateid integer)
    returns integer
    language plpgsql
as
$$
declare
    t_company_id integer;
begin

    INSERT INTO groupmembers.company(name, description, dateid)
    VALUES(t_name, t_description, t_dateid) returning companyid INTO t_company_id;
    return t_company_id;
end;
$$;
create or replace function public.addcustomcommand(t_guildid bigint, t_name text, t_content text)
    returns integer
    language plpgsql
as
$$
declare
    t_commandid integer;
begin
    INSERT INTO public.customcommands(guildid, name, content)
    VALUES (t_guildid, t_name, t_content) RETURNING commandid INTO t_commandid;
    return t_commandid;
end;
$$;create or replace function public.adddatamod(t_userid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.datamods WHERE userid = t_userid;

    IF t_already_exists = 0 THEN
        INSERT INTO public.datamods(userid)
        VALUES(t_userid);
    END IF;
end;
$$;create or replace function groupmembers.adddate(t_startdate timestamp, t_enddate timestamp)
    returns integer
    language plpgsql
as
$$
declare
    t_date_id integer;
begin

    INSERT INTO groupmembers.dates(startdate, enddate)
    VALUES(t_startdate, t_enddate) returning dateid INTO t_date_id;
    return t_date_id;
end;
$$;create or replace function groupmembers.adddisplay(t_avatar text, t_banner text)
    returns integer
    language plpgsql
as
$$
declare
    t_display_id integer;
begin

    INSERT INTO groupmembers.display(avatar, banner)
    VALUES(t_avatar, t_banner) returning displayid INTO t_display_id;
    return t_display_id;
end;
$$;create or replace function groupmembers.addfandom(t_groupid bigint, t_name text)
    returns void
    language plpgsql
as
$$
begin

    INSERT INTO groupmembers.fandom(groupid, name)
    VALUES(t_groupid, t_name);
end;
$$;create or replace function groupmembers.addgroup(t_name text, t_dateid integer, t_description text, t_companyid integer,
                                                 t_displayid integer, t_website text, t_socialid integer, t_tagids integer[])
    returns integer
    language plpgsql
as
$$
declare
    t_group_id integer;
begin

    INSERT INTO groupmembers.groups(name, dateid, description, companyid, displayid, website, socialid, tagids)
    VALUES(t_name, t_dateid, t_description, t_companyid, t_displayid, t_website, t_socialid, t_tagids) returning groupid INTO t_group_id;
    return t_group_id;
end;
$$;create or replace function groupmembers.addgroupalias(t_alias text, t_groupid integer, t_guildid bigint)
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
create or replace function public.addguildprefix(t_guildid bigint, t_prefix text)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.guildprefixes WHERE guildid = t_guildid;
    IF t_already_exists = 0 THEN
        INSERT INTO public.guildprefixes(guildid, prefix)
        VALUES(t_guildid, t_prefix);
    ELSE
        UPDATE public.guildprefixes SET prefix = t_prefix WHERE guildid = t_guildid;
    END IF;
end;
$$;create or replace function groupmembers.addlocation(t_country text, t_city text)
    returns integer
    language plpgsql
as
$$
declare
    t_location_id integer;
begin

    INSERT INTO groupmembers.location(country, city)
    VALUES(t_country, t_city) returning locationid INTO t_location_id;
    return t_location_id;
end;
$$;create or replace function groupmembers.addmedia(t_link text, t_faces integer, t_filetype text, t_affiliationid integer, t_enabled boolean)
    returns integer
    language plpgsql
as
$$
declare
    t_media_id integer;
begin

    INSERT INTO groupmembers.media(link, faces, filetype, affiliationid, enabled)
    VALUES(t_link, t_faces, t_filetype, t_affiliationid, t_enabled) returning mediaid INTO t_media_id;
    return t_media_id;
end;
$$;create or replace function public.addmod(t_userid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.mods WHERE userid = t_userid;

    IF t_already_exists = 0 THEN
        INSERT INTO public.mods(userid)
        VALUES(t_userid);
    END IF;
end;
$$;create or replace function groupmembers.addname(t_firstname text, t_lastname text)
    returns integer
    language plpgsql
as
$$
declare
    t_name_id integer;
begin

    INSERT INTO groupmembers.name(firstname, lastname)
    VALUES(t_firstname, t_lastname) returning nameid INTO t_name_id;
    return t_name_id;
end;
$$;create or replace function public.addpatron(t_userid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.patron WHERE userid = t_userid;

    IF t_already_exists = 0 THEN
        INSERT INTO public.patron(userid)
        VALUES(t_userid);
    END IF;
end;
$$;create or replace function groupmembers.addperson(t_dateid integer, t_nameid integer, t_formernameid integer,
                                                  t_gender character(1), t_description text, t_height integer, t_displayid integer, t_socialid integer,
                                                  t_locationid integer, t_tagids integer[], t_bloodid integer, t_callcount integer)
    returns integer
    language plpgsql
as
$$
declare
    t_person_id integer;
begin

    INSERT INTO groupmembers.person(dateid, nameid, formernameid, gender, description, height, displayid, socialid,
                                    locationid, tagids, bloodid, callcount)
    VALUES (t_dateid, t_nameid, t_formernameid, t_gender, t_description, t_height,
            t_displayid, t_socialid, t_locationid, t_tagids, t_bloodid, t_callcount) returning personid INTO t_person_id;
    return t_person_id;
end;
$$;create or replace function groupmembers.addpersonalias(t_alias text, t_personid integer, t_guildid bigint)
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
create or replace function groupmembers.addposition(t_name text)
    returns integer
    language plpgsql
as
$$
declare
    t_position_id integer;
begin

    INSERT INTO groupmembers.position(name)
    VALUES(t_name) returning positionid INTO t_position_id;
    return t_position_id;
end;
$$;create or replace function public.addproofreader(t_userid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.proofreader WHERE userid = t_userid;

    IF t_already_exists = 0 THEN
        INSERT INTO public.proofreader(userid)
        VALUES(t_userid);
    END IF;
end;
$$;create or replace function groupmembers.addsocials(t_twitter text, t_youtube text, t_melon text, t_instagram text,
    t_vlive text, t_spotify text, t_fancafe text, t_facebook text, t_tiktok text)
    returns integer
    language plpgsql
as
$$
declare
    t_social_id integer;
begin

    INSERT INTO groupmembers.socialmedia(twitter, youtube, melon, instagram, vlive, spotify, fancafe, facebook, tiktok)
    VALUES(t_twitter, t_youtube, t_melon, t_instagram, t_vlive, t_spotify, t_fancafe, t_facebook, t_tiktok) returning socialid INTO t_social_id;
    return t_social_id;
end;
$$;create or replace function public.addsuperpatron(t_userid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.superpatron WHERE userid = t_userid;

    IF t_already_exists = 0 THEN
        INSERT INTO public.superpatron(userid)
        VALUES(t_userid);
    END IF;
end;
$$;create or replace function groupmembers.addtag(t_name text)
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
create or replace function public.addtoken(t_userid bigint, t_hashed text, t_accessid integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO public.apitokens(userid, hashed, accessid)
    VALUES(t_userid, t_hashed, t_accessid);
end;
$$;create or replace function public.addtranslator(t_userid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.translator WHERE userid = t_userid;

    IF t_already_exists = 0 THEN
        INSERT INTO public.translator(userid)
        VALUES(t_userid);
    END IF;
end;
$$;create or replace function public.addusage(t_userid bigint, t_endpoint text)
    returns integer
    language plpgsql
as
$$
declare
    t_old_count integer;
begin
    SELECT count INTO t_old_count FROM public.apiusage WHERE userid = t_userid AND endpoint = t_endpoint;

    IF t_old_count is null THEN
        INSERT INTO public.apiusage(userid, endpoint, count)
        VALUES(t_userid, t_endpoint, 1);
        return 1;
    ELSE
        UPDATE public.apiusage SET count = t_old_count + 1 WHERE userid = t_userid AND endpoint = t_endpoint;
        return t_old_count + 1;
    END IF;
end;
$$;create or replace function public.botban(t_userid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_user_banned integer;
begin
    SELECT COUNT(*) INTO t_user_banned FROM public.botbanned WHERE userid = t_userid;

    IF t_user_banned = 1 THEN
        INSERT INTO public.botbanned(userid)
        VALUES(t_userid);
    END IF;
end;
$$;
create or replace function public.botunban(t_userid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_user_banned integer;
begin
    SELECT COUNT(*) INTO t_user_banned FROM public.botbanned WHERE userid = t_userid;

    IF t_user_banned = 1 THEN
        DELETE FROM public.botbanned WHERE user = t_userid;
    END IF;
end;
$$;create or replace function public.deletecustomcommand(t_guildid bigint, t_name text)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.customcommands WHERE guildid = t_guildid AND name = t_name;
end;
$$;create or replace function public.deletecustomcommandbyid(t_commandid integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.customcommands WHERE commandid = t_commandid;
end;
$$;create or replace function public.deletedatamod(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.datamods WHERE userid = t_userid;
end;
$$;
create or replace function public.deletemod(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.mods WHERE userid = t_userid;
end;
$$;
create or replace function public.deletepatron(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.patron WHERE userid = t_userid;
end;
$$;
create or replace function public.deleteproofreader(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.proofreader WHERE userid = t_userid;
end;
$$;create or replace function public.deletesuperpatron(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.superpatron WHERE userid = t_userid;
end;
$$;create or replace function public.deletetranslator(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.translator WHERE userid = t_userid;
end;
$$;create or replace function public.getaccess(t_userid bigint)
    returns text
    language plpgsql
as
$$
declare
    t_access text;
begin
    SELECT name INTO t_access FROM public.apiaccess aa, public.apitokens at WHERE userid = t_userid AND aa.accessid = at.accessid;
    return t_access;
end;
$$;create or replace function groupmembers.getaffiliation(t_affiliation_id integer)
    returns table
            (
                t_personid integer,
                t_groupid integer,
                t_positionids integer[],
                t_stagename text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT personid, groupid, positionids, stagename
                 FROM groupmembers.affiliation
                 WHERE affiliationid = t_affiliation_id;
end;
$$;create or replace function groupmembers.getbloodtype(t_blood_id integer)
    returns table
            (
                t_name text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT name
                 FROM groupmembers.bloodtypes
                 WHERE t_blood_id = bloodid;
end;
$$;create or replace function public.getcommandusage(t_sessionid integer, t_commandname text)
    returns integer
    language plpgsql
as
$$
declare
    t_count integer;
begin
    SELECT count into t_count FROM public.commandusage WHERE sessionid = t_sessionid AND commandname = t_commandname;
    return t_count;
end;
$$;create or replace function groupmembers.getcompany(t_company_id integer)
    returns table
            (
                t_name text,
                t_description text,
                t_dateid integer
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT name, description, dateid
                 FROM groupmembers.company
                 WHERE companyid = t_company_id;
end;
$$;create or replace function groupmembers.getdate(t_dateid integer)
    returns table
            (
                t_startdate timestamp,
                t_enddate timestamp
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT startdate, enddate
                 FROM groupmembers.dates
                 WHERE dateid = t_dateid;
end;
$$;
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
$$;create or replace function groupmembers.getfandom(t_groupid integer)
    returns table
            (
                t_name text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT name
                 FROM groupmembers.fandom
                 WHERE t_groupid = groupid;
end;
$$;create or replace function groupmembers.getgroup(t_group_id integer)
    returns table
            (
                t_name        text,
                t_dateid      integer,
                t_description text,
                t_companyid   integer,
                t_displayid   integer,
                t_website     text,
                t_socialid    integer,
                t_tagids      integer[]
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT name, dateid, description, companyid, displayid, website, socialid, tagids
                 FROM groupmembers.groups
                 WHERE groupid = t_group_id;
end;
$$;create or replace function groupmembers.getgroupalias(t_aliasid integer)
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
$$;create or replace function groupmembers.getgroupaliases(t_groupid integer)
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
$$;create or replace function groupmembers.getlocation(t_locationid integer)
    returns table
            (
                t_country text,
                t_city integer
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT country, city
                 FROM groupmembers.location
                 WHERE locationid = t_locationid;
end;
$$;
create or replace function groupmembers.getmedia(t_mediaid integer)
    returns table
            (
                t_link text,
                t_faces integer,
                t_filetype text,
                t_affiliationid integer,
                t_enabled boolean
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT link, faces, filetype, affiliationid, enabled
                 FROM groupmembers.media
                 WHERE mediaid = t_mediaid;
end;
$$;create or replace function groupmembers.getname(t_nameid integer)
    returns table
            (
                t_firstname text,
                t_lastname text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT firstname, lastname
                 FROM groupmembers.name
                 WHERE t_nameid = nameid;
end;
$$;create or replace function groupmembers.getperson(t_person_id integer)
    returns table (
                      t_dateid integer,
                      t_nameid integer,
                      t_formernameid integer,
                      t_gender char,
                      t_description text,
                      t_height integer,
                      t_displayid integer,
                      t_socialid integer,
                      t_locationid integer,
                      t_tagids integer[],
                      t_bloodid integer,
                      t_callcount integer)
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT person.dateid, nameid, formernameid, gender, description, height, displayid, socialid,
                        locationid, tagids, bloodid, callcount
                 FROM groupmembers.person
                 WHERE personid = t_person_id;
end;
$$;create or replace function groupmembers.getpersonalias(t_aliasid integer)
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
$$;create or replace function groupmembers.getpersonaliases(t_personid integer)
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
$$;create or replace function groupmembers.getposition(t_positionid integer)
    returns table
            (
                t_name text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT name
                 FROM groupmembers.position
                 WHERE positionid = t_positionid;
end;
$$;create or replace function groupmembers.getpositionid(t_positionname text)
    returns table
            (
                t_positionid integer
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT positionid
                 FROM groupmembers.position
                 WHERE name = t_positionname;
end;
$$;create or replace function groupmembers.getsocials(t_socialid integer)
    returns table
            (
                t_twitter text,
                t_youtube text,
                t_melon text,
                t_instagram text,
                t_vlive text,
                t_spotify text,
                t_fancafe text,
                t_facebook text,
                t_tiktok text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT twitter, youtube, melon, instagram, vlive, spotify, fancafe, facebook, tiktok
                 FROM groupmembers.socialmedia
                 WHERE socialid = t_socialid;
end;
$$;
create or replace function groupmembers.gettag(t_tagid integer)
    returns table
            (
                t_name text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT name
                 FROM groupmembers.tag
                 WHERE tagid = t_tagid;
end;
$$;create or replace function groupmembers.gettagid(t_tagname text)
    returns table
            (
                t_tagid integer
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT tagid
                 FROM groupmembers.tag
                 WHERE name = t_tagname;
end;
$$;create or replace function public.gettoken(t_userid bigint)
    returns text
    language plpgsql
as
$$
declare
    t_hashed text;
begin
    SELECT hashed into t_hashed FROM public.apitokens WHERE userid = t_userid;
    return t_hashed;
end;
$$;create or replace function public.getusage(t_userid bigint, t_endpoint text)
    returns integer
    language plpgsql
as
$$
declare
    t_count integer;
begin
    SELECT count into t_count FROM public.apiusage WHERE userid = t_userid AND endpoint = t_endpoint;
    return t_count;
end;
$$;