create or replace function groupmembers.deleteposition(t_position_id integer)
    returns void
    language plpgsql
as
$$
begin
    DELETE FROM groupmembers.position WHERE positionid = t_position_id;
end;
$$;
@check_permission(permission_level=DEVELOPER)
async def add_fandom(requestor: Requestor, group_id, fandom_name) -> dict:
    """Add a fandom"""
    return await self.db.execute("SELECT * FROM groupmembers.addfandom($1, $2)", group_id, fandom_name)
