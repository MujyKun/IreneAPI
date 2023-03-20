CREATE OR REPLACE VIEW unscramblegame.getuss AS
    SELECT gameid, dateid, statusids, modeid, difficultyid FROM unscramblegame.games;

