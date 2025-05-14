import json

with open("tracks.json", "r", encoding="utf-8") as f:
    tracks = json.load(f)

latest = tracks[0]
rest = tracks[1:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Soundtrack50</title>
</head>
<body>
""")
    f.write(f'''
<h1>Soundtrack #{latest["number"]}: {latest["title"]} by {latest["artist"]}</h1>
<p>{latest["description"]}</p>
''')
    f.write("<ul>")
    for track in rest:
        f.write(f"<li>#{track['number']} - {track['title']} by {track['artist']}</li>")
    f.write("</ul></body></html>")