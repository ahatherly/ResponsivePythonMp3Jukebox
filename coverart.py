import sacad
import asyncio
import logging
import threading
from sacad.cover import SUPPORTED_IMG_FORMATS

class CoverArt:

    async_loop = None

    def __init__(self):
        self.async_loop = asyncio.new_event_loop()

    def getCoverArt(self, artist, album):

          # search and download
          threadID = str(threading.get_ident())
          print('Thread ID: ', threadID)

          coroutine = sacad.search_and_download(album,
                                  artist,
                                  SUPPORTED_IMG_FORMATS["jpg"],
                                  400,
                                  "/tmp/cover.jpg",
                                  size_tolerance_prct=25,
                                  amazon_tlds=["co.uk"],
                                  no_lq_sources=False,
                                  async_loop=self.async_loop)
          future = asyncio.ensure_future(coroutine, loop=self.async_loop)
          self.async_loop.run_until_complete(future)

if __name__ == "__main__":
	art = CoverArt()
	art.getCoverArt("Metallica","Master of Puppets")
