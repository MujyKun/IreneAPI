-- DROP SCHEMA biasgame;

CREATE SCHEMA biasgame AUTHORIZATION postgres;

COMMENT ON SCHEMA biasgame IS 'Information contained for a bias game.';
-- biasgame.winners definition

-- Drop table

-- DROP TABLE biasgame.winners;

CREATE TABLE biasgame.winners (
	personid int4 NOT NULL,
	userid int8 NOT NULL,
	wins int4 NULL,
	CONSTRAINT bg_personid_userid PRIMARY KEY (personid, userid)
);
CREATE INDEX idx_winners_personid_userid ON biasgame.winners USING btree (personid, userid);
COMMENT ON TABLE biasgame.winners IS 'The amount of wins a user has on a person.';

-- Permissions

ALTER TABLE biasgame.winners OWNER TO postgres;
GRANT ALL ON TABLE biasgame.winners TO postgres;


-- biasgame.winners foreign keys

ALTER TABLE biasgame.winners ADD CONSTRAINT winners_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE biasgame.winners ADD CONSTRAINT winners_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;




-- Permissions

GRANT ALL ON SCHEMA biasgame TO postgres;

-- DROP SCHEMA blackjack;

CREATE SCHEMA blackjack AUTHORIZATION postgres;

COMMENT ON SCHEMA blackjack IS 'Information contained for a blackjack game.';

-- DROP SEQUENCE blackjack.cardvalues_id_seq;

CREATE SEQUENCE blackjack.cardvalues_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE blackjack.cardvalues_id_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE blackjack.cardvalues_id_seq TO postgres;

-- DROP SEQUENCE blackjack.customcards_id_seq;

CREATE SEQUENCE blackjack.customcards_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE blackjack.customcards_id_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE blackjack.customcards_id_seq TO postgres;

-- DROP SEQUENCE blackjack.games_gameid_seq;

CREATE SEQUENCE blackjack.games_gameid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE blackjack.games_gameid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE blackjack.games_gameid_seq TO postgres;

-- DROP SEQUENCE blackjack.userstatus_statusid_seq;

CREATE SEQUENCE blackjack.userstatus_statusid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE blackjack.userstatus_statusid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE blackjack.userstatus_statusid_seq TO postgres;
-- blackjack.cardvalues definition

-- Drop table

-- DROP TABLE blackjack.cardvalues;

CREATE TABLE blackjack.cardvalues (
	id serial4 NOT NULL,
	"name" text NULL,
	value int4 NULL,
	CONSTRAINT cardvalues_pkey PRIMARY KEY (id)
);
COMMENT ON TABLE blackjack.cardvalues IS 'The values of cards';

-- Permissions

ALTER TABLE blackjack.cardvalues OWNER TO postgres;
GRANT ALL ON TABLE blackjack.cardvalues TO postgres;


-- blackjack.customcards definition

-- Drop table

-- DROP TABLE blackjack.customcards;

CREATE TABLE blackjack.customcards (
	id serial4 NOT NULL,
	valueid int4 NULL,
	personid int4 NULL,
	filename text NULL,
	CONSTRAINT customcards_pkey PRIMARY KEY (id)
);
COMMENT ON TABLE blackjack.customcards IS 'Custom playing cards with unique backgrounds.';

-- Permissions

ALTER TABLE blackjack.customcards OWNER TO postgres;
GRANT ALL ON TABLE blackjack.customcards TO postgres;


-- blackjack.games definition

-- Drop table

-- DROP TABLE blackjack.games;

CREATE TABLE blackjack.games (
	gameid serial4 NOT NULL,
	channelid int8 NULL,
	statusids _int4 NULL,
	active bool NULL,
	CONSTRAINT games_pkey PRIMARY KEY (gameid)
);
COMMENT ON TABLE blackjack.games IS 'The active and inactive blackjack games.';

-- Permissions

ALTER TABLE blackjack.games OWNER TO postgres;
GRANT ALL ON TABLE blackjack.games TO postgres;


-- blackjack.userstatus definition

-- Drop table

-- DROP TABLE blackjack.userstatus;

CREATE TABLE blackjack.userstatus (
	statusid serial4 NOT NULL,
	userid int8 NOT NULL,
	stand bool NULL,
	cards _int4 NULL,
	bid text NULL,
	CONSTRAINT userstatus_pkey PRIMARY KEY (statusid, userid)
);
COMMENT ON TABLE blackjack.userstatus IS 'The status of a user in a blackjack game.';

-- Permissions

ALTER TABLE blackjack.userstatus OWNER TO postgres;
GRANT ALL ON TABLE blackjack.userstatus TO postgres;


-- blackjack.customcards foreign keys

ALTER TABLE blackjack.customcards ADD CONSTRAINT customcards_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE blackjack.customcards ADD CONSTRAINT customcards_valueid FOREIGN KEY (valueid) REFERENCES blackjack.cardvalues(id) ON DELETE CASCADE ON UPDATE CASCADE;


-- blackjack.games foreign keys

ALTER TABLE blackjack.games ADD CONSTRAINT games_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;


-- blackjack.userstatus foreign keys

ALTER TABLE blackjack.userstatus ADD CONSTRAINT bj_userstatus_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;




-- Permissions

GRANT ALL ON SCHEMA blackjack TO postgres;

-- DROP SCHEMA groupmembers;

CREATE SCHEMA groupmembers AUTHORIZATION postgres;

COMMENT ON SCHEMA groupmembers IS 'Everything related to Celebrities, Groups, Affiliations, and Companies.';

-- DROP SEQUENCE groupmembers.affiliations_affiliationid_seq;

CREATE SEQUENCE groupmembers.affiliations_affiliationid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.affiliations_affiliationid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.affiliations_affiliationid_seq TO postgres;

-- DROP SEQUENCE groupmembers.companies_companyid_seq;

CREATE SEQUENCE groupmembers.companies_companyid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.companies_companyid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.companies_companyid_seq TO postgres;

-- DROP SEQUENCE groupmembers.dates_dateid_seq;

CREATE SEQUENCE groupmembers.dates_dateid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.dates_dateid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.dates_dateid_seq TO postgres;

-- DROP SEQUENCE groupmembers.displays_displayid_seq;

CREATE SEQUENCE groupmembers.displays_displayid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.displays_displayid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.displays_displayid_seq TO postgres;

-- DROP SEQUENCE groupmembers.groupaliases_aliasid_seq;

CREATE SEQUENCE groupmembers.groupaliases_aliasid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.groupaliases_aliasid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.groupaliases_aliasid_seq TO postgres;

-- DROP SEQUENCE groupmembers.groups_groupid_seq;

CREATE SEQUENCE groupmembers.groups_groupid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.groups_groupid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.groups_groupid_seq TO postgres;

-- DROP SEQUENCE groupmembers.locations_locationid_seq;

CREATE SEQUENCE groupmembers.locations_locationid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.locations_locationid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.locations_locationid_seq TO postgres;

-- DROP SEQUENCE groupmembers.media_mediaid_seq;

CREATE SEQUENCE groupmembers.media_mediaid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.media_mediaid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.media_mediaid_seq TO postgres;

-- DROP SEQUENCE groupmembers.names_nameid_seq;

CREATE SEQUENCE groupmembers.names_nameid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.names_nameid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.names_nameid_seq TO postgres;

-- DROP SEQUENCE groupmembers.personaliases_aliasid_seq;

CREATE SEQUENCE groupmembers.personaliases_aliasid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.personaliases_aliasid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.personaliases_aliasid_seq TO postgres;

-- DROP SEQUENCE groupmembers.persons_personid_seq;

CREATE SEQUENCE groupmembers.persons_personid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.persons_personid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.persons_personid_seq TO postgres;

-- DROP SEQUENCE groupmembers.positions_positionid_seq;

