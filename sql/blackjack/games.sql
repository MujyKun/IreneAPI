CREATE TABLE IF NOT EXISTS blackjack.games
(
    gameid serial,
    channelid bigint,
    statusids integer[],
    active boolean,
    PRIMARY KEY (gameid),
    CONSTRAINT games_channelid FOREIGN KEY (channelid) REFERENCES public.channels(channelid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE blackjack.games
    OWNER to postgres;
COMMENT ON TABLE blackjack.games
    IS 'The active and inactive blackjack games.';