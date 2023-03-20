CREATE OR REPLACE VIEW interactions.getinteractions AS
    SELECT m.typeid, url, name FROM interactions.media m LEFT JOIN interactions.interactiontypes it ON m.typeid = it.typeid;