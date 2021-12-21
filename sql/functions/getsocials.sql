create or replace function groupmembers.getsocials(t_socialid integer)
    returns table
            (
                t_twitter text,
                t_youtube text,
                t_melon text,
                t_instagram text,
                t_vlive text,
                t_spotify text,
                t_fancafe text,
                t_facebook text,
                t_tiktok text
            )
    language plpgsql
as
$$

begin
    RETURN QUERY SELECT twitter, youtube, melon, instagram, vlive, spotify, fancafe, facebook, tiktok
                 FROM groupmembers.socialmedia
                 WHERE socialid = t_socialid;
end;
$$;
