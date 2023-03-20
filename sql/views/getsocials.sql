CREATE OR REPLACE VIEW groupmembers.getsocials AS
    SELECT socialid, twitter, youtube, melon, instagram, vlive, spotify, fancafe, facebook, tiktok
    FROM groupmembers.socialmedia;