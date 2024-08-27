from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from random import choice


# The interface of a remote service
class ThirdPartyYoutubeLib(ABC):
    @abstractmethod
    def list_videos(self):
        pass

    @abstractmethod
    def get_video_info(self, id):
        pass

    @abstractmethod
    def download_video(self, id):
        pass


class ThirdPartyYoutubeClass(ThirdPartyYoutubeLib):
    def list_videos(self):
        print('Getting the video list from Youtube API')
    
    def get_video_info(self, id):
        print(f'Get metadata from Youtube API about a video, with id: {id}')
    
    def download_video(self, id):
        print(f'Download a video file from YouTube API, with id: {id}')


@dataclass
class CachedYoutubeClass(ThirdPartyYoutubeLib):
    service: ThirdPartyYoutubeLib
    # Reference: https://stackoverflow.com/questions/53632152/why-cant-dataclasses-have-mutable-defaults-in-their-class-attributes-declaratio
    list_cache: list = field(default_factory=list)
    video_cache: str = None
    need_reset: bool = False

    def list_videos(self):
        if self.list_cache == [] or self.need_reset:
            self.list_cache = self.service.list_videos()
        
        return self.list_cache

    def get_video_info(self, id):
        if self.video_cache == None or self.need_reset:
            self.video_cache = self.service.get_video_info(id)
        
        return self.video_cache
    
    def download_video(self, id):
        if not self.downdload_exists(id) or self.need_reset:
            self.service.download_video(id)

    def _download_exists(self):
        return choice(True, False)


@dataclass
class YoutubeManager:
    service: ThirdPartyYoutubeLib

    def render_video_page(self, id):
        info = self.service.get_video_info(id)

        return info

    def render_list_panel(self):
        video_list = self.service.list_videos()

        return video_list

    def react_on_user_input(self, id):
        self.render_video_page(id)
        self.render_list_panel()


if __name__ == '__main__':
    concrete_youtube_class = ThirdPartyYoutubeClass()
    proxy_youtube_class = CachedYoutubeClass(concrete_youtube_class)

    manager = YoutubeManager(proxy_youtube_class)
    manager.react_on_user_input(id='xc343fgg')
