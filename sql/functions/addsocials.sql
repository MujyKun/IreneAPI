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