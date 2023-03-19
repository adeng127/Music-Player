

import webbrowser
import requests

# 使用一个免费的音乐API，网址是https://api.deezer.com/
# 你可以在这里查看文档：https://developers.deezer.com/api

# 定义一个函数，根据歌曲名和歌手名，获取一首歌曲的信息和播放链接
def get_song_info(song_name, artist_name):
  # 构造一个搜索请求的URL，使用q参数来指定搜索条件
  search_url = f"https://api.deezer.com/search?q=track:\"{song_name}\" artist:\"{artist_name}\""
  # 发送请求，获取响应
  response = requests.get(search_url)
  # 检查响应状态码是否为200，表示成功
  if response.status_code == 200:
    # 解析响应内容为JSON格式
    data = response.json()
    # 检查data中是否有data键，表示搜索结果列表
    if "data" in data:
      # 获取搜索结果列表中的第一项，表示最匹配的歌曲
      song = data["data"][0]
      # 返回歌曲的信息和播放链接，包括id, title, artist, album, preview等
      return song
    else:
      # 如果没有data键，表示没有找到匹配的歌曲，返回None
      return None
  else:
    # 如果响应状态码不为200，表示请求失败，返回None
    return None

# 定义一个函数，根据播放链接，在浏览器中打开并播放音乐
def play_song(preview_url):
  # 使用webbrowser模块的open方法，打开播放链接
  webbrowser.open(preview_url)

# 调用get_song_info函数，传入歌曲名和歌手名，得到歌曲信息
# 从我的回答中获取歌曲名和歌手名
song_name = input("What is the song name? ")
artist_name = input("Who is the artist name? ")
# 调用get_song_info函数，传入歌曲名和歌手名
song_info = get_song_info(song_name, artist_name)
# 检查是否获取到了歌曲信息
if song_info is not None:
  # 打印歌曲信息
  print(f"Song ID: {song_info['id']}")
  print(f"Song Title: {song_info['title']}")
  print(f"Artist Name: {song_info['artist']['name']}")
  print(f"Album Name: {song_info['album']['title']}")
  # 获取播放链接
  preview_url = song_info["preview"]
  # 调用play_song函数，传入播放链接，在浏览器中打开并播放音乐
  play_song(preview_url)
else:
  # 如果没有获取到歌曲信息，打印提示信息
  print("Sorry, I could not find the song you requested.")



