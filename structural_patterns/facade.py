from dataclasses import dataclass


@dataclass
class VideoFile:
    filename: str


class OggCompressionCode:
    pass


class MPEG4CompressionCode:
    pass


class CodecFactory:
    def extract(self, video_file):
        print(f'Extracted codec to {video_file}')

        return 'codec'


class BitrateReader:
    def read(self, filename, source_codec):
        print(f'Reading bitrate {filename}')

        return 'Read buffer'

    def convert(self, buffer, destination_codec):
        print(f'Converting bitrate')
        
        return 'converted buffer'

class AudioMixer:
    def fix(self, pre_result):
        print('Mix the audio with the video - Final result')


# Facade class
class VideoConverter:
    def convert(self, filename, format):
        video_file = VideoFile(filename)
        source_codec = CodecFactory().extract(video_file)

        if format == 'mp4':
            destination_codec = MPEG4CompressionCode()
        else:
            destination_codec = OggCompressionCode()
        
        bitrate_reader = BitrateReader()
        buffer = bitrate_reader.read(filename, source_codec)
        pre_result = bitrate_reader.convert(buffer, destination_codec)
        result = AudioMixer().fix(pre_result)

        return result


if __name__ == '__main__':
    convertor = VideoConverter()
    mp4_file = convertor.convert('seiya.ogg', 'mp4')
