import json

with open('/home/dinika/sem7/IR+project/lyrics/lyrics/song_lyrics4.json') as ob:
    data = json.load(ob)

with open('/home/dinika/sem7/IR+project/lyrics/lyrics/song_lyrics4_sinhala.json', 'w') as ob1:
    json.dump(data, ob1, ensure_ascii=False)