CREATE SEQUENCE groupmembers.positions_positionid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.positions_positionid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.positions_positionid_seq TO postgres;

-- DROP SEQUENCE groupmembers.socialmedia_socialid_seq;

CREATE SEQUENCE groupmembers.socialmedia_socialid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.socialmedia_socialid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.socialmedia_socialid_seq TO postgres;

-- DROP SEQUENCE groupmembers.tags_tagid_seq;

CREATE SEQUENCE groupmembers.tags_tagid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE groupmembers.tags_tagid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE groupmembers.tags_tagid_seq TO postgres;
-- groupmembers.dates definition

-- Drop table

-- DROP TABLE groupmembers.dates;

CREATE TABLE groupmembers.dates (
	dateid serial4 NOT NULL,
	startdate timestamp NULL,
	enddate timestamp NULL,
	CONSTRAINT dates_pkey PRIMARY KEY (dateid),
	CONSTRAINT unique_dates UNIQUE (startdate, enddate)
);
CREATE INDEX idx_dates_dateid ON groupmembers.dates USING btree (dateid);
COMMENT ON TABLE groupmembers.dates IS 'Contains a start and end date.';

-- Permissions

ALTER TABLE groupmembers.dates OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.dates TO postgres;


-- groupmembers.displays definition

-- Drop table

-- DROP TABLE groupmembers.displays;

CREATE TABLE groupmembers.displays (
	displayid serial4 NOT NULL,
	avatar text NULL,
	banner text NULL,
	CONSTRAINT displays_pkey PRIMARY KEY (displayid),
	CONSTRAINT unique_display UNIQUE (avatar, banner)
);
CREATE INDEX idx_display_displayid ON groupmembers.displays USING btree (displayid);
COMMENT ON TABLE groupmembers.displays IS 'Contains the URL to an avatar and banner';

-- Permissions

ALTER TABLE groupmembers.displays OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.displays TO postgres;


-- groupmembers.locations definition

-- Drop table

-- DROP TABLE groupmembers.locations;

CREATE TABLE groupmembers.locations (
	locationid serial4 NOT NULL,
	country text NULL,
	city text NULL,
	CONSTRAINT ensure_country_or_city CHECK (((country IS NOT NULL) AND (city IS NOT NULL))),
	CONSTRAINT locations_country_city_key UNIQUE (country, city),
	CONSTRAINT locations_pkey PRIMARY KEY (locationid)
);
COMMENT ON TABLE groupmembers.locations IS 'Contains a country and city.';

-- Permissions

ALTER TABLE groupmembers.locations OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.locations TO postgres;


-- groupmembers.names definition

-- Drop table

-- DROP TABLE groupmembers.names;

CREATE TABLE groupmembers.names (
	nameid serial4 NOT NULL,
	firstname text NULL,
	lastname text NULL,
	CONSTRAINT names_pkey PRIMARY KEY (nameid),
	CONSTRAINT unique_name UNIQUE (firstname, lastname)
);
CREATE INDEX idx_name_nameid ON groupmembers.names USING btree (nameid);
COMMENT ON TABLE groupmembers.names IS 'Contains a first and last name. Useful for people with several names. ';

-- Permissions

ALTER TABLE groupmembers.names OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.names TO postgres;


-- groupmembers.positions definition

-- Drop table

-- DROP TABLE groupmembers.positions;

CREATE TABLE groupmembers.positions (
	positionid serial4 NOT NULL,
	"name" text NULL,
	CONSTRAINT positions_name_key UNIQUE (name),
	CONSTRAINT positions_pkey PRIMARY KEY (positionid)
);
CREATE INDEX idx_position_positionid ON groupmembers.positions USING btree (positionid);
COMMENT ON TABLE groupmembers.positions IS 'A position such as vocal, leader, dancer.';

-- Permissions

ALTER TABLE groupmembers.positions OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.positions TO postgres;


-- groupmembers.socialmedia definition

-- Drop table

-- DROP TABLE groupmembers.socialmedia;

CREATE TABLE groupmembers.socialmedia (
	socialid serial4 NOT NULL,
	twitter text NULL,
	youtube text NULL,
	melon text NULL,
	instagram text NULL,
	vlive text NULL,
	spotify text NULL,
	fancafe text NULL,
	facebook text NULL,
	tiktok text NULL,
	CONSTRAINT non_empty_columns CHECK (((twitter <> ''::text) AND (youtube <> ''::text) AND (melon <> ''::text) AND (instagram <> ''::text) AND (vlive <> ''::text) AND (spotify <> ''::text) AND (fancafe <> ''::text) AND (facebook <> ''::text) AND (tiktok <> ''::text))),
	CONSTRAINT socialmedia_pkey PRIMARY KEY (socialid),
	CONSTRAINT unique_social_media UNIQUE (twitter, youtube, melon, instagram, vlive, spotify, fancafe, facebook, tiktok)
);
CREATE INDEX idx_socialmedia_socialid ON groupmembers.socialmedia USING btree (socialid);
COMMENT ON TABLE groupmembers.socialmedia IS 'Contains information about social media. Will be linked to an entity. ';

-- Permissions

ALTER TABLE groupmembers.socialmedia OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.socialmedia TO postgres;


-- groupmembers.tags definition

-- Drop table

-- DROP TABLE groupmembers.tags;

CREATE TABLE groupmembers.tags (
	tagid serial4 NOT NULL,
	"name" text NULL,
	CONSTRAINT tags_name_key UNIQUE (name),
	CONSTRAINT tags_pkey PRIMARY KEY (tagid)
);
CREATE INDEX idx_tag_tagid ON groupmembers.tags USING btree (tagid);
COMMENT ON TABLE groupmembers.tags IS 'A general list of tags. ';

-- Permissions

ALTER TABLE groupmembers.tags OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.tags TO postgres;


-- groupmembers.companies definition

-- Drop table

-- DROP TABLE groupmembers.companies;

CREATE TABLE groupmembers.companies (
	companyid serial4 NOT NULL,
	"name" text NULL,
	description text NULL,
	dateid int4 NULL,
	CONSTRAINT companies_pkey PRIMARY KEY (companyid),
	CONSTRAINT unique_company_name UNIQUE (name),
	CONSTRAINT company_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE
);
CREATE INDEX idx_company_companyid ON groupmembers.companies USING btree (companyid);
COMMENT ON TABLE groupmembers.companies IS 'An enterprise.';

-- Permissions

ALTER TABLE groupmembers.companies OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.companies TO postgres;


-- groupmembers."groups" definition

-- Drop table

-- DROP TABLE groupmembers."groups";

CREATE TABLE groupmembers."groups" (
	groupid serial4 NOT NULL,
	"name" text NULL,
	dateid int4 NULL,
	description text NULL,
	companyid int4 NULL,
	displayid int4 NULL,
	website text NULL,
	socialid int4 NULL,
	CONSTRAINT groups_pkey PRIMARY KEY (groupid),
	CONSTRAINT group_companyid FOREIGN KEY (companyid) REFERENCES groupmembers.companies(companyid) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT group_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT group_displayid FOREIGN KEY (displayid) REFERENCES groupmembers.displays(displayid) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT group_socialid FOREIGN KEY (socialid) REFERENCES groupmembers.socialmedia(socialid) ON DELETE SET NULL ON UPDATE CASCADE
);
CREATE INDEX idx_groups_groupid ON groupmembers.groups USING btree (groupid);
COMMENT ON TABLE groupmembers."groups" IS 'A general group.';

-- Permissions

ALTER TABLE groupmembers."groups" OWNER TO postgres;
GRANT ALL ON TABLE groupmembers."groups" TO postgres;


-- groupmembers.grouptags definition

-- Drop table

-- DROP TABLE groupmembers.grouptags;

CREATE TABLE groupmembers.grouptags (
	tagid int4 NOT NULL,
	groupid int4 NOT NULL,
	CONSTRAINT grouptags_pkey PRIMARY KEY (tagid, groupid),
	CONSTRAINT tags_groupid FOREIGN KEY (groupid) REFERENCES groupmembers."groups"(groupid) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT tags_tag_id FOREIGN KEY (tagid) REFERENCES groupmembers.tags(tagid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_grouptags_groupid ON groupmembers.grouptags USING btree (groupid);
COMMENT ON TABLE groupmembers.grouptags IS 'The tags for groups.';

-- Permissions

ALTER TABLE groupmembers.grouptags OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.grouptags TO postgres;


-- groupmembers.persons definition

-- Drop table

-- DROP TABLE groupmembers.persons;

CREATE TABLE groupmembers.persons (
	personid serial4 NOT NULL,
	dateid int4 NULL,
	nameid int4 NULL,
	formernameid int4 NULL,
	gender bpchar(1) NULL,
	description text NULL,
	height int4 NULL,
	displayid int4 NULL,
	socialid int4 NULL,
	locationid int4 NULL,
	bloodtype public."bloodtypes" NULL,
	callcount int4 NULL,
	CONSTRAINT persons_pkey PRIMARY KEY (personid),
	CONSTRAINT person_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT person_displayid FOREIGN KEY (displayid) REFERENCES groupmembers.displays(displayid) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT person_formernameid FOREIGN KEY (formernameid) REFERENCES groupmembers.names(nameid) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT person_locationid FOREIGN KEY (locationid) REFERENCES groupmembers.locations(locationid) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT person_nameid FOREIGN KEY (nameid) REFERENCES groupmembers.names(nameid) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT person_socialid FOREIGN KEY (socialid) REFERENCES groupmembers.socialmedia(socialid) ON DELETE SET NULL ON UPDATE CASCADE
);
CREATE INDEX idx_person_personid ON groupmembers.persons USING btree (personid);
COMMENT ON TABLE groupmembers.persons IS 'A general person';

-- Permissions

ALTER TABLE groupmembers.persons OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.persons TO postgres;


-- groupmembers.persontags definition

-- Drop table

-- DROP TABLE groupmembers.persontags;

CREATE TABLE groupmembers.persontags (
	tagid int4 NOT NULL,
	personid int4 NOT NULL,
	CONSTRAINT persontags_pkey PRIMARY KEY (tagid, personid),
	CONSTRAINT p_tags_tag_id FOREIGN KEY (tagid) REFERENCES groupmembers.tags(tagid) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT tags_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_persontags_personid ON groupmembers.persontags USING btree (personid);
COMMENT ON TABLE groupmembers.persontags IS 'The tags for persons.';

-- Permissions

ALTER TABLE groupmembers.persontags OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.persontags TO postgres;


-- groupmembers.affiliations definition

-- Drop table

-- DROP TABLE groupmembers.affiliations;

CREATE TABLE groupmembers.affiliations (
	affiliationid serial4 NOT NULL,
	personid int4 NOT NULL,
	groupid int4 NOT NULL,
	stagename text NULL,
	active bool DEFAULT true NULL,
	CONSTRAINT affiliations_affiliationid_key UNIQUE (affiliationid),
	CONSTRAINT affiliations_pkey PRIMARY KEY (affiliationid, personid, groupid),
	CONSTRAINT affiliation_groupid FOREIGN KEY (groupid) REFERENCES groupmembers."groups"(groupid) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT affiliation_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_affiliation_affiliationid ON groupmembers.affiliations USING btree (affiliationid);
COMMENT ON TABLE groupmembers.affiliations IS 'The affiliation of a person to a group.';

-- Permissions

ALTER TABLE groupmembers.affiliations OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.affiliations TO postgres;


-- groupmembers.fandom definition

-- Drop table

-- DROP TABLE groupmembers.fandom;

CREATE TABLE groupmembers.fandom (
	groupid int4 NOT NULL,
	"name" text NULL,
	CONSTRAINT fandom_name_key UNIQUE (name),
	CONSTRAINT fandom_pkey PRIMARY KEY (groupid),
	CONSTRAINT fandom_groupid FOREIGN KEY (groupid) REFERENCES groupmembers."groups"(groupid) ON DELETE CASCADE ON UPDATE CASCADE
);
COMMENT ON TABLE groupmembers.fandom IS 'A group''s fandom name (if it exists).';

-- Permissions

ALTER TABLE groupmembers.fandom OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.fandom TO postgres;


-- groupmembers.media definition

-- Drop table

-- DROP TABLE groupmembers.media;

CREATE TABLE groupmembers.media (
	mediaid serial4 NOT NULL,
	link text NULL,
	faces int4 NULL,
	filetype text NULL,
	affiliationid int4 NULL,
	enabled bool NULL,
	nsfw bool NULL,
	CONSTRAINT media_link_affiliationid_key UNIQUE (link, affiliationid),
	CONSTRAINT media_pkey PRIMARY KEY (mediaid),
	CONSTRAINT media_affiliationid FOREIGN KEY (affiliationid) REFERENCES groupmembers.affiliations(affiliationid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_affiliationid ON groupmembers.media USING btree (affiliationid);
CREATE INDEX idx_media_mediaid ON groupmembers.media USING btree (mediaid);
COMMENT ON TABLE groupmembers.media IS 'The information about a media file.';

-- Permissions

ALTER TABLE groupmembers.media OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.media TO postgres;


-- groupmembers.affiliation_positions definition

-- Drop table

-- DROP TABLE groupmembers.affiliation_positions;

CREATE TABLE groupmembers.affiliation_positions (
	affiliationid int4 NOT NULL,
	positionid int4 NOT NULL,
	CONSTRAINT pk_affiliation_positions PRIMARY KEY (affiliationid, positionid),
	CONSTRAINT fk_affiliation_positions_affiliation FOREIGN KEY (affiliationid) REFERENCES groupmembers.affiliations(affiliationid) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_affiliation_positions_position FOREIGN KEY (positionid) REFERENCES groupmembers.positions(positionid) ON DELETE CASCADE ON UPDATE CASCADE
);
COMMENT ON TABLE groupmembers.affiliation_positions IS 'Links the positions to the affiliation.';

-- Permissions

ALTER TABLE groupmembers.affiliation_positions OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.affiliation_positions TO postgres;


-- groupmembers.automedia definition

-- Drop table

-- DROP TABLE groupmembers.automedia;

CREATE TABLE groupmembers.automedia (
	channelid int8 NOT NULL,
	affiliationid int4 NOT NULL,
	hoursafter int4 NULL,
	CONSTRAINT automedia_pkey PRIMARY KEY (channelid, affiliationid)
);
CREATE INDEX idx_automedia_affiliationid ON groupmembers.automedia USING btree (affiliationid);
COMMENT ON TABLE groupmembers.automedia IS 'Automatically post a list of affiliation ids in a channel.';

-- Permissions

ALTER TABLE groupmembers.automedia OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.automedia TO postgres;


-- groupmembers.groupaliases definition

-- Drop table

-- DROP TABLE groupmembers.groupaliases;

CREATE TABLE groupmembers.groupaliases (
	aliasid serial4 NOT NULL,
	alias text NULL,
	groupid int4 NULL,
	guildid int8 NULL,
	CONSTRAINT ensure_groupalias CHECK ((alias <> ''::text)),
	CONSTRAINT groupaliases_pkey PRIMARY KEY (aliasid),
	CONSTRAINT unique_group_alias UNIQUE (alias, groupid, guildid)
);
CREATE INDEX idx_groupaliases_groupid ON groupmembers.groupaliases USING btree (groupid);
COMMENT ON TABLE groupmembers.groupaliases IS 'The aliases of a group.';

-- Permissions

ALTER TABLE groupmembers.groupaliases OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.groupaliases TO postgres;


-- groupmembers.personaliases definition

-- Drop table

-- DROP TABLE groupmembers.personaliases;

CREATE TABLE groupmembers.personaliases (
	aliasid serial4 NOT NULL,
	alias text NULL,
	personid int4 NULL,
	guildid int8 NULL,
	CONSTRAINT ensure_personalias CHECK ((alias <> ''::text)),
	CONSTRAINT personaliases_pkey PRIMARY KEY (aliasid),
	CONSTRAINT unique_person_alias UNIQUE (alias, personid, guildid)
);
CREATE INDEX idx_personaliases_personid ON groupmembers.personaliases USING btree (personid);
COMMENT ON TABLE groupmembers.personaliases IS 'The aliases of a person.';

-- Permissions

ALTER TABLE groupmembers.personaliases OWNER TO postgres;
GRANT ALL ON TABLE groupmembers.personaliases TO postgres;


-- groupmembers.automedia foreign keys

ALTER TABLE groupmembers.automedia ADD CONSTRAINT automedia_affid FOREIGN KEY (affiliationid) REFERENCES groupmembers.affiliations(affiliationid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE groupmembers.automedia ADD CONSTRAINT automedia_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE;


-- groupmembers.groupaliases foreign keys

ALTER TABLE groupmembers.groupaliases ADD CONSTRAINT groupaliases_groupid FOREIGN KEY (groupid) REFERENCES groupmembers."groups"(groupid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE groupmembers.groupaliases ADD CONSTRAINT groupaliases_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE SET NULL ON UPDATE CASCADE;


-- groupmembers.personaliases foreign keys

ALTER TABLE groupmembers.personaliases ADD CONSTRAINT personaliases_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE groupmembers.personaliases ADD CONSTRAINT personaliases_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE;




-- Permissions

GRANT ALL ON SCHEMA groupmembers TO postgres;

-- DROP SCHEMA guessinggame;

CREATE SCHEMA guessinggame AUTHORIZATION postgres;

COMMENT ON SCHEMA guessinggame IS 'information about the guessing games.';

-- DROP SEQUENCE guessinggame.games_gameid_seq;

CREATE SEQUENCE guessinggame.games_gameid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE guessinggame.games_gameid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE guessinggame.games_gameid_seq TO postgres;
-- guessinggame.difficulty definition

-- Drop table

-- DROP TABLE guessinggame.difficulty;

CREATE TABLE guessinggame.difficulty (
	mediaid int4 NOT NULL,
	failed int4 NULL,
	correct int4 NULL,
	CONSTRAINT difficulty_pkey PRIMARY KEY (mediaid)
);
CREATE INDEX idx_difficulty_mediaid ON guessinggame.difficulty USING btree (mediaid);
COMMENT ON TABLE guessinggame.difficulty IS 'Difficulty of Media based on failed/correct guesses.';

-- Permissions

ALTER TABLE guessinggame.difficulty OWNER TO postgres;
GRANT ALL ON TABLE guessinggame.difficulty TO postgres;


-- guessinggame.filtered definition

-- Drop table

-- DROP TABLE guessinggame.filtered;

CREATE TABLE guessinggame.filtered (
	userid int8 NOT NULL,
	groupids _int4 NULL,
	personids _int4 NULL,
	CONSTRAINT filtered_pkey PRIMARY KEY (userid)
);
CREATE INDEX idx_filtered_userid ON guessinggame.filtered USING btree (userid);
COMMENT ON TABLE guessinggame.filtered IS 'The groups/persons a user has filtered to show in the guessing game.';

-- Permissions

ALTER TABLE guessinggame.filtered OWNER TO postgres;
GRANT ALL ON TABLE guessinggame.filtered TO postgres;


-- guessinggame.games definition

-- Drop table

-- DROP TABLE guessinggame.games;

CREATE TABLE guessinggame.games (
	gameid serial4 NOT NULL,
	dateid int4 NULL,
	mediaids _int4 NULL,
	statusids _int4 NULL,
	modeid int4 NULL,
	difficultyid int4 NULL,
	isnsfw bool NULL,
	CONSTRAINT games_pkey PRIMARY KEY (gameid)
);
CREATE INDEX idx_games_gameid ON guessinggame.games USING btree (gameid);
COMMENT ON TABLE guessinggame.games IS 'Information about a guessing game.';

-- Permissions

ALTER TABLE guessinggame.games OWNER TO postgres;
GRANT ALL ON TABLE guessinggame.games TO postgres;


-- guessinggame.stats definition

-- Drop table

-- DROP TABLE guessinggame.stats;

CREATE TABLE guessinggame.stats (
	userid int8 NOT NULL,
	modeid int4 NULL,
	difficultyid int4 NULL,
	value int4 NULL,
	CONSTRAINT stats_pkey PRIMARY KEY (userid)
);
COMMENT ON TABLE guessinggame.stats IS 'Stats a user has in every mode of the guessing game.';

-- Permissions

ALTER TABLE guessinggame.stats OWNER TO postgres;
GRANT ALL ON TABLE guessinggame.stats TO postgres;


-- guessinggame.filtered foreign keys

ALTER TABLE guessinggame.filtered ADD CONSTRAINT filteredgroups_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;


-- guessinggame.games foreign keys

ALTER TABLE guessinggame.games ADD CONSTRAINT gg_games_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE guessinggame.games ADD CONSTRAINT gg_games_modeid FOREIGN KEY (modeid) REFERENCES public.modes(modeid) ON DELETE SET NULL ON UPDATE CASCADE;


-- guessinggame.stats foreign keys

ALTER TABLE guessinggame.stats ADD CONSTRAINT gg_stats_modeid FOREIGN KEY (modeid) REFERENCES public.modes(modeid) ON DELETE SET NULL ON UPDATE CASCADE;




-- Permissions

GRANT ALL ON SCHEMA guessinggame TO postgres;

-- DROP SCHEMA interactions;

CREATE SCHEMA interactions AUTHORIZATION postgres;

COMMENT ON SCHEMA interactions IS 'Manages the interaction module.';

-- DROP SEQUENCE interactions.interactiontypes_typeid_seq;

CREATE SEQUENCE interactions.interactiontypes_typeid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE interactions.interactiontypes_typeid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE interactions.interactiontypes_typeid_seq TO postgres;
-- interactions.interactiontypes definition

-- Drop table

-- DROP TABLE interactions.interactiontypes;

CREATE TABLE interactions.interactiontypes (
	typeid serial4 NOT NULL,
	"name" text NULL,
	CONSTRAINT interactiontypes_name_key UNIQUE (name),
	CONSTRAINT interactiontypes_pkey PRIMARY KEY (typeid)
);
COMMENT ON TABLE interactions.interactiontypes IS 'Types of Interactions';

-- Permissions

ALTER TABLE interactions.interactiontypes OWNER TO postgres;
GRANT ALL ON TABLE interactions.interactiontypes TO postgres;


-- interactions.media definition

-- Drop table

-- DROP TABLE interactions.media;

CREATE TABLE interactions.media (
	url text NOT NULL,
	typeid int4 NULL,
	CONSTRAINT media_pkey PRIMARY KEY (url),
	CONSTRAINT media_typeid FOREIGN KEY (typeid) REFERENCES interactions.interactiontypes(typeid) ON DELETE CASCADE ON UPDATE CASCADE
);
COMMENT ON TABLE interactions.media IS 'Media URLs';

-- Permissions

ALTER TABLE interactions.media OWNER TO postgres;
GRANT ALL ON TABLE interactions.media TO postgres;


-- interactions.disabledtypes definition

-- Drop table

-- DROP TABLE interactions.disabledtypes;

CREATE TABLE interactions.disabledtypes (
	guildid int8 NOT NULL,
	interactionids _int4 NULL,
	CONSTRAINT disabledtypes_pkey PRIMARY KEY (guildid)
);
COMMENT ON TABLE interactions.disabledtypes IS 'The interaction types disabled for a guild';

-- Permissions

ALTER TABLE interactions.disabledtypes OWNER TO postgres;
GRANT ALL ON TABLE interactions.disabledtypes TO postgres;


-- interactions.disabledtypes foreign keys

ALTER TABLE interactions.disabledtypes ADD CONSTRAINT interactions_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE;




-- Permissions

GRANT ALL ON SCHEMA interactions TO postgres;


-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION postgres;

COMMENT ON SCHEMA public IS 'General Information';

-- DROP TYPE public."bloodtypes";

CREATE TYPE public."bloodtypes" AS ENUM (
	'A+',
	'A-',
	'B+',
	'B-',
	'AB+',
	'AB-',
	'O+',
	'O-');

-- DROP SEQUENCE public.apiaccess_accessid_seq;

CREATE SEQUENCE public.apiaccess_accessid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.apiaccess_accessid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.apiaccess_accessid_seq TO postgres;

-- DROP SEQUENCE public.banphrases_phraseid_seq;

CREATE SEQUENCE public.banphrases_phraseid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.banphrases_phraseid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.banphrases_phraseid_seq TO postgres;

-- DROP SEQUENCE public.customcommands_commandid_seq;

CREATE SEQUENCE public.customcommands_commandid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.customcommands_commandid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.customcommands_commandid_seq TO postgres;

-- DROP SEQUENCE public.difficulty_difficultyid_seq;

CREATE SEQUENCE public.difficulty_difficultyid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.difficulty_difficultyid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.difficulty_difficultyid_seq TO postgres;

-- DROP SEQUENCE public.eightball_responseid_seq;

CREATE SEQUENCE public.eightball_responseid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.eightball_responseid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.eightball_responseid_seq TO postgres;

-- DROP SEQUENCE public.languages_languageid_seq;

CREATE SEQUENCE public.languages_languageid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.languages_languageid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.languages_languageid_seq TO postgres;

-- DROP SEQUENCE public.modes_modeid_seq;

CREATE SEQUENCE public.modes_modeid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.modes_modeid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.modes_modeid_seq TO postgres;

-- DROP SEQUENCE public.notifications_noti_id_seq;

CREATE SEQUENCE public.notifications_noti_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.notifications_noti_id_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.notifications_noti_id_seq TO postgres;

-- DROP SEQUENCE public.reminders_id_seq;

CREATE SEQUENCE public.reminders_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.reminders_id_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.reminders_id_seq TO postgres;

-- DROP SEQUENCE public.roletypes_typeid_seq;

CREATE SEQUENCE public.roletypes_typeid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.roletypes_typeid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.roletypes_typeid_seq TO postgres;

-- DROP SEQUENCE public.sessions_sessionid_seq;

CREATE SEQUENCE public.sessions_sessionid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.sessions_sessionid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.sessions_sessionid_seq TO postgres;

-- DROP SEQUENCE public.statuses_statusid_seq;

CREATE SEQUENCE public.statuses_statusid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.statuses_statusid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.statuses_statusid_seq TO postgres;

-- DROP SEQUENCE public.timezones_id_seq;

CREATE SEQUENCE public.timezones_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.timezones_id_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.timezones_id_seq TO postgres;

-- DROP SEQUENCE public.userstatus_statusid_seq;

CREATE SEQUENCE public.userstatus_statusid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE public.userstatus_statusid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE public.userstatus_statusid_seq TO postgres;
-- public.apiaccess definition

-- Drop table

-- DROP TABLE public.apiaccess;

CREATE TABLE public.apiaccess (
	accessid serial4 NOT NULL,
	"name" text NULL,
	CONSTRAINT apiaccess_name_key UNIQUE (name),
	CONSTRAINT apiaccess_pkey PRIMARY KEY (accessid)
);
CREATE INDEX idx_api_access ON public.apiaccess USING btree (accessid);

-- Permissions

ALTER TABLE public.apiaccess OWNER TO postgres;
GRANT ALL ON TABLE public.apiaccess TO postgres;


-- public.banphrases definition

-- Drop table

-- DROP TABLE public.banphrases;

CREATE TABLE public.banphrases (
	phraseid serial4 NOT NULL,
	guildid int8 NOT NULL,
	logchannelid int8 NOT NULL,
	phrase text NULL,
	punishment text NULL,
	CONSTRAINT banphrases_pkey PRIMARY KEY (phraseid)
);
CREATE INDEX idx_banphrases_guildid ON public.banphrases USING btree (guildid);
COMMENT ON TABLE public.banphrases IS 'The ban phrases to punish a user for.';

-- Permissions

ALTER TABLE public.banphrases OWNER TO postgres;
GRANT ALL ON TABLE public.banphrases TO postgres;


-- public.channels definition

-- Drop table

-- DROP TABLE public.channels;

CREATE TABLE public.channels (
	channelid int8 NOT NULL,
	guildid int8 NULL,
	CONSTRAINT channels_pkey PRIMARY KEY (channelid)
);
CREATE INDEX idx_channels_guildid ON public.channels USING btree (guildid);

-- Permissions

ALTER TABLE public.channels OWNER TO postgres;
GRANT ALL ON TABLE public.channels TO postgres;


-- public.difficulty definition

-- Drop table

-- DROP TABLE public.difficulty;

CREATE TABLE public.difficulty (
	difficultyid serial4 NOT NULL,
	"name" text NULL,
	CONSTRAINT difficulty_name_key UNIQUE (name),
	CONSTRAINT difficulty_pkey PRIMARY KEY (difficultyid)
);

-- Permissions

ALTER TABLE public.difficulty OWNER TO postgres;
GRANT ALL ON TABLE public.difficulty TO postgres;


-- public.eightball definition

-- Drop table

-- DROP TABLE public.eightball;

CREATE TABLE public.eightball (
	responseid serial4 NOT NULL,
	response text NULL,
	CONSTRAINT eightball_pkey PRIMARY KEY (responseid)
);
COMMENT ON TABLE public.eightball IS 'Eight Ball Responses';

-- Permissions

ALTER TABLE public.eightball OWNER TO postgres;
GRANT ALL ON TABLE public.eightball TO postgres;


-- public.guilds definition

-- Drop table

-- DROP TABLE public.guilds;

CREATE TABLE public.guilds (
	guildid int8 NOT NULL,
	"name" text NULL,
	emojicount int4 NULL,
	afktimeout int4 NULL,
	icon text NULL,
	ownerid int8 NULL,
	banner text NULL,
	description text NULL,
	mfalevel int4 NULL,
	splash text NULL,
	nitrolevel int4 NULL,
	boosts int4 NULL,
	textchannelcount int4 NULL,
	voicechannelcount int4 NULL,
	categorycount int4 NULL,
	emojilimit int4 NULL,
	membercount int4 NULL,
	rolecount int4 NULL,
	shardid int4 NULL,
	createdate timestamptz NULL,
	hasbot bool NULL,
	CONSTRAINT guilds_pkey PRIMARY KEY (guildid)
);
CREATE INDEX idx_guilds_guildid ON public.guilds USING btree (guildid);
COMMENT ON TABLE public.guilds IS 'Information about guilds that have been previously associated with the bot.';

-- Permissions

ALTER TABLE public.guilds OWNER TO postgres;
GRANT ALL ON TABLE public.guilds TO postgres;


-- public.languages definition

-- Drop table

-- DROP TABLE public.languages;

CREATE TABLE public.languages (
	languageid serial4 NOT NULL,
	shortname text NULL,
	"name" text NULL,
	CONSTRAINT languages_name_key UNIQUE (name),
	CONSTRAINT languages_pkey PRIMARY KEY (languageid),
	CONSTRAINT languages_shortname_key UNIQUE (shortname)
);
CREATE INDEX idx_languages_languageid ON public.languages USING btree (languageid);
COMMENT ON TABLE public.languages IS 'The languages the bot has content for.';

-- Permissions

ALTER TABLE public.languages OWNER TO postgres;
GRANT ALL ON TABLE public.languages TO postgres;


-- public.modes definition

-- Drop table

-- DROP TABLE public.modes;

CREATE TABLE public.modes (
	modeid serial4 NOT NULL,
	"name" text NULL,
	CONSTRAINT modes_pkey PRIMARY KEY (modeid)
);
COMMENT ON TABLE public.modes IS 'The modes available for entities.';

-- Permissions

ALTER TABLE public.modes OWNER TO postgres;
GRANT ALL ON TABLE public.modes TO postgres;


-- public.notifications definition

-- Drop table

-- DROP TABLE public.notifications;

CREATE TABLE public.notifications (
	noti_id serial4 NOT NULL,
	guildid int8 NOT NULL,
	userid int8 NOT NULL,
	phrase text NULL,
	CONSTRAINT notifications_pkey PRIMARY KEY (noti_id)
);
CREATE INDEX idx_notifications_guildid_userid ON public.notifications USING btree (guildid, userid);
COMMENT ON TABLE public.notifications IS 'The user phrases to notify a user about.';

-- Permissions

ALTER TABLE public.notifications OWNER TO postgres;
GRANT ALL ON TABLE public.notifications TO postgres;


-- public.reactionroles definition

-- Drop table

-- DROP TABLE public.reactionroles;

CREATE TABLE public.reactionroles (
	messageid int8 NOT NULL,
	CONSTRAINT reactionroles_pkey PRIMARY KEY (messageid)
);
CREATE INDEX idx_reactionroles_messageid ON public.reactionroles USING btree (messageid);

-- Permissions

ALTER TABLE public.reactionroles OWNER TO postgres;
GRANT ALL ON TABLE public.reactionroles TO postgres;


-- public.roletypes definition

-- Drop table

-- DROP TABLE public.roletypes;

CREATE TABLE public.roletypes (
	typeid serial4 NOT NULL,
	"name" text NULL,
	CONSTRAINT roletypes_pkey PRIMARY KEY (typeid)
);
COMMENT ON TABLE public.roletypes IS 'The types of role (ex: muted, patron, super patron, mod, data mod)';

-- Permissions

ALTER TABLE public.roletypes OWNER TO postgres;
GRANT ALL ON TABLE public.roletypes TO postgres;


-- public.sessions definition

-- Drop table

-- DROP TABLE public.sessions;

CREATE TABLE public.sessions (
	sessionid serial4 NOT NULL,
	used int4 NULL,
	sessiondate date NULL,
	CONSTRAINT sessions_pkey PRIMARY KEY (sessionid)
);
COMMENT ON TABLE public.sessions IS 'A day by day session of the bot tracking command usage.';

-- Permissions

ALTER TABLE public.sessions OWNER TO postgres;
GRANT ALL ON TABLE public.sessions TO postgres;


-- public.stats definition

-- Drop table

-- DROP TABLE public.stats;

CREATE TABLE public.stats (
	"name" text NOT NULL,
	value int8 NULL,
	"time" timestamp DEFAULT now() NOT NULL,
	CONSTRAINT stats_pkey PRIMARY KEY (name, "time")
);
COMMENT ON TABLE public.stats IS 'Available Stats';

-- Permissions

ALTER TABLE public.stats OWNER TO postgres;
GRANT ALL ON TABLE public.stats TO postgres;


-- public.statuses definition

-- Drop table

-- DROP TABLE public.statuses;

CREATE TABLE public.statuses (
	statusid serial4 NOT NULL,
	status text NULL,
	CONSTRAINT statuses_pkey PRIMARY KEY (statusid)
);
COMMENT ON TABLE public.statuses IS 'The statuses the bot will iterate through.';

-- Permissions

ALTER TABLE public.statuses OWNER TO postgres;
GRANT ALL ON TABLE public.statuses TO postgres;


-- public.tiktokfollowage definition

-- Drop table

-- DROP TABLE public.tiktokfollowage;

CREATE TABLE public.tiktokfollowage (
	username text NOT NULL,
	userid int8 NOT NULL,
	channelid int8 NOT NULL,
	roleid int8 NULL,
	CONSTRAINT tiktokfollowage_pkey PRIMARY KEY (username, userid, channelid)
);
CREATE INDEX idx_tiktokfollowage_username ON public.tiktokfollowage USING btree (username);
COMMENT ON TABLE public.tiktokfollowage IS 'The channels/guilds that follow a tiktok account. Each record belongs to a patron.';

-- Permissions

ALTER TABLE public.tiktokfollowage OWNER TO postgres;
GRANT ALL ON TABLE public.tiktokfollowage TO postgres;


-- public.timezones definition

-- Drop table

-- DROP TABLE public.timezones;

CREATE TABLE public.timezones (
	id serial4 NOT NULL,
	shortname text NULL,
	"name" text NULL,
	CONSTRAINT timezones_name_key UNIQUE (name),
	CONSTRAINT timezones_pkey PRIMARY KEY (id)
);
CREATE INDEX idx_timezones_id ON public.timezones USING btree (id);
COMMENT ON TABLE public.timezones IS 'A list of timezones (used to be locale_by_timezones.json)';

-- Permissions

ALTER TABLE public.timezones OWNER TO postgres;
GRANT ALL ON TABLE public.timezones TO postgres;


-- public.commandusage definition

-- Drop table

-- DROP TABLE public.commandusage;

CREATE TABLE public.commandusage (
	sessionid int4 NOT NULL,
	commandname text NOT NULL,
	count int4 NULL,
	CONSTRAINT commandusage_pkey PRIMARY KEY (sessionid, commandname),
	CONSTRAINT commandusage_sessionid FOREIGN KEY (sessionid) REFERENCES public.sessions(sessionid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_commandusage_sessionid_commandname ON public.commandusage USING btree (sessionid, commandname);
COMMENT ON TABLE public.commandusage IS 'The usage of every command during a session.';

-- Permissions

ALTER TABLE public.commandusage OWNER TO postgres;
GRANT ALL ON TABLE public.commandusage TO postgres;


-- public.customcommands definition

-- Drop table

-- DROP TABLE public.customcommands;

CREATE TABLE public.customcommands (
	commandid serial4 NOT NULL,
	guildid int8 NULL,
	"name" text NULL,
	"content" text NULL,
	CONSTRAINT customcommands_pkey PRIMARY KEY (commandid),
	CONSTRAINT customcommands_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE
);
COMMENT ON TABLE public.customcommands IS 'Message IDs containing reaction roles.';

-- Permissions

ALTER TABLE public.customcommands OWNER TO postgres;
GRANT ALL ON TABLE public.customcommands TO postgres;


-- public.guildprefixes definition

-- Drop table

-- DROP TABLE public.guildprefixes;

CREATE TABLE public.guildprefixes (
	guildid int8 NOT NULL,
	prefix text NOT NULL,
	CONSTRAINT guildprefixes_pkey PRIMARY KEY (guildid, prefix),
	CONSTRAINT guildprefixes_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_guildprefixes_guildid ON public.guildprefixes USING btree (guildid);
COMMENT ON TABLE public.guildprefixes IS 'The custom prefixes for a guild.';

-- Permissions

ALTER TABLE public.guildprefixes OWNER TO postgres;
GRANT ALL ON TABLE public.guildprefixes TO postgres;


-- public.languagepacks definition

-- Drop table

-- DROP TABLE public.languagepacks;

CREATE TABLE public.languagepacks (
	languageid int4 NOT NULL,
	"label" text NOT NULL,
	message text NULL,
	CONSTRAINT languagepacks_pkey PRIMARY KEY (languageid, label),
	CONSTRAINT pack_language FOREIGN KEY (languageid) REFERENCES public.languages(languageid) ON DELETE SET NULL ON UPDATE CASCADE
);
COMMENT ON TABLE public.languagepacks IS 'The content for each language.';

-- Permissions

ALTER TABLE public.languagepacks OWNER TO postgres;
GRANT ALL ON TABLE public.languagepacks TO postgres;


-- public.logging definition

-- Drop table

-- DROP TABLE public.logging;

CREATE TABLE public.logging (
	guildid int8 NOT NULL,
	channelids _int8 NULL,
	active bool NULL,
	sendall bool NULL,
	CONSTRAINT logging_pkey PRIMARY KEY (guildid),
	CONSTRAINT logging_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE
);
COMMENT ON TABLE public.logging IS 'Guild Logging';

-- Permissions

ALTER TABLE public.logging OWNER TO postgres;
GRANT ALL ON TABLE public.logging TO postgres;


-- public.roles definition

-- Drop table

-- DROP TABLE public.roles;

CREATE TABLE public.roles (
	roleid int8 NOT NULL,
	typeids _int4 NULL,
	guildid int8 NULL,
	CONSTRAINT roles_pkey PRIMARY KEY (roleid),
	CONSTRAINT roles_guildid FOREIGN KEY (guildid) REFERENCES public.guilds(guildid) ON DELETE CASCADE ON UPDATE CASCADE
);
COMMENT ON TABLE public.roles IS 'Roles with a bot purpose.';

-- Permissions

ALTER TABLE public.roles OWNER TO postgres;
GRANT ALL ON TABLE public.roles TO postgres;


-- public.selfassignroles definition

-- Drop table

-- DROP TABLE public.selfassignroles;

CREATE TABLE public.selfassignroles (
	roleid int8 NOT NULL,
	channelid int8 NULL,
	"name" text NULL,
	CONSTRAINT selfassignroles_pkey PRIMARY KEY (roleid),
	CONSTRAINT selfassignroles_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE
);
COMMENT ON TABLE public.selfassignroles IS 'Roles that can be self assigned in a channel.';

-- Permissions

ALTER TABLE public.selfassignroles OWNER TO postgres;
GRANT ALL ON TABLE public.selfassignroles TO postgres;


-- public.tempchannels definition

-- Drop table

-- DROP TABLE public.tempchannels;

CREATE TABLE public.tempchannels (
	channelid int8 NOT NULL,
	delay int4 NULL,
	CONSTRAINT tempchannels_pkey PRIMARY KEY (channelid),
	CONSTRAINT tempchannels_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE
);
COMMENT ON TABLE public.tempchannels IS 'A self-destruct channel that removes messages after t seconds.';

-- Permissions

ALTER TABLE public.tempchannels OWNER TO postgres;
GRANT ALL ON TABLE public.tempchannels TO postgres;


-- public.twitchfollowage definition

-- Drop table

-- DROP TABLE public.twitchfollowage;

CREATE TABLE public.twitchfollowage (
	username text NOT NULL,
	channelid int8 NOT NULL,
	posted bool NULL,
	roleid int8 NULL,
	CONSTRAINT twitchfollowage_pkey PRIMARY KEY (username, channelid),
	CONSTRAINT twitchfollowage_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_twitchfollowage_username ON public.twitchfollowage USING btree (username);
CREATE INDEX idx_twitchfollowage_username_channelid ON public.twitchfollowage USING btree (username, channelid);
COMMENT ON TABLE public.twitchfollowage IS 'The channels/guilds that follow a twitch channel.';

-- Permissions

ALTER TABLE public.twitchfollowage OWNER TO postgres;
GRANT ALL ON TABLE public.twitchfollowage TO postgres;


-- public.users definition

-- Drop table

-- DROP TABLE public.users;

CREATE TABLE public.users (
	userid int8 NOT NULL,
	balance text DEFAULT '0'::text NULL,
	timezoneid int4 NULL,
	ggfilteractive bool DEFAULT false NULL,
	languageid int4 DEFAULT 8 NULL,
	xp int4 DEFAULT 0 NULL,
	CONSTRAINT users_pkey PRIMARY KEY (userid),
	CONSTRAINT users_language FOREIGN KEY (languageid) REFERENCES public.languages(languageid) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT users_timezone FOREIGN KEY (timezoneid) REFERENCES public.timezones(id) ON DELETE SET NULL ON UPDATE CASCADE
);
CREATE INDEX idx_users_userid ON public.users USING btree (userid);
COMMENT ON TABLE public.users IS 'User Information';

-- Permissions

ALTER TABLE public.users OWNER TO postgres;
GRANT ALL ON TABLE public.users TO postgres;


-- public.userstatus definition

-- Drop table

-- DROP TABLE public.userstatus;

CREATE TABLE public.userstatus (
	statusid serial4 NOT NULL,
	userid int8 NOT NULL,
	score int4 NULL,
	CONSTRAINT userstatus_pkey PRIMARY KEY (statusid, userid),
	CONSTRAINT gg_userstatus_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT us_userstatus_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_userstatus_statusid ON public.userstatus USING btree (statusid);
COMMENT ON TABLE public.userstatus IS 'The status of a user during a specific game.';

-- Permissions

ALTER TABLE public.userstatus OWNER TO postgres;
GRANT ALL ON TABLE public.userstatus TO postgres;


-- public.votes definition

-- Drop table

-- DROP TABLE public.votes;

CREATE TABLE public.votes (
	votedat timestamp NOT NULL,
	userid int8 NOT NULL,
	CONSTRAINT votes_pkey PRIMARY KEY (votedat, userid),
	CONSTRAINT votes_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Permissions

ALTER TABLE public.votes OWNER TO postgres;
GRANT ALL ON TABLE public.votes TO postgres;


-- public.apitokens definition

-- Drop table

-- DROP TABLE public.apitokens;

CREATE TABLE public.apitokens (
	userid int8 NOT NULL,
	hashed text NOT NULL,
	accessid int4 NOT NULL,
	CONSTRAINT apitokens_pkey PRIMARY KEY (userid),
	CONSTRAINT token_accessid FOREIGN KEY (accessid) REFERENCES public.apiaccess(accessid) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT token_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_api_tokens ON public.apitokens USING btree (accessid);
CREATE INDEX idx_apitokens_userid ON public.apitokens USING btree (userid);
COMMENT ON TABLE public.apitokens IS 'User IDs to their hashed API tokens';

-- Permissions

ALTER TABLE public.apitokens OWNER TO postgres;
GRANT ALL ON TABLE public.apitokens TO postgres;


-- public.apiusage definition

-- Drop table

-- DROP TABLE public.apiusage;

CREATE TABLE public.apiusage (
	"time" timestamp DEFAULT now() NOT NULL,
	userid int8 NOT NULL,
	func text NOT NULL,
	response text NULL,
	args text NULL,
	kwargs text NULL,
	CONSTRAINT apiusage_pkey PRIMARY KEY ("time", func, userid),
	CONSTRAINT usage_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
COMMENT ON TABLE public.apiusage IS 'The usage a user has to each api function..';

-- Permissions

ALTER TABLE public.apiusage OWNER TO postgres;
GRANT ALL ON TABLE public.apiusage TO postgres;


-- public.botbanned definition

-- Drop table

-- DROP TABLE public.botbanned;

CREATE TABLE public.botbanned (
	userid int8 NOT NULL,
	CONSTRAINT botbanned_pkey PRIMARY KEY (userid),
	CONSTRAINT botbanned_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_botbanned_userid ON public.botbanned USING btree (userid);
COMMENT ON TABLE public.botbanned IS 'Users that are currently banned from the bot.';

-- Permissions

ALTER TABLE public.botbanned OWNER TO postgres;
GRANT ALL ON TABLE public.botbanned TO postgres;


-- public.datamods definition

-- Drop table

-- DROP TABLE public.datamods;

CREATE TABLE public.datamods (
	userid int8 NOT NULL,
	CONSTRAINT datamods_pkey PRIMARY KEY (userid),
	CONSTRAINT datamods_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_datamods_userid ON public.datamods USING btree (userid);
COMMENT ON TABLE public.datamods IS 'Data moderators of the bot.';

-- Permissions

ALTER TABLE public.datamods OWNER TO postgres;
GRANT ALL ON TABLE public.datamods TO postgres;


-- public.lastfm definition

-- Drop table

-- DROP TABLE public.lastfm;

CREATE TABLE public.lastfm (
	userid int8 NOT NULL,
	username text NULL,
	CONSTRAINT lastfm_pkey PRIMARY KEY (userid),
	CONSTRAINT lastfm_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_lastfm_userid ON public.lastfm USING btree (userid);
COMMENT ON TABLE public.lastfm IS 'The LastFM usernames of a user.';

-- Permissions

ALTER TABLE public.lastfm OWNER TO postgres;
GRANT ALL ON TABLE public.lastfm TO postgres;


-- public.levels definition

-- Drop table

-- DROP TABLE public.levels;

CREATE TABLE public.levels (
	userid int8 NOT NULL,
	rob int4 NULL,
	daily int4 NULL,
	beg int4 NULL,
	profile int4 NULL,
	CONSTRAINT levels_pkey PRIMARY KEY (userid),
	CONSTRAINT levels_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_levels_userid ON public.levels USING btree (userid);
COMMENT ON TABLE public.levels IS 'The levels of a user.';

-- Permissions

ALTER TABLE public.levels OWNER TO postgres;
GRANT ALL ON TABLE public.levels TO postgres;


-- public.mods definition

-- Drop table

-- DROP TABLE public.mods;

CREATE TABLE public.mods (
	userid int8 NOT NULL,
	CONSTRAINT mods_pkey PRIMARY KEY (userid),
	CONSTRAINT mods_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_mods_userid ON public.mods USING btree (userid);
COMMENT ON TABLE public.mods IS 'General Moderators of the bot.';

-- Permissions

ALTER TABLE public.mods OWNER TO postgres;
GRANT ALL ON TABLE public.mods TO postgres;


-- public.patron definition

-- Drop table

-- DROP TABLE public.patron;

CREATE TABLE public.patron (
	userid int8 NOT NULL,
	CONSTRAINT patron_pk PRIMARY KEY (userid),
	CONSTRAINT patron_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_patron_userid ON public.patron USING btree (userid);
COMMENT ON TABLE public.patron IS 'Users who are a patron.';

-- Permissions

ALTER TABLE public.patron OWNER TO mujy;
GRANT ALL ON TABLE public.patron TO mujy;


-- public.proofreader definition

-- Drop table

-- DROP TABLE public.proofreader;

CREATE TABLE public.proofreader (
	userid int8 NOT NULL,
	CONSTRAINT proofreader_pk PRIMARY KEY (userid),
	CONSTRAINT proofreader_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_proofreader_userid ON public.proofreader USING btree (userid);
COMMENT ON TABLE public.proofreader IS 'Users who are a proofreader.';

-- Permissions

ALTER TABLE public.proofreader OWNER TO mujy;
GRANT ALL ON TABLE public.proofreader TO mujy;


-- public.superpatron definition

-- Drop table

-- DROP TABLE public.superpatron;

CREATE TABLE public.superpatron (
	userid int8 NOT NULL,
	CONSTRAINT superpatron_pk PRIMARY KEY (userid),
	CONSTRAINT super_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_superpatron_userid ON public.superpatron USING btree (userid);
COMMENT ON TABLE public.superpatron IS 'Users who are a super patron.';

-- Permissions

ALTER TABLE public.superpatron OWNER TO mujy;
GRANT ALL ON TABLE public.superpatron TO mujy;


-- public.translator definition

-- Drop table

-- DROP TABLE public.translator;

CREATE TABLE public.translator (
	userid int8 NOT NULL,
	CONSTRAINT translator_pk PRIMARY KEY (userid),
	CONSTRAINT translator_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_translator_userid ON public.translator USING btree (userid);
COMMENT ON TABLE public.translator IS 'Users who are a translator.';

-- Permissions

ALTER TABLE public.translator OWNER TO mujy;
GRANT ALL ON TABLE public.translator TO mujy;


-- public.reminders definition

-- Drop table

-- DROP TABLE public.reminders;

CREATE TABLE public.reminders (
	id serial4 NOT NULL,
	userid int8 NULL,
	reason text NULL,
	dateid int4 NULL,
	CONSTRAINT reminders_pkey PRIMARY KEY (id)
);
CREATE INDEX idx_reminders_id ON public.reminders USING btree (id);
COMMENT ON TABLE public.reminders IS 'All reminders that have or will be sent to a user.';

-- Permissions

ALTER TABLE public.reminders OWNER TO postgres;
GRANT ALL ON TABLE public.reminders TO postgres;


-- public.reminders foreign keys

ALTER TABLE public.reminders ADD CONSTRAINT reminders_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE public.reminders ADD CONSTRAINT reminders_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;




-- Permissions

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;


-- DROP SCHEMA unscramblegame;

CREATE SCHEMA unscramblegame AUTHORIZATION postgres;

COMMENT ON SCHEMA unscramblegame IS 'information about the unscramble games.';

-- DROP SEQUENCE unscramblegame.games_gameid_seq;

CREATE SEQUENCE unscramblegame.games_gameid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

-- Permissions

ALTER SEQUENCE unscramblegame.games_gameid_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE unscramblegame.games_gameid_seq TO postgres;
-- unscramblegame.games definition

-- Drop table

-- DROP TABLE unscramblegame.games;

CREATE TABLE unscramblegame.games (
	gameid serial4 NOT NULL,
	dateid int4 NULL,
	statusids _int4 NULL,
	modeid int4 NULL,
	difficultyid int4 NULL,
	CONSTRAINT games_pkey PRIMARY KEY (gameid)
);
CREATE INDEX idx_games_gameid_statusids ON unscramblegame.games USING btree (gameid, statusids);
COMMENT ON TABLE unscramblegame.games IS 'Information about an unscramble game.';

-- Permissions

ALTER TABLE unscramblegame.games OWNER TO postgres;
GRANT ALL ON TABLE unscramblegame.games TO postgres;


-- unscramblegame.stats definition

-- Drop table

-- DROP TABLE unscramblegame.stats;

CREATE TABLE unscramblegame.stats (
	userid int8 NULL,
	modeid int4 NULL,
	difficultyid int4 NULL,
	value int4 NOT NULL,
	CONSTRAINT stats_pkey PRIMARY KEY (value)
);
COMMENT ON TABLE unscramblegame.stats IS 'Stats a user has in every mode of the unscramble game.';

-- Permissions

ALTER TABLE unscramblegame.stats OWNER TO postgres;
GRANT ALL ON TABLE unscramblegame.stats TO postgres;


-- unscramblegame.games foreign keys

ALTER TABLE unscramblegame.games ADD CONSTRAINT us_games_dateid FOREIGN KEY (dateid) REFERENCES groupmembers.dates(dateid) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE unscramblegame.games ADD CONSTRAINT us_games_modeid FOREIGN KEY (modeid) REFERENCES public.modes(modeid) ON DELETE CASCADE ON UPDATE CASCADE;


-- unscramblegame.stats foreign keys

ALTER TABLE unscramblegame.stats ADD CONSTRAINT us_stats_modeid FOREIGN KEY (modeid) REFERENCES public.modes(modeid) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE unscramblegame.stats ADD CONSTRAINT us_stats_userid FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE ON UPDATE CASCADE;




-- Permissions

GRANT ALL ON SCHEMA unscramblegame TO postgres;