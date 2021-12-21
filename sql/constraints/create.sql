ALTER TABLE groupmembers.affiliation DROP CONSTRAINT IF EXISTS affiliation_groupid;
ALTER TABLE groupmembers.groupaliases DROP CONSTRAINT IF EXISTS groupaliases_groupid;
ALTER TABLE groupmembers.fandom DROP CONSTRAINT IF EXISTS fandom_groupid;
ALTER TABLE groupmembers.affiliation ADD CONSTRAINT affiliation_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE groupmembers.groupaliases ADD CONSTRAINT groupaliases_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE groupmembers.fandom ADD CONSTRAINT fandom_groupid FOREIGN KEY (groupid) REFERENCES groupmembers.groups(groupid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE groupmembers.automedia DROP CONSTRAINT IF EXISTS automedia_channelid;
ALTER TABLE groupmembers.automedia ADD CONSTRAINT automedia_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE groupmembers.company DROP CONSTRAINT IF EXISTS company_dateid;
ALTER TABLE groupmembers.groups DROP CONSTRAINT IF EXISTS group_dateid;
ALTER TABLE groupmembers.person DROP CONSTRAINT IF EXISTS person_dateid;
ALTER TABLE groupmembers.company ADD CONSTRAINT company_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE groupmembers.groups ADD CONSTRAINT group_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE groupmembers.person ADD CONSTRAINT person_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE groupmembers.groupaliases DROP CONSTRAINT IF EXISTS groupaliases_guildid;
ALTER TABLE groupmembers.personaliases DROP CONSTRAINT IF EXISTS personaliases_guildid;
ALTER TABLE groupmembers.groupaliases ADD CONSTRAINT groupaliases_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE groupmembers.personaliases ADD CONSTRAINT personaliases_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE groupmembers.personaliases DROP CONSTRAINT IF EXISTS personaliases_personid;
ALTER TABLE groupmembers.affiliation DROP CONSTRAINT IF EXISTS affiliation_personid;
ALTER TABLE groupmembers.personaliases ADD CONSTRAINT personaliases_personid FOREIGN KEY (personid) REFERENCES groupmembers.person(personid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE groupmembers.affiliation ADD CONSTRAINT affiliation_personid FOREIGN KEY (personid) REFERENCES groupmembers.person(personid) ON DELETE CASCADE ON UPDATE CASCADE;


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


