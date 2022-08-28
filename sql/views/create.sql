CREATE OR REPLACE VIEW groupmembers.getaffiliations AS
    SELECT affiliationid, personid, groupid, positionids, stagename FROM groupmembers.affiliation;CREATE OR REPLACE VIEW biasgame.getbgwinners AS
    SELECT personid, userid, wins from biasgame.winners;CREATE OR REPLACE VIEW groupmembers.getbloodtypes AS
    SELECT bloodid, name FROM groupmembers.bloodtypes;CREATE OR REPLACE VIEW public.getchannels AS
SELECT channelid, guildid
FROM public.channels c;CREATE OR REPLACE VIEW groupmembers.getcompanies AS
    SELECT companyid, name, description, dateid FROM groupmembers.company;CREATE OR REPLACE VIEW groupmembers.getdates AS
    SELECT dateid, startdate, enddate FROM groupmembers.dates;CREATE OR REPLACE VIEW groupmembers.getdisplays AS
    SELECT displayid, avatar, banner FROM groupmembers.display;CREATE OR REPLACE VIEW groupmembers.getfandoms AS
    SELECT groupid, name FROM groupmembers.fandom;CREATE OR REPLACE VIEW guessinggame.getggs AS
    SELECT gameid, dateid, mediaids, statusids, modeid, difficultyid, isnsfw FROM guessinggame.games;CREATE OR REPLACE VIEW groupmembers.getgroupaliases AS
    SELECT aliasid, alias, groupid, guildid FROM groupmembers.groupaliases;CREATE OR REPLACE VIEW groupmembers.getgroups AS
SELECT
       g.groupid,
       g.name,
       g.dateid,
       g.description,
       g.companyid,
       g.displayid,
       g.website,
       g.socialid,
    (SELECT array_agg(gt.tagid) AS tagids
    FROM groupmembers.grouptags gt
    WHERE gt.groupid = g.groupid),
   (SELECT array_agg(aliasid) AS aliasids
    FROM groupmembers.groupaliases ga
    WHERE ga.groupid = g.groupid)
FROM groupmembers.groups g;CREATE OR REPLACE VIEW public.getguilds AS
SELECT
       guildid,
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
       hasbot,
        (SELECT array_agg(t_gp.prefix)
        FROM public.guildprefixes t_gp WHERE g.guildid = t_gp.guildid) AS prefixes
FROM public.guilds g;CREATE OR REPLACE VIEW public.getlanguages AS
    SELECT l.languageid, l.shortname, l.name,
           (SELECT json_agg(row_to_json(lp)) FROM public.languagepacks lp WHERE lp.languageid = l.languageid) AS pack
    FROM public.languages l;
CREATE OR REPLACE VIEW groupmembers.getlocations AS
    SELECT locationid, country, city FROM groupmembers.location;CREATE OR REPLACE VIEW groupmembers.getmedia AS
    SELECT m.mediaid, link, faces, filetype, m.affiliationid, a.personid, a.groupid, enabled, nsfw, d.failed, d.correct
        FROM groupmembers.media m LEFT JOIN
            groupmembers.affiliation a on m.affiliationid = a.affiliationid
            LEFT JOIN guessinggame.difficulty d on d.mediaid = m.mediaid;
CREATE OR REPLACE VIEW groupmembers.getnames AS
    SELECT nameid, firstname, lastname FROM groupmembers.name;CREATE OR REPLACE VIEW getpatrons AS
SELECT p.userid FROM public.patron p
UNION DISTINCT
SELECT sp.userid FROM public.superpatron sp
UNION DISTINCT
SELECT t.userid FROM public.translator t
UNION DISTINCT
SELECT pr.userid FROM public.proofreader pr
UNION DISTINCT
SELECT mod.userid FROM public.mods mod
UNION DISTINCT
SELECT dmod.userid FROM public.datamods dmod
ORDER BY userid DESC;CREATE OR REPLACE VIEW groupmembers.getpersonaliases AS
    SELECT aliasid, alias, personid, guildid FROM groupmembers.personaliases;CREATE OR REPLACE VIEW groupmembers.getpersons AS
    SELECT
        p.personid,
        p.dateid,
        p.nameid,
        p.formernameid,
        p.displayid,
        p.socialid,
        p.locationid,
        p.bloodid,
        gender,
        description,
        height,
        callcount,
       (SELECT array_agg(pt.tagid) AS tagids
            FROM groupmembers.persontags pt
            WHERE pt.personid = p.personid),
       (SELECT array_agg(aliasid) AS aliasids
            FROM groupmembers.personaliases pa
            WHERE pa.personid = p.personid)
       FROM groupmembers.person p;CREATE OR REPLACE VIEW groupmembers.getpositions AS
    SELECT positionid, name FROM groupmembers.position;CREATE OR REPLACE VIEW public.getprefixes AS
