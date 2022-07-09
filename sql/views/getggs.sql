CREATE OR REPLACE VIEW guessinggame.getggs AS
    SELECT gameid, dateid, mediaids, statusids, modeid, difficultyid, isnsfw FROM guessinggame.games;