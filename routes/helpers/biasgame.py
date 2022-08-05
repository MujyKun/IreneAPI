import asyncio
import concurrent.futures
import os
from typing import Optional

from . import (
    self,
    check_permission,
    OWNER,
    DEVELOPER,
    SUPER_PATRON,
    FRIEND,
    USER,
    is_int64,
)

from PIL import Image

from models import Requestor

from resources.keys import avatar_location, bias_game_location, image_host

from random import randint


DIR_FILE_LIMIT = 2


def blocking_remove_oldest_files():
    """Remove the oldest files in the bias game directory if it surpasses the file limit."""
    from os import listdir
    from os.path import getctime

    files = listdir(bias_game_location)
    if len(files) < DIR_FILE_LIMIT:
        return

    webp_files = [
        f"{bias_game_location}{file_name}"
        for file_name in files
        if file_name.endswith(".webp")
    ]
    sorted_by_oldest_files = sorted(webp_files, key=getctime)
    _ = [
        os.unlink(file_path)
        for file_path in sorted_by_oldest_files[0 : DIR_FILE_LIMIT // 2]
    ]


def blocking_merge_images(merge_name, first_loc, second_loc):
    final_saved_path = f"{bias_game_location}{merge_name}"
    image_url = image_host + f"bias_game/{merge_name}"

    if os.path.exists(final_saved_path):
        return image_url
    else:
        blocking_remove_oldest_files()

    with Image.open(f"images/versus.png") as versus_image, Image.open(
        first_loc
    ) as first_idol_image, Image.open(second_loc) as second_idol_image:
        # define the dimensions
        idol_image_width = 150
        idol_image_height = 150
        first_image_area = (0, 0)
        second_image_area = (versus_image.width - idol_image_width, 0)
        image_size = (idol_image_width, idol_image_height)

        # resize the idol images
        first_idol_image = first_idol_image.resize(image_size)
        second_idol_image = second_idol_image.resize(image_size)

        # add the idol images onto the VS image.
        versus_image.paste(first_idol_image, first_image_area)
        versus_image.paste(second_idol_image, second_image_area)

        # save the versus image.
        versus_image.save(final_saved_path)
        return image_url


def blocking_generate_bracket(game_info: dict):
    num_of_rounds = len(game_info)
    if num_of_rounds < 3:
        # TODO: exception
        raise Exception
    keys_to_slice = [i for i in range(num_of_rounds - 2, num_of_rounds + 1)]

    round_info = {key: game_info[str(key)] for key in keys_to_slice}

    def resize_images(fp_img, fp_size, sp_img, sp_size):
        return fp_img.resize(fp_size), sp_img.resize(sp_size)

    def paste_image(fp_img, fp_area, sp_img, sp_area):
        # fp = first person, sp = second person
        bracket.paste(fp_img, fp_area)
        bracket.paste(sp_img, sp_area)

    final_winner: Optional[int] = None

    bracket_counter = 1
    with Image.open("images/bracket8.png") as bracket:
        for round_number, pvps in round_info.items():
            for pvp in pvps:
                fp = pvp["player_one"]
                sp = pvp["player_two"]
                fp_bracket_info = _stored_bracket_positions[bracket_counter]
                sp_bracket_info = _stored_bracket_positions[bracket_counter + 1]
                bracket_counter += 2
                final_winner = pvp["winner"]
                with Image.open(
                    f"{avatar_location}{fp}_IDOL.png"
                ) as first_person_img, Image.open(
                    f"{avatar_location}{sp}_IDOL.png"
                ) as second_person_image:
                    first_person_img, second_person_image = resize_images(
                        first_person_img,
                        fp_bracket_info["img_size"],
                        second_person_image,
                        sp_bracket_info["img_size"],
                    )

                    paste_image(
                        first_person_img,
                        fp_bracket_info["pos"],
                        second_person_image,
                        sp_bracket_info["pos"],
                    )

        p_info = _stored_bracket_positions[bracket_counter]
        file_name = f"t_{randint(10000,50000)}_{randint(10000,50000)}.webp"
        final_bracket_path = f"{bias_game_location}{file_name}"
        with Image.open(f"{avatar_location}{final_winner}_IDOL.png") as p_image:
            p_image = p_image.resize(p_info["img_size"])
            bracket.paste(p_image, p_info["pos"])
            bracket.save(final_bracket_path)
            return image_host + f"bias_game/{file_name}"


@check_permission(permission_level=DEVELOPER)
async def generate_pvp(
    requestor: Requestor, first_file_name: str, second_file_name: str
):
    """Generate a PvP image for the bias game."""
    with concurrent.futures.ThreadPoolExecutor() as pool:
        merge_name = (
            first_file_name[: first_file_name.find(".")]
            + "_"
            + second_file_name[: second_file_name.find(".")]
            + ".webp"
        )

        first_file_location = avatar_location + first_file_name
        second_file_location = avatar_location + second_file_name
        future = pool.submit(
            blocking_merge_images, merge_name, first_file_location, second_file_location
        )
        while not future.done():
            await asyncio.sleep(0)

    final_image_url: Optional[str] = future.result()
    return {"results": final_image_url}


@check_permission(permission_level=DEVELOPER)
async def get_winners(requestor: Requestor, user_id: int, limit: int = 15):
    """Get the winners of a bias game for a certain user."""
    is_int64(limit)
    is_int64(user_id)
    return await self.db.fetch(
        "SELECT personid, wins FROM biasgame.getbgwinners WHERE userid = $1 ORDER BY wins "
        "DESC LIMIT $2",
        user_id,
        limit,
    )


@check_permission(permission_level=DEVELOPER)
async def upsert_wins(requestor: Requestor, user_id: int, person_id: int):
    is_int64(user_id)
    is_int64(person_id)
    return await self.db.execute(
        "SELECT biasgame.upsertbgwin($1, $2)", user_id, person_id
    )


@check_permission(permission_level=DEVELOPER)
async def generate_bracket(requestor: Requestor, game_info):
    """Generate a bracket image for the bias game."""
    with concurrent.futures.ThreadPoolExecutor() as pool:
        future = pool.submit(blocking_generate_bracket, game_info)
        while not future.done():
            await asyncio.sleep(0)

    final_image_url: Optional[str] = future.result()
    return {"results": final_image_url}


_stored_bracket_positions = {
    1: {"img_size": (50, 50), "pos": (30, 515)},
    2: {"img_size": (50, 50), "pos": (100, 515)},
    3: {"img_size": (50, 50), "pos": (165, 515)},
    4: {"img_size": (50, 50), "pos": (230, 515)},
    5: {"img_size": (50, 50), "pos": (320, 515)},
    6: {"img_size": (50, 50), "pos": (390, 515)},
    7: {"img_size": (50, 50), "pos": (455, 515)},
    8: {"img_size": (50, 50), "pos": (525, 515)},
    9: {"img_size": (75, 75), "pos": (55, 380)},
    10: {"img_size": (75, 75), "pos": (185, 380)},
    11: {"img_size": (75, 75), "pos": (340, 380)},
    12: {"img_size": (75, 75), "pos": (475, 380)},
    13: {"img_size": (100, 100), "pos": (110, 225)},
    14: {"img_size": (100, 100), "pos": (390, 225)},
    15: {"img_size": (134, 130), "pos": (235, 55)},
}
