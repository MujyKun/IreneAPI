CREATE OR REPLACE VIEW public.getusers AS
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
                        l.rob as roblevel, l.daily as dailylevel, l.beg as beglevel, l.profile as profilelevel
    FROM users u LEFT JOIN public.levels l ON l.userid = u.userid;