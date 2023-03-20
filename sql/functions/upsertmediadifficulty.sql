create or replace function guessinggame.upsertmediadifficulty(media_id integer, failed_guesses integer, correct_guesses integer)
    returns void
    language plpgsql
as
$$
begin
    INSERT INTO guessinggame.difficulty(mediaid, failed, correct) VALUES (media_id, failed_guesses, correct_guesses)
    ON CONFLICT (mediaid) DO UPDATE SET failed = failed_guesses, correct = correct_guesses WHERE guessinggame.difficulty.mediaid = media_id;
end;
$$;