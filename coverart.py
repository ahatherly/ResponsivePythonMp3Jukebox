import sacad

class CoverArt:

    def getCoverArt(self, artist, album):
        # search and download

        """
        sacad.search_and_download(album,
                                  artist,
                                  "JPEG",
                                  600,
                                  "/tmp/cover.jpg",
                                  size_tolerance_prct=25,
                                  amazon_tlds="",
                                  no_lq_sources=False,
                                  async_loop="")
        """
        args = []
        print(sacad.cl_main(args))

