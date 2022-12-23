CREATE OR REPLACE VIEW public.getreminders AS
    SELECT id AS remindid, userid, reason, dateid FROM public.reminders;
