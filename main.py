import sys
import iterm2


async def main(connection):
    # should be piped into this method
    anime_path = sys.stdin.read().strip()

    profile = await iterm2.Profile.async_get_default(connection)
    await profile.async_set_background_image_location(anime_path)


iterm2.run_until_complete(main)