SELECT
        DISTINCT (gp.guildid),
        (SELECT array_agg(t_gp.prefix)
        FROM public.guildprefixes t_gp WHERE gp.guildid = t_gp.guildid) as prefixes
FROM public.guildprefixes gp;CREATE OR REPLACE VIEW public.getresponses AS
    SELECT responseid, response FROM public.eightball;
CREATE OR REPLACE VIEW groupmembers.getsocials AS
    SELECT socialid, twitter, youtube, melon, instagram, vlive, spotify, fancafe, facebook, tiktok
    FROM groupmembers.socialmedia;CREATE OR REPLACE VIEW getsuperpatrons AS
SELECT sp.userid FROM public.superpatron sp
UNION DISTINCT
SELECT mod.userid FROM public.mods mod
ORDER BY userid DESC;CREATE OR REPLACE VIEW groupmembers.gettags AS
    SELECT tagid, name FROM groupmembers.tag;CREATE OR REPLACE VIEW public.gettwitchchannels AS
SELECT username, guildid, c.channelid, posted, roleid
FROM public.twitchfollowage c LEFT JOIN public.channels ch on c.channelid = ch.channelid;CREATE OR REPLACE VIEW public.gettwitterchannels AS
SELECT c.accountid, username, guildid, c.channelid, roleid
FROM public.twitterfollowage c
    LEFT JOIN public.channels ch on c.channelid = ch.channelid
    LEFT JOIN public.twitteraccounts ta ON c.accountid = ta.accountid;CREATE OR REPLACE VIEW public.getusers AS
    SELECT u.userid as userid,
                        u.balance as balance,
                        u.ggfilteractive as ggfilteractive,
                        u.xp xp,
                        (SELECT exists(
                            SELECT 1
                            FROM public.patron
                            WHERE patron.userid = u.userid))
                            AS ispatron,
                        (SELECT exists(
                            SELECT 1
                            FROM public.mods
                            WHERE mods.userid = u.userid))
                            AS ismod,
                        (SELECT exists(
                            SELECT 1
                            FROM public.proofreader
                            WHERE proofreader.userid = u.userid))
                            AS isproofreader,
                        (SELECT exists(
                            SELECT 1
                            FROM public.translator
                            WHERE translator.userid = u.userid))
                            AS istranslator,
                        (SELECT exists(
                            SELECT 1
                            FROM public.datamods
                            WHERE datamods.userid = u.userid))
                            AS isdatamod,
                        (SELECT exists(
                            SELECT 1
                            FROM public.superpatron
                            WHERE superpatron.userid = u.userid))
                            AS issuperpatron,
                        (SELECT exists(
                            SELECT 1
                            FROM public.botbanned
                            WHERE botbanned.userid = u.userid))
                            AS isbanned,
                        (SELECT shortname
                            FROM public.languages
                            WHERE u.languageid = public.languages.languageid)
                            AS language,
                        (SELECT accessid
                            FROM public.apitokens
                            WHERE u.userid = public.apitokens.userid)
                            AS access,
                        (SELECT username
                            FROM public.lastfm
                            WHERE u.userid = public.lastfm.userid)
                            AS lastfmusername,
                        (SELECT shortname
                            FROM public.timezones
                            WHERE u.timezoneid = public.timezones.id)
                            AS timezone,
                        l.rob as roblevel, l.daily as dailylevel, l.beg as beglevel, l.profile as profilelevel,
                        gf.groupids as ggfiltergroups, gf.personids as ggfilterpersons
    FROM users u LEFT JOIN public.levels l ON l.userid = u.userid LEFT JOIN
        guessinggame.filtered gf ON gf.userid = u.userid;CREATE OR REPLACE VIEW public.getuserstatuses AS
    SELECT statusid, userid, score FROM public.userstatus;
CREATE OR REPLACE VIEW unscramblegame.getuss AS
    SELECT gameid, dateid, statusids, modeid, difficultyid FROM unscramblegame.games;

