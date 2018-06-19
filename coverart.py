import sacad
import asyncio
import logging
from sacad.cover import SUPPORTED_IMG_FORMATS

class CoverArt:

    def getCoverArt(self, artist, album):
        # search and download
        async_loop = asyncio.get_event_loop()
        logging.getLogger().setLevel(logging.DEBUG)
        coroutine = sacad.search_and_download(album,
                                  artist,
                                  SUPPORTED_IMG_FORMATS["jpg"],
                                  600,
                                  "cover.jpg",
                                  size_tolerance_prct=25,
                                  amazon_tlds=["co.uk"],
                                  no_lq_sources=False,
                                  async_loop=async_loop)
        future = asyncio.ensure_future(coroutine, loop=async_loop)
        async_loop.run_until_complete(future)

if __name__ == "__main__":
	art = CoverArt()
	art.getCoverArt("Metallica","Master of Puppets")
