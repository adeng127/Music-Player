

import webbrowser
import requests

# ʹ��һ����ѵ�����API����ַ��https://api.deezer.com/
# �����������鿴�ĵ���https://developers.deezer.com/api

# ����һ�����������ݸ������͸���������ȡһ�׸�������Ϣ�Ͳ�������
def get_song_info(song_name, artist_name):
  # ����һ�����������URL��ʹ��q������ָ����������
  search_url = f"https://api.deezer.com/search?q=track:\"{song_name}\" artist:\"{artist_name}\""
  # �������󣬻�ȡ��Ӧ
  response = requests.get(search_url)
  # �����Ӧ״̬���Ƿ�Ϊ200����ʾ�ɹ�
  if response.status_code == 200:
    # ������Ӧ����ΪJSON��ʽ
    data = response.json()
    # ���data���Ƿ���data������ʾ��������б�
    if "data" in data:
      # ��ȡ��������б��еĵ�һ���ʾ��ƥ��ĸ���
      song = data["data"][0]
      # ���ظ�������Ϣ�Ͳ������ӣ�����id, title, artist, album, preview��
      return song
    else:
      # ���û��data������ʾû���ҵ�ƥ��ĸ���������None
      return None
  else:
    # �����Ӧ״̬�벻Ϊ200����ʾ����ʧ�ܣ�����None
    return None

# ����һ�����������ݲ������ӣ���������д򿪲���������
def play_song(preview_url):
  # ʹ��webbrowserģ���open�������򿪲�������
  webbrowser.open(preview_url)

# ����get_song_info����������������͸��������õ�������Ϣ
# ���ҵĻش��л�ȡ�������͸�����
song_name = input("What is the song name? ")
artist_name = input("Who is the artist name? ")
# ����get_song_info����������������͸�����
song_info = get_song_info(song_name, artist_name)
# ����Ƿ��ȡ���˸�����Ϣ
if song_info is not None:
  # ��ӡ������Ϣ
  print(f"Song ID: {song_info['id']}")
  print(f"Song Title: {song_info['title']}")
  print(f"Artist Name: {song_info['artist']['name']}")
  print(f"Album Name: {song_info['album']['title']}")
  # ��ȡ��������
  preview_url = song_info["preview"]
  # ����play_song���������벥�����ӣ���������д򿪲���������
  play_song(preview_url)
else:
  # ���û�л�ȡ��������Ϣ����ӡ��ʾ��Ϣ
  print("Sorry, I could not find the song you requested.")



