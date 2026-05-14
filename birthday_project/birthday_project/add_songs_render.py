# add_songs_render.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday_project.settings')
django.setup()

from birthday_app.models import Music

# Clear existing
Music.objects.all().delete()
print("🗑️ Cleared existing songs")

# Add 3 songs
songs = [
    ('"Say You Won\'t Let Go" - James Arthur', 'https://open.spotify.com/embed/track/5uCax9HTNlzGybIStD3vDh?utm_source=generator', 'main', 1),
    ('"A Thousand Years" - Christina Perri', 'https://open.spotify.com/embed/track/3EzfjzgNaWtTJZbxfAU3vT?utm_source=generator', 'main', 2),
    ('"Perfect" - Ed Sheeran', 'https://open.spotify.com/embed/track/5h5CQwgjgQrBUacsqR2zR7?utm_source=generator', 'bonus', 3),
]

for title, url, song_type, order in songs:
    Music.objects.create(title=title, spotify_embed_url=url, song_type=song_type, order=order, is_active=True)
    print(f"✅ Added: {title}")

print(f"\n🎵 Total songs: {Music.objects.count()}")