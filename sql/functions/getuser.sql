create or replace function public.getuser(t_userid bigint)
    returns table
            (
                userid bigint,
                balance text,
                ggfilteractive boolean,
                xp integer,
                ispatron boolean,
                ismod boolean,
                isproofreader boolean,
                istranslator boolean,
                isdatamod boolean,
                issuperpatron boolean,
                isbanned boolean,
                language char(5),
                access integer,
                lastfmusername text,
                timezone text,
                roblevel integer,
                dailylevel integer,
                beglevel integer,
                profilelevel integer
            )
    language plpgsql
as
$$
begin
    RETURN QUERY SELECT u.userid,
                        u.balance,
                        u.ggfilteractive,
                        u.xp,
                        (SELECT exists(
                            SELECT 1
                            FROM public.patron
                            WHERE patron.userid = t_userid))
                            AS is_patron,
                        (SELECT exists(
                            SELECT 1
                            FROM public.mods
                            WHERE mods.userid = t_userid))
                            AS is_mod,
                        (SELECT exists(
                            SELECT 1
                            FROM public.proofreader
                            WHERE proofreader.userid = t_userid))
                            AS is_proofreader,
                        (SELECT exists(
                            SELECT 1
                            FROM public.translator
                            WHERE translator.userid = t_userid))
                            AS is_translator,
                        (SELECT exists(
                            SELECT 1
                            FROM public.datamods
                            WHERE datamods.userid = t_userid))
                            AS is_data_mod,
                        (SELECT exists(
                            SELECT 1
                            FROM public.superpatron
                            WHERE superpatron.userid = t_userid))
                            AS is_super_patron,
                        (SELECT exists(
                            SELECT 1
                            FROM public.botbanned
                            WHERE botbanned.userid = t_userid))
                            AS is_banned,
                        (SELECT shortname
                            FROM public.languages
                            WHERE u.languageid = public.languages.languageid)
                            AS language,
                        (SELECT accessid
                            FROM public.apitokens
                            WHERE u.userid = public.apitokens.userid)
                            AS accessid,
                        (SELECT username
                            FROM public.lastfm
                            WHERE u.userid = public.lastfm.userid)
                            AS lastfmuser,
                        (SELECT shortname
                            FROM public.timezones
                            WHERE u.timezoneid = public.timezones.id)
                            AS tzname,
                        l.rob, l.daily, l.beg, l.profile

    FROM users u LEFT JOIN public.levels l ON l.userid = u.userid WHERE u.userid = t_userid;
end;
$$;