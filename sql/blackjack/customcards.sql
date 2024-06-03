CREATE TABLE IF NOT EXISTS blackjack.customcards
(
    id serial,
    valueid integer,
    personid integer,
    filename text,
    PRIMARY KEY (id),
    CONSTRAINT customcards_valueid FOREIGN KEY (valueid) REFERENCES blackjack.cardvalues(id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT customcards_personid FOREIGN KEY (personid) REFERENCES groupmembers.persons(personid) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE blackjack.customcards
    OWNER to postgres;
COMMENT ON TABLE blackjack.customcards
    IS 'Custom playing cards with unique backgrounds.';