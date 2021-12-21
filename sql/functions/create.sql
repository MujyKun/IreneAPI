create or replace function groupmembers.addaffiliation(t_personid integer, t_groupid integer, t_position_ids integer[],
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
create or replace function groupmembers.adddate(t_startdate timestamp, t_enddate timestamp)
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
create or replace function groupmembers.addlocation(t_country text, t_city text)
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
create or replace function groupmembers.addsocials(t_twitter text, t_youtube text, t_melon text, t_instagram text,
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
$$;