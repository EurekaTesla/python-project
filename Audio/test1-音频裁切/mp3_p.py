from pydub import AudioSegment



# # 先将 m4a 文件转为 mp3 文件
# def trans_m4a_to_other(filepath, hz):
#     song = AudioSegment.from_file(filepath)
#     song.export("Newsound." + str(hz), format=str(hz))
#
#
# # 参数1：音频路径， 参数2：转换后的格式
# trans_m4a_to_other("test.m4a", "mp3")
#
#

# mp3进行截取
#sourceName = "Newsound"
sourceName = "test1"

# 1s=1000ms
SECOND = 1000

# 加载mp3文件
input_music = AudioSegment.from_mp3(sourceName + '.mp3')
sound_time = input_music.duration_seconds
# 截取音频最后3000毫秒前的内容
#output_music = input_music[:sound_time - 3000]
# 截取前63分钟音频
output_music = input_music[:2*SECOND]
# 保存前2s的音频 前面为保存的路径，后面为保存的格式
output_music.export(sourceName + '_p.mp3', format='mp3')