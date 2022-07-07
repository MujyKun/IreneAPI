CREATE OR REPLACE VIEW guessinggame.getggs AS
    SELECT gameid, dateid, mediaids, statusids, modeid, difficulty, isnsfw FROM guessinggame.games;