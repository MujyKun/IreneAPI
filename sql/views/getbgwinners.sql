CREATE OR REPLACE VIEW biasgame.getbgwinners AS
    SELECT personid, userid, wins from biasgame.winners;