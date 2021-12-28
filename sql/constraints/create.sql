ALTER TABLE groupmembers.affiliation DROP CONSTRAINT IF EXISTS affiliation_groupid;
ALTER TABLE groupmembers.groupaliases DROP CONSTRAINT IF EXISTS groupaliases_groupid;
ALTER TABLE groupmembers.fandom DROP CONSTRAINT IF EXISTS fandom_groupid;
ALTER TABLE groupmembers.affiliation ADD CONSTRAINT affiliation_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE groupmembers.groupaliases ADD CONSTRAINT groupaliases_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE groupmembers.fandom ADD CONSTRAINT fandom_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE groupmembers.automedia DROP CONSTRAINT IF EXISTS automedia_channelid;
ALTER TABLE blackjack.games DROP CONSTRAINT IF EXISTS games_channelid;
ALTER TABLE groupmembers.automedia ADD CONSTRAINT automedia_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE blackjack.games ADD CONSTRAINT games_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE groupmembers.company DROP CONSTRAINT IF EXISTS company_dateid;
ALTER TABLE groupmembers.groups DROP CONSTRAINT IF EXISTS group_dateid;
ALTER TABLE groupmembers.person DROP CONSTRAINT IF EXISTS person_dateid;
ALTER TABLE guessinggame.games DROP CONSTRAINT IF EXISTS gg_games_dateid;
ALTER TABLE unscramblegame.games DROP CONSTRAINT IF EXISTS us_games_dateid;
ALTER TABLE public.reminders DROP CONSTRAINT IF EXISTS reminders_dateid;
ALTER TABLE groupmembers.company ADD CONSTRAINT company_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE groupmembers.groups ADD CONSTRAINT group_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE groupmembers.person ADD CONSTRAINT person_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE guessinggame.games ADD CONSTRAINT gg_games_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE unscramblegame.games ADD CONSTRAINT us_games_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE public.reminders ADD CONSTRAINT reminders_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE groupmembers.groupaliases DROP CONSTRAINT IF EXISTS groupaliases_guildid;
ALTER TABLE groupmembers.personaliases DROP CONSTRAINT IF EXISTS personaliases_guildid;
ALTER TABLE public.customcommands DROP CONSTRAINT IF EXISTS customcommands_guildid;
ALTER TABLE interactions.disabledtypes DROP CONSTRAINT IF EXISTS interactions_guildid;
ALTER TABLE public.guildprefixes DROP CONSTRAINT IF EXISTS guildprefixes_guildid;
ALTER TABLE public.logging DROP CONSTRAINT IF EXISTS logging_guildid;
ALTER TABLE public.roles DROP CONSTRAINT IF EXISTS roles_guildid;
ALTER TABLE public.twitchfollowage DROP CONSTRAINT IF EXISTS twitchfollowage_guildid;
ALTER TABLE groupmembers.groupaliases ADD CONSTRAINT groupaliases_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE groupmembers.personaliases ADD CONSTRAINT personaliases_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE public.customcommands ADD CONSTRAINT customcommands_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE interactions.disabledtypes ADD CONSTRAINT interactions_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.guildprefixes ADD CONSTRAINT guildprefixes_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.logging ADD CONSTRAINT logging_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.roles ADD CONSTRAINT roles_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.twitchfollowage ADD CONSTRAINT twitchfollowage_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE groupmembers.personaliases DROP CONSTRAINT IF EXISTS personaliases_personid;
ALTER TABLE groupmembers.affiliation DROP CONSTRAINT IF EXISTS affiliation_personid;
ALTER TABLE biasgame.winners DROP CONSTRAINT IF EXISTS winners_personid;
ALTER TABLE blackjack.customcards DROP CONSTRAINT IF EXISTS customcards_personid;
ALTER TABLE groupmembers.personaliases ADD CONSTRAINT personaliases_personid FOREIGN KEY (personid) REFERENCES groupmembers.person(personid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE groupmembers.affiliation ADD CONSTRAINT affiliation_personid FOREIGN KEY (personid) REFERENCES groupmembers.person(personid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE biasgame.winners ADD CONSTRAINT winners_personid FOREIGN KEY (personid) REFERENCES groupmembers.person(personid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE blackjack.customcards ADD CONSTRAINT customcards_personid FOREIGN KEY (personid) REFERENCES groupmembers.person(personid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE groupmembers.groups DROP CONSTRAINT IF EXISTS group_companyid;
ALTER TABLE groupmembers.groups ADD CONSTRAINT group_companyid FOREIGN KEY (companyid) REFERENCES groupmembers.company(companyid) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE groupmembers.groups DROP CONSTRAINT IF EXISTS group_displayid;
ALTER TABLE groupmembers.person DROP CONSTRAINT IF EXISTS person_displayid;
ALTER TABLE groupmembers.groups ADD CONSTRAINT group_displayid FOREIGN KEY (displayid) REFERENCES groupmembers.display(displayid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE groupmembers.person ADD CONSTRAINT person_displayid FOREIGN KEY (displayid) REFERENCES groupmembers.display(displayid) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE groupmembers.groups DROP CONSTRAINT IF EXISTS group_socialid;
ALTER TABLE groupmembers.person DROP CONSTRAINT IF EXISTS person_socialid;
ALTER TABLE groupmembers.groups ADD CONSTRAINT group_socialid FOREIGN KEY (socialid) REFERENCES groupmembers.socialmedia(socialid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE groupmembers.person ADD CONSTRAINT person_socialid FOREIGN KEY (socialid) REFERENCES groupmembers.socialmedia(socialid) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE groupmembers.media DROP CONSTRAINT IF EXISTS media_affiliationid;
ALTER TABLE groupmembers.media ADD CONSTRAINT media_affiliationid FOREIGN KEY (affiliationid) REFERENCES groupmembers.affiliation(affiliationid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE groupmembers.person DROP CONSTRAINT IF EXISTS person_nameid;
ALTER TABLE groupmembers.person ADD CONSTRAINT person_nameid FOREIGN KEY (nameid) REFERENCES groupmembers.name(nameid) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE groupmembers.person DROP CONSTRAINT IF EXISTS person_formernameid;
ALTER TABLE groupmembers.person ADD CONSTRAINT person_formernameid FOREIGN KEY (formernameid) REFERENCES groupmembers.name(nameid) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE groupmembers.person DROP CONSTRAINT IF EXISTS person_locationid;
ALTER TABLE groupmembers.person ADD CONSTRAINT person_locationid FOREIGN KEY (locationid) REFERENCES groupmembers.location(locationid) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE groupmembers.person DROP CONSTRAINT IF EXISTS person_bloodid;
ALTER TABLE groupmembers.person ADD CONSTRAINT person_bloodid FOREIGN KEY (bloodid) REFERENCES groupmembers.bloodtypes(bloodid) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE blackjack.customcards DROP CONSTRAINT IF EXISTS customcards_valueid;
ALTER TABLE blackjack.customcards ADD CONSTRAINT customcards_valueid FOREIGN KEY (valueid) REFERENCES blackjack.cardvalues(id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE blackjack.userstatus DROP CONSTRAINT IF EXISTS bj_userstatus_userid;
ALTER TABLE guessinggame.filteredgroups DROP CONSTRAINT IF EXISTS filteredgroups_userid;
ALTER TABLE guessinggame.userstatus DROP CONSTRAINT IF EXISTS gg_userstatus_userid;
ALTER TABLE unscramblegame.stats DROP CONSTRAINT IF EXISTS us_stats_userid;
ALTER TABLE unscramblegame.userstatus DROP CONSTRAINT IF EXISTS us_userstatus_userid;
ALTER TABLE public.apitokens DROP CONSTRAINT IF EXISTS token_userid;
ALTER TABLE public.apiusage DROP CONSTRAINT IF EXISTS usage_userid;
ALTER TABLE public.botbanned DROP CONSTRAINT IF EXISTS botbanned_userid;
ALTER TABLE public.datamods DROP CONSTRAINT IF EXISTS datamods_userid;
ALTER TABLE public.lastfm DROP CONSTRAINT IF EXISTS lastfm_userid;
ALTER TABLE public.levels DROP CONSTRAINT IF EXISTS levels_userid;
ALTER TABLE public.mods DROP CONSTRAINT IF EXISTS mods_userid;
ALTER TABLE public.reminders DROP CONSTRAINT IF EXISTS reminders_userid;
ALTER TABLE public.votes DROP CONSTRAINT IF EXISTS votes_userid;
ALTER TABLE public.patron DROP CONSTRAINT IF EXISTS patron_userid;
ALTER TABLE public.superpatron DROP CONSTRAINT IF EXISTS super_userid;
ALTER TABLE public.translator DROP CONSTRAINT IF EXISTS translator_userid;
ALTER TABLE public.proofreader DROP CONSTRAINT IF EXISTS proofreader_userid;
ALTER TABLE blackjack.userstatus ADD CONSTRAINT bj_userstatus_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE guessinggame.filteredgroups ADD CONSTRAINT filteredgroups_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE guessinggame.userstatus ADD CONSTRAINT gg_userstatus_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE unscramblegame.stats ADD CONSTRAINT us_stats_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE unscramblegame.userstatus ADD CONSTRAINT us_userstatus_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.apitokens ADD CONSTRAINT token_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.apiusage ADD CONSTRAINT usage_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.botbanned ADD CONSTRAINT botbanned_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.datamods ADD CONSTRAINT datamods_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.lastfm ADD CONSTRAINT lastfm_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.levels ADD CONSTRAINT levels_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.mods ADD CONSTRAINT mods_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.reminders ADD CONSTRAINT reminders_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.votes ADD CONSTRAINT votes_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.patron ADD CONSTRAINT patron_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.superpatron ADD CONSTRAINT super_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.translator ADD CONSTRAINT translator_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.proofreader ADD CONSTRAINT proofreader_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;


ALTER TABLE guessinggame.games DROP CONSTRAINT IF EXISTS gg_games_modeid;
ALTER TABLE guessinggame.stats DROP CONSTRAINT IF EXISTS gg_stats_modeid;
ALTER TABLE unscramblegame.games DROP CONSTRAINT IF EXISTS us_games_modeid;
ALTER TABLE unscramblegame.stats DROP CONSTRAINT IF EXISTS us_stats_modeid;
ALTER TABLE guessinggame.games ADD CONSTRAINT gg_games_modeid FOREIGN KEY (modeid) REFERENCES guessinggame.modes(modeid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE guessinggame.stats ADD CONSTRAINT gg_stats_modeid FOREIGN KEY (modeid) REFERENCES guessinggame.modes(modeid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE unscramblegame.games ADD CONSTRAINT us_games_modeid FOREIGN KEY (modeid) REFERENCES unscramblegame.modes(modeid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE unscramblegame.stats ADD CONSTRAINT us_stats_modeid FOREIGN KEY (modeid) REFERENCES unscramblegame.modes(modeid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE interactions.media DROP CONSTRAINT IF EXISTS media_typeid;
ALTER TABLE interactions.media ADD CONSTRAINT media_typeid FOREIGN KEY (typeid) REFERENCES interactions.interactiontypes(typeid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.apitokens DROP CONSTRAINT IF EXISTS token_accessid;
ALTER TABLE public.apitokens ADD CONSTRAINT token_accessid FOREIGN KEY (accessid) REFERENCES public.apiaccess(accessid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.commandusage DROP CONSTRAINT IF EXISTS commandusage_sessionid;
ALTER TABLE public.commandusage ADD CONSTRAINT commandusage_sessionid FOREIGN KEY (sessionid) REFERENCES public.sessions(sessionid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.selfassignroles DROP CONSTRAINT IF EXISTS selfassignroles_channelid;
ALTER TABLE public.tempchannels DROP CONSTRAINT IF EXISTS tempchannels_channelid;
ALTER TABLE public.twitchfollowage DROP CONSTRAINT IF EXISTS twitchfollowage_channelid;
ALTER TABLE public.twitterfollowage DROP CONSTRAINT IF EXISTS twitterfollowage_channelid;
ALTER TABLE public.selfassignroles ADD CONSTRAINT selfassignroles_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.tempchannels ADD CONSTRAINT tempchannels_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.twitchfollowage ADD CONSTRAINT twitchfollowage_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.twitterfollowage ADD CONSTRAINT twitterfollowage_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.twitteruploadedmedia DROP CONSTRAINT IF EXISTS twitteruploadedmedia_mediaid;
ALTER TABLE public.twitteruploadedmedia ADD CONSTRAINT twitteruploadedmedia_mediaid FOREIGN KEY (mediaid) REFERENCES groupmembers.media(mediaid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.users DROP CONSTRAINT IF EXISTS users_timezone;
ALTER TABLE public.users ADD CONSTRAINT users_timezone FOREIGN KEY (timezoneid) REFERENCES public.timezones(id) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE public.users DROP CONSTRAINT IF EXISTS users_language;
ALTER TABLE public.users ADD CONSTRAINT users_language FOREIGN KEY (languageid) REFERENCES public.languages(languageid) ON DELETE SET NULL ON UPDATE CASCADE;