CREATE OR REPLACE VIEW public.getusers AS
select u.userid,
	u.balance,
	u.ggfilteractive,
	u.xp,
	(p.userid is not null) as ispatron,
	(m.userid is not null) as ismod,
	(pf.userid is not null) as isproofreader,
	(t.userid is not null) as istranslator,
	(d.userid is not null) as isdatamod,
	(sp.userid is not null) as issuperpatron,
	(b.userid is not null) as isbanned,
	lang.shortname as language,
	tok.accessid as access,
	fm.username as lastfmusername,
	tz.shortname as timezone,
	l.rob as roblevel,
	l.daily as dailylevel,
	l.beg as beglevel,
	l.profile as profilelevel,
	ggf.groupids as ggfiltergroups,
	ggf.personids as ggfilterpersons
from public.users u
left join public.patron p on p.userid = u.userid
left join public.mods m on m.userid = u.userid
left join public.proofreader pf on pf.userid = u.userid
left join public.translator t on t.userid = u.userid
left join public.datamods d on d.userid = u.userid
left join public.superpatron sp on sp.userid = u.userid
left join public.botbanned b on b.userid = u.userid
left join public.languages lang on lang.languageid = u.languageid
left join public.apitokens tok on tok.userid = u.userid
left join public.lastfm fm on fm.userid = u.userid
left join public.timezones tz on tz.id = u.timezoneid
left join public.levels l on l.userid = u.userid
left join guessinggame.filtered ggf on ggf.userid = u.userid;