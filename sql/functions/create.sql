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


create or replace function groupmembers.addautomedia(t_channel_id bigint, t_aff_id integer, t_hours_after integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO groupmembers.automedia(channelid, affiliationid, hoursafter)
    VALUES(t_channel_id, t_aff_id, t_hours_after) ON CONFLICT DO NOTHING;
end;
$$;create or replace function groupmembers.addbloodtype(t_name text)
    returns integer
    language plpgsql
as
$$
declare
    t_blood_id integer;
begin

    INSERT INTO groupmembers.bloodtypes(name)
    VALUES(t_name) returning bloodid INTO t_blood_id;
    return t_blood_id;
end;
$$;


create or replace function public.addchannel(t_channelid bigint, t_guildid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_channel_exists integer;
begin
    SELECT COUNT(*) INTO t_channel_exists FROM public.channels WHERE t_channelid = channelid;

    IF t_channel_exists = 0 THEN
        INSERT INTO public.channels(channelid, guildid)
        VALUES(t_channelid, t_guildid);
    END IF;
end;
$$;
create or replace function public.addcommandusage(t_sessionid integer, t_commandname text)
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
    VALUES(t_groupid, t_name) ON CONFLICT DO NOTHING;
end;
$$;create or replace function guessinggame.addgg(t_dateid integer, t_media_ids integer[], t_status_ids integer[],
                                                    t_mode_id integer, t_difficulty_id integer, t_is_nsfw bool)
    returns integer
    language plpgsql
as
$$
declare
    t_gg_id integer;
begin

    INSERT INTO guessinggame.games(dateid, mediaids, statusids, modeid, difficultyid, isnsfw)
    VALUES (t_dateid, t_media_ids, t_status_ids, t_mode_id, t_difficulty_id, t_is_nsfw) returning gameid INTO t_gg_id;
    return t_gg_id;
end;
$$;create or replace function groupmembers.addgroup(t_name text, t_dateid integer, t_description text, t_companyid integer,
                                                 t_displayid integer, t_website text, t_socialid integer)
    returns integer
    language plpgsql
as
$$
declare
    t_group_id integer;
begin

    INSERT INTO groupmembers.groups(name, dateid, description, companyid, displayid, website, socialid)
    VALUES(t_name, t_dateid, t_description, t_companyid, t_displayid, t_website, t_socialid) returning groupid INTO t_group_id;
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
create or replace function groupmembers.addgrouptag(t_tag_id integer, t_group_id integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO groupmembers.grouptags(tagid, groupid) VALUES (t_tag_id, t_group_id) ON CONFLICT DO NOTHING;
end;
$$;create or replace function public.addguild(
            t_guildid bigint,
            t_name text,
            t_emojicount integer,
            t_afktimeout integer,
            t_icon text,
            t_ownerid bigint,
            t_banner text,
            t_description text,
            t_mfalevel integer,
            t_splash text,
            t_nitrolevel integer,
            t_boosts integer,
            t_textchannelcount integer,
            t_voicechannelcount integer,
            t_categorycount integer,
            t_emojilimit integer,
            t_membercount integer,
            t_rolecount integer,
            t_shardid integer,
            t_createdate timestamptz,
            t_hasbot bool)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO public.guilds(guildid,
                              name,
                              emojicount,
                              afktimeout,
                              icon,
                              ownerid,
                              banner,
                              description,
                              mfalevel,
                              splash,
                              nitrolevel,
                              boosts,
                              textchannelcount,
                              voicechannelcount,
                              categorycount,
                              emojilimit,
                              membercount,
                              rolecount,
                              shardid,
                              createdate,
                              hasbot)
    VALUES(t_guildid,
            t_name,
            t_emojicount,
            t_afktimeout,
            t_icon,
            t_ownerid,
            t_banner,
            t_description,
            t_mfalevel,
            t_splash,
            t_nitrolevel,
            t_boosts,
            t_textchannelcount,
            t_voicechannelcount,
            t_categorycount,
            t_emojilimit,
            t_membercount,
            t_rolecount,
            t_shardid,
            t_createdate,
            t_hasbot) ON CONFLICT (guildid) DO NOTHING;
end;
$$;create or replace function public.addguildprefix(t_guildid bigint, t_prefix text)
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
$$;create or replace function interactions.addinteraction(t_type_id integer, t_url text)
    returns void
    language plpgsql
as
$$
begin

    INSERT INTO interactions.media(url, typeid)
    VALUES(t_url, t_type_id) ON CONFLICT DO NOTHING;
end;
$$;create or replace function interactions.addinteractionmedia(t_url text, type_id integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO interactions.media(url, typeid)
    VALUES(t_url, type_id) ON CONFLICT DO NOTHING;
end;
$$;create or replace function interactions.addinteractiontype(t_name text)
    returns integer
    language plpgsql
as
$$
declare
    t_type_id integer;
begin

    INSERT INTO interactions.interactiontypes(name)
    VALUES(t_name) returning typeid INTO t_type_id;
    return t_type_id;
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
$$;create or replace function groupmembers.addmedia(t_link text, t_faces integer, t_filetype text,
t_affiliationid integer, t_enabled boolean, t_nsfw boolean)
    returns integer
    language plpgsql
as
$$
declare
    t_media_id integer;
begin

    INSERT INTO groupmembers.media(link, faces, filetype, affiliationid, enabled, nsfw)
    VALUES(t_link, t_faces, t_filetype, t_affiliationid, t_enabled, t_nsfw) returning mediaid INTO t_media_id;
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
$$;create or replace function public.addnotification(t_guildid bigint,
                                t_userid bigint, t_phrase text)
    returns integer
    language plpgsql
as
$$
declare
    t_noti_id integer;
begin

    INSERT INTO public.notifications(guildid, userid, phrase)
    VALUES(t_guildid, t_userid, t_phrase) returning notiid INTO t_noti_id;
    return t_noti_id;
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
                                                  t_gender character(1), t_description text, t_height integer,
                                                  t_displayid integer, t_socialid integer, t_locationid integer,
                                                  t_bloodid integer, t_callcount integer)
    returns integer
    language plpgsql
as
$$
declare
    t_person_id integer;
begin

    INSERT INTO groupmembers.person(dateid, nameid, formernameid, gender, description, height, displayid, socialid,
                                    locationid, bloodid, callcount)
    VALUES (t_dateid, t_nameid, t_formernameid, t_gender, t_description, t_height,
            t_displayid, t_socialid, t_locationid, t_bloodid, t_callcount) returning personid INTO t_person_id;

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
create or replace function groupmembers.addpersontag(t_tag_id integer, t_person_id integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO groupmembers.persontags(tagid, personid) VALUES (t_tag_id, t_person_id) ON CONFLICT DO NOTHING;
end;
$$;create or replace function groupmembers.addposition(t_name text)
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
$$;create or replace function public.addprefix(t_guild_id bigint, t_prefix text)
    returns void
    language plpgsql
as
$$
begin

    INSERT INTO public.guildprefixes(guildid, prefix) VALUES(t_guild_id, t_prefix);
end;
$$;


create or replace function public.addproofreader(t_userid bigint)
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
$$;create or replace function public.addreactionrole(t_message_id bigint)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO public.reactionroles(messageid) VALUES(t_message_id);
end;
$$;create or replace function public.addreminder(t_user_id bigint, t_reason text, t_date_id integer)
    returns integer
    language plpgsql
as
$$
declare
    t_remind_id integer;
begin

    INSERT INTO public.reminders(userid, reason, dateid)
    VALUES(t_user_id, t_reason, t_date_id) returning id INTO t_remind_id;
    return t_remind_id;
end;
$$;create or replace function public.addresponse(t_response text)
    returns integer
    language plpgsql
as
$$
declare
    t_response_id integer;
begin

    INSERT INTO public.eightball(response)
    VALUES(t_response) returning responseid INTO t_response_id;
    return t_response_id;
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
$$;create or replace function public.addtwitteraccount(t_accountid bigint, t_username text)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.twitteraccounts WHERE t_accountid = accountid;

    IF t_already_exists = 0 THEN
        INSERT INTO public.twitteraccounts(accountid, username)
        VALUES(t_accountid, t_username);
    END IF;
end;
$$;create or replace function public.addtwittersubscription(t_accountid bigint, t_channelid bigint, t_roleid bigint)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO public.twitterfollowage(accountid, channelid, roleid)
        VALUES(t_accountid, t_channelid, t_roleid) ON CONFLICT DO NOTHING;
end;
$$;
create or replace function unscramblegame.addus(t_dateid integer, t_status_ids integer[], t_mode_id integer,
        t_difficulty_id integer)
    returns integer
    language plpgsql
as
$$
declare
    t_us_id integer;
begin

    INSERT INTO unscramblegame.games(dateid, statusids, modeid, difficultyid)
    VALUES (t_dateid, t_status_ids, t_mode_id, t_difficulty_id) returning gameid INTO t_us_id;
    return t_us_id;
end;
$$;

create or replace function public.addusage(t_userid bigint, t_endpoint text)
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
$$;create or replace function public.adduser(t_userid bigint)
    returns void
    language plpgsql
as
$$
declare
    t_already_exists integer;
begin
    SELECT COUNT(*) INTO t_already_exists FROM public.users WHERE userid = t_userid;

    IF t_already_exists = 0 THEN
        INSERT INTO public.users(userid)
        VALUES(t_userid);
    END IF;
end;
$$;create or replace function public.adduserstatus(t_user_id bigint, t_score int)
    returns integer
    language plpgsql
as
$$
declare
    t_status_id integer;
begin

    INSERT INTO public.userstatus(userid, score)
    VALUES(t_user_id, t_score) returning statusid INTO t_status_id;
    return t_status_id;
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

    IF t_user_banned = 0 THEN
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
        DELETE FROM public.botbanned
        WHERE userid = t_userid;
    END IF;
end;
$$;create or replace function groupmembers.deleteaffiliation(t_affiliation_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.affiliation WHERE affiliationid = t_affiliation_id;
end;
$$;
create or replace function groupmembers.deleteautomedia(t_channel_id bigint, t_aff_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.automedia WHERE channelid = t_channel_id AND affiliationid = t_aff_id;
end;
$$;create or replace function groupmembers.deletebloodtype(t_blood_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.bloodtypes WHERE bloodid = t_blood_id;
end;
$$;
create or replace function groupmembers.deletecompany(t_company_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.company WHERE companyid = t_company_id;
end;
$$;
create or replace function public.deletecustomcommand(t_guildid bigint, t_name text)
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
create or replace function groupmembers.deletedate(t_date_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.dates WHERE dateid = t_date_id;
end;
$$;
create or replace function groupmembers.deletedisplay(t_display_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.display WHERE displayid = t_display_id;
end;
$$;
create or replace function groupmembers.deletefandom(t_group_id integer, t_name text)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.fandom WHERE groupid = t_group_id AND name = t_name ;
end;
$$;create or replace function guessinggame.deletegg(t_gg_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM guessinggame.games WHERE gameid = t_gg_id;
end;
$$;
create or replace function groupmembers.deletegroup(t_group_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.groups WHERE groupid = t_group_id;
end;
$$;
create or replace function public.deletegroupalias(t_aliasid integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.groupaliases WHERE aliasid = t_aliasid;
end;
$$;
create or replace function public.deleteguild(t_guildid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.guilds WHERE guildid = t_guildid;
end;
$$;
create or replace function interactions.deleteinteraction(t_type_id integer, t_url text)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM interactions.media WHERE url=t_url AND typeid=t_type_id;
end;
$$;create or replace function interactions.deleteinteractiontype(t_type_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM interactions.media WHERE typeid = t_type_id;
    DELETE FROM interactions.interactiontypes WHERE typeid = t_type_id;
end;
$$;create or replace function groupmembers.deletelocation(t_location_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.company WHERE companyid = t_company_id;
end;
$$;
create or replace function groupmembers.deletemedia(t_media_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.media WHERE mediaid = t_media_id;
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
create or replace function groupmembers.deletename(t_name_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.name WHERE nameid = t_name_id;
end;
$$;
create or replace function public.deletenotification(t_noti_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.notifications WHERE notiid = t_noti_id;
end;
$$;create or replace function public.deletepatron(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.patron WHERE userid = t_userid;
end;
$$;
create or replace function groupmembers.deleteperson(t_person_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.person WHERE personid  = t_person_id;
end;
$$;
create or replace function public.deletepersonalias(t_aliasid integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.personaliases WHERE aliasid = t_aliasid;
end;
$$;
create or replace function groupmembers.deleteposition(t_position_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.position WHERE positionid = t_position_id;
end;
$$;create or replace function public.deleteprefix(t_guild_id bigint, t_prefix text)
    returns void
    language plpgsql
as
$$
begin

    DELETE FROM public.guildprefixes WHERE guildid = t_guild_id AND prefix = t_prefix;
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
$$;create or replace function public.deletereminder(t_remind_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.reminders WHERE id = t_remind_id;
end;
$$;
create or replace function public.deleteresponse(t_response_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.eightball WHERE responseid = t_response_id;
end;
$$;create or replace function groupmembers.deletesocial(t_social_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.socialmedia WHERE socialid = t_social_id;
end;
$$;
create or replace function public.deletesuperpatron(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.superpatron WHERE userid = t_userid;
end;
$$;create or replace function groupmembers.deletetag(t_tag_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.tag WHERE tagid = t_tag_id;
end;
$$;
create or replace function public.deletetoken(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.apitokens WHERE userid = t_userid;
end;
$$;create or replace function public.deletetranslator(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.translator WHERE userid = t_userid;
end;
$$;create or replace function public.deletetwitteraccount(t_accountid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.twitteraccounts WHERE accountid = t_accountid;
end;
$$;

create or replace function public.deletetwittersubscription(t_accountid bigint, t_channelid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.twitterfollowage WHERE accountid = t_accountid AND channelid = t_channelid;
end;
$$;create or replace function unscramblegame.deleteus(t_us_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM unscramblegame.games WHERE gameid = t_us_id;
end;
$$;
create or replace function public.deleteuser(t_userid bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.users WHERE userid = t_userid;
end;
$$;
create or replace function public.deleteuserstatus(t_status_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.userstatus WHERE statusid = t_status_id;
end;
$$;
create or replace function public.getaccess(t_userid bigint)
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
$$;create or replace function public.getaccessid(t_userid bigint)
    returns integer
    language plpgsql
as
$$
declare
    t_access_id integer;
begin
    SELECT accessid INTO t_access_id FROM public.apitokens WHERE userid = t_userid;
    return t_access_id;
end;
$$;create or replace function public.getbanstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_banned boolean;
begin
    SELECT COUNT(*) INTO t_user_is_banned FROM public.botbanned WHERE userid = t_userid;
    return t_user_is_banned;
end;
$$;
create or replace function public.getbotban(t_userid bigint)
    returns integer
    language plpgsql
as
$$
declare
    t_user_banned integer;
begin
    SELECT COUNT(*) INTO t_user_banned FROM public.botbanned WHERE userid = t_userid;
    return t_user_banned;
end;
$$;
create or replace function public.getcommandusage(t_sessionid integer, t_commandname text)
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
$$;create or replace function public.getdatamodstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_datamod boolean;
begin
    SELECT COUNT(*) INTO t_user_is_datamod FROM public.datamods WHERE userid = t_userid;
    return t_user_is_datamod;
end;
$$;
create or replace function public.getmodstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_mod boolean;
begin
    SELECT COUNT(*) INTO t_user_is_mod FROM public.mods WHERE userid = t_userid;
    return t_user_is_mod;
end;
$$;
create or replace function public.getpatronstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_patron boolean;
begin
    SELECT COUNT(*) INTO t_user_is_patron FROM public.getpatrons WHERE userid = t_userid;
    return t_user_is_patron;
end;
$$;
create or replace function groupmembers.getpositionid(t_positionname text)
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
$$;create or replace function public.getproofreaderstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_proofreader boolean;
begin
    SELECT COUNT(*) INTO t_user_is_proofreader FROM public.proofreader WHERE userid = t_userid;
    return t_user_is_proofreader;
end;
$$;
create or replace function public.getsuperpatronstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_super_patron boolean;
begin
    SELECT COUNT(*) INTO t_user_is_super_patron FROM public.getsuperpatrons WHERE userid = t_userid;
    return t_user_is_super_patron;
end;
$$;
create or replace function groupmembers.gettagid(t_tagname text)
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
$$;create or replace function public.gettokenexists(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_token_exists boolean;
begin
    SELECT COUNT(*) INTO t_token_exists FROM public.apitokens WHERE userid = t_userid;
    return t_token_exists;
end;
$$;
create or replace function public.gettranslatorstatus(t_userid bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_user_is_translator boolean;
begin
    SELECT COUNT(*) INTO t_user_is_translator FROM public.translator WHERE userid = t_userid;
    return t_user_is_translator;
end;
$$;
create or replace function public.gettwitterid(t_username text)
    returns table
            (
                t_accountid bigint
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT accountid FROM public.twitteraccounts WHERE t_username = username;
end;
$$;create or replace function public.gettwitterstatus(t_account_id bigint, t_channel_id bigint)
    returns boolean
    language plpgsql
as
$$
declare
    t_exists boolean;
begin
    SELECT COUNT(*) INTO t_exists
    FROM public.twitterfollowage
    WHERE channelid = t_channel_id
      AND t_account_id = accountid;
    return t_exists;
end;
$$;
create or replace function public.getusage(t_userid bigint, t_endpoint text)
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
$$;create or replace function public.logfunc(t_userid bigint, t_func text, t_response text, t_args text, t_kwargs text)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO public.apiusage(userid, func, response, args, kwargs)
    VALUES(t_userid, t_func, t_response, t_args, t_kwargs);
end;
$$;create or replace function public.subscribetotwitch(t_username text, t_channel_id bigint, t_role_id bigint)
    returns void
    language plpgsql
as
$$
begin

    INSERT INTO public.twitchfollowage(username, channelid, posted, roleid) VALUES(t_username, t_channel_id,
                                                                                   False, t_role_id);
end;
$$;create or replace function public.toggleggfilter(t_userid bigint, active bool)
    returns void
    language plpgsql
as
$$
begin
    UPDATE public.users SET ggfilteractive = active WHERE userid = t_userid;
end;
$$;
create or replace function public.unsubscribefromtwitch(t_username text, t_channel_id bigint)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM public.twitchfollowage WHERE username = t_username AND channelid = t_channel_id ;
end;
$$;
create or replace function groupmembers.updatedate(t_date_id int, t_end_date timestamp)
    returns void
    language plpgsql
as
$$
begin
    UPDATE groupmembers.dates SET enddate = t_end_date WHERE dateid = t_date_id;
end;
$$;create or replace function guessinggame.updatemediaandstatus(t_game_id int, t_media_ids integer[], t_status_ids integer[])
    returns void
    language plpgsql
as
$$
begin
    UPDATE guessinggame.games SET mediaids = t_media_ids, statusids = t_status_ids WHERE gameid = t_game_id;
end;
$$;create or replace function public.updateposted(t_username text, channel_ids bigint[], t_posted bool)
    returns void
    language plpgsql
as
$$
begin
    UPDATE public.twitchfollowage SET posted = t_posted WHERE username = t_username AND channelid = any(channel_ids);
end;
$$;create or replace function public.updatepostedtwitter(t_account_id int, channel_ids bigint[], t_posted bool)
    returns void
    language plpgsql
as
$$
begin
    UPDATE public.twitterfollowage SET posted = t_posted WHERE accountid = t_account_id AND channelid = any(channel_ids);
end;
$$;create or replace function unscramblegame.updatestatus(t_game_id int, t_status_ids integer[])
    returns void
    language plpgsql
as
$$
begin
    UPDATE unscramblegame.games SET statusids = t_status_ids WHERE gameid = t_game_id;
end;
$$;create or replace function public.updateuserstatus(t_status_id integer, t_score int)
    returns void
    language plpgsql
as
$$
begin
    UPDATE public.userstatus SET score = t_score WHERE statusid = t_status_id;
end;
$$;create or replace function biasgame.upsertbgwin(t_user_id bigint, t_person_id integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO biasgame.winners(personid, userid, wins) VALUES (t_person_id, t_user_id, 1)
    ON CONFLICT (personid, userid) DO UPDATE SET wins = biasgame.winners.wins + 1 WHERE biasgame.winners.personid = t_person_id AND biasgame.winners.userid = t_user_id;

end;
$$;create or replace function guessinggame.upsertggfiltergroups(user_id bigint, group_ids integer[])
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO guessinggame.filtered(userid, groupids) VALUES (user_id, group_ids)
    ON CONFLICT (userid) DO UPDATE SET groupids = group_ids WHERE guessinggame.filtered.userid = user_id;
end;
$$;create or replace function guessinggame.upsertggfilterpersons(user_id bigint, person_ids integer[])
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO guessinggame.filtered(userid, personids) VALUES (user_id, person_ids)
    ON CONFLICT (userid) DO UPDATE SET personids = person_ids WHERE guessinggame.filtered.userid = user_id;
end;
$$;create or replace function guessinggame.upsertmediadifficulty(media_id integer, failed_guesses integer, correct_guesses integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO guessinggame.difficulty(mediaid, failed, correct) VALUES (media_id, failed_guesses, correct_guesses)
    ON CONFLICT (mediaid) DO UPDATE SET failed = failed_guesses, correct = correct_guesses WHERE guessinggame.difficulty.mediaid = media_id;
end;
$$;