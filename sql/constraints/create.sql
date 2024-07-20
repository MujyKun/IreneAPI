-- These constraints are kept outside of table definitions so that we don't need to worry about the order
-- that tables are created.
ALTER TABLE
  groupmembers.media
ADD
  CONSTRAINT media_affiliationid FOREIGN KEY (affiliationid) REFERENCES groupmembers.affiliations(affiliationid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  biasgame.winners
ADD
  CONSTRAINT winners_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE,
ADD
  CONSTRAINT winners_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  guessinggame.games
ADD
  CONSTRAINT gg_games_modeid FOREIGN KEY (modeid) REFERENCES modes(modeid) ON DELETE
SET
  NULL ON UPDATE CASCADE;
ALTER TABLE
  groupmembers.groups
ADD
  CONSTRAINT group_companyid FOREIGN KEY (companyid) REFERENCES groupmembers.companies(companyid) ON DELETE
SET
  NULL ON UPDATE CASCADE,
ADD
  CONSTRAINT group_displayid FOREIGN KEY (displayid) REFERENCES groupmembers.displays(displayid) ON DELETE
SET
  NULL ON UPDATE CASCADE,
ADD
  CONSTRAINT group_socialid FOREIGN KEY (socialid) REFERENCES groupmembers.socialmedia(socialid) ON DELETE
SET
  NULL ON UPDATE CASCADE;
ALTER TABLE
  groupmembers.persons
ADD
  CONSTRAINT person_displayid FOREIGN KEY (displayid) REFERENCES groupmembers.displays(displayid) ON DELETE
SET
  NULL ON UPDATE CASCADE,
ADD
  CONSTRAINT person_socialid FOREIGN KEY (socialid) REFERENCES groupmembers.socialmedia(socialid) ON DELETE
SET
  NULL ON UPDATE CASCADE,
ADD
  CONSTRAINT person_nameid FOREIGN KEY (nameid) REFERENCES groupmembers.names(nameid) ON DELETE
SET
  NULL ON UPDATE CASCADE,
ADD
  CONSTRAINT person_formernameid FOREIGN KEY (formernameid) REFERENCES groupmembers.names(nameid) ON DELETE
SET
  NULL ON UPDATE CASCADE,
ADD
  CONSTRAINT person_locationid FOREIGN KEY (locationid) REFERENCES groupmembers.locations(locationid) ON DELETE
SET
  NULL ON UPDATE CASCADE;
ALTER TABLE
  groupmembers.affiliation_positions
ADD
  CONSTRAINT fk_affiliation_positions_affiliation FOREIGN KEY (affiliationid) REFERENCES groupmembers.affiliations (affiliationid) ON DELETE CASCADE ON UPDATE CASCADE,
ADD
  CONSTRAINT fk_affiliation_positions_position FOREIGN KEY (positionid) REFERENCES groupmembers.positions (positionid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  patron
ADD
  CONSTRAINT patron_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  blackjack.customcards
ADD
  CONSTRAINT customcards_valueid FOREIGN KEY (valueid) REFERENCES blackjack.cardvalues(id) ON DELETE CASCADE ON UPDATE CASCADE,
ADD
  CONSTRAINT customcards_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  blackjack.games
ADD
  CONSTRAINT games_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.userstatus
ADD
  CONSTRAINT gg_userstatus_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE,
ADD
  CONSTRAINT us_userstatus_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  blackjack.userstatus
ADD
  CONSTRAINT bj_userstatus_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  groupmembers.affiliations
ADD
  CONSTRAINT affiliation_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE,
ADD
  CONSTRAINT affiliation_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  groupmembers.automedia
ADD
  CONSTRAINT automedia_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE,
ADD
  CONSTRAINT automedia_affid FOREIGN KEY (affiliationid) REFERENCES groupmembers.affiliations(affiliationid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  groupmembers.fandoms
ADD
  CONSTRAINT fandom_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  groupmembers.groupaliases
ADD
  CONSTRAINT ensure_groupalias CHECK (alias <> ''),
ADD
  CONSTRAINT groupaliases_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE,
ADD
  CONSTRAINT groupaliases_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE
SET
  NULL ON UPDATE CASCADE;
ALTER TABLE
  groupmembers.grouptags
ADD
  CONSTRAINT tags_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE,
ADD
  CONSTRAINT tags_tag_id FOREIGN KEY (tagid) REFERENCES groupmembers.tags(tagid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  groupmembers.locations
ADD
  CONSTRAINT ensure_country_or_city CHECK (
    country IS NOT NULL
    OR city IS NOT NULL
  );
ALTER TABLE
  groupmembers.personaliases
ADD
  CONSTRAINT ensure_personalias CHECK (alias <> ''),
ADD
  CONSTRAINT personaliases_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE
SET
  NULL ON UPDATE CASCADE,
ADD
  CONSTRAINT personaliases_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  translator
ADD
  CONSTRAINT translator_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  groupmembers.persontags
ADD
  CONSTRAINT p_tags_tag_id FOREIGN KEY (tagid) REFERENCES groupmembers.tags(tagid) ON DELETE CASCADE ON UPDATE CASCADE,
ADD
  CONSTRAINT tags_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  guessinggame.filtered
ADD
  CONSTRAINT filteredgroups_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  guessinggame.stats
ADD
  CONSTRAINT gg_stats_modeid FOREIGN KEY (modeid) REFERENCES modes(modeid) ON DELETE
SET
  NULL ON UPDATE CASCADE;
ALTER TABLE
  interactions.disabledtypes
ADD
  CONSTRAINT interactions_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  interactions.media
ADD
  CONSTRAINT media_typeid FOREIGN KEY (typeid) REFERENCES interactions.interactiontypes(typeid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.apitokens
ADD
  CONSTRAINT token_accessid FOREIGN KEY (accessid) REFERENCES public.apiaccess(accessid) ON DELETE CASCADE ON UPDATE CASCADE,
ADD
  CONSTRAINT token_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.apiusage
ADD
  CONSTRAINT usage_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.botbanned
ADD
  CONSTRAINT botbanned_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.commandusage
ADD
  CONSTRAINT commandusage_sessionid FOREIGN KEY (sessionid) REFERENCES public.sessions(sessionid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.customcommands
ADD
  CONSTRAINT customcommands_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  superpatron
ADD
  CONSTRAINT super_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.datamods
ADD
  CONSTRAINT datamods_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.guildprefixes
ADD
  CONSTRAINT guildprefixes_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.languagepacks
ADD
  CONSTRAINT pack_language FOREIGN KEY (languageid) REFERENCES public.languages(languageid) ON DELETE
SET
  NULL ON UPDATE CASCADE;
ALTER TABLE
  public.lastfm
ADD
  CONSTRAINT lastfm_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.levels
ADD
  CONSTRAINT levels_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.logging
ADD
  CONSTRAINT logging_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.mods
ADD
  CONSTRAINT mods_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  unscramblegame.stats
ADD
  CONSTRAINT us_stats_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE,
ADD
  CONSTRAINT us_stats_modeid FOREIGN KEY (modeid) REFERENCES modes(modeid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  unscramblegame.games
ADD
  CONSTRAINT us_games_modeid FOREIGN KEY (modeid) REFERENCES modes(modeid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.votes
ADD
  CONSTRAINT votes_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.users
ADD
  CONSTRAINT users_timezone FOREIGN KEY (timezoneid) REFERENCES public.timezones(id) ON DELETE
SET
  NULL ON UPDATE CASCADE,
ADD
  CONSTRAINT users_language FOREIGN KEY (languageid) REFERENCES public.languages(languageid) ON DELETE
SET
  NULL ON UPDATE CASCADE;
ALTER TABLE
  proofreader
ADD
  CONSTRAINT proofreader_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.reminders
ADD
  CONSTRAINT reminders_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.roles
ADD
  CONSTRAINT roles_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.selfassignroles
ADD
  CONSTRAINT selfassignroles_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.tempchannels
ADD
  CONSTRAINT tempchannels_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE
  public.twitchfollowage
ADD
  CONSTRAINT twitchfollowage_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;
