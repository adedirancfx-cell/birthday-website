# add_songs.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday_project.settings')
django.setup()

from birthday_app.models import Music

# Clear existing
Music.objects.all().delete()
print("🗑️ Cleared existing songs\n")

# Songs list
songs = [
    {
        'title': '"Say You Won\'t Let Go" - James Arthur',
        'url': 'https://open.spotify.com/embed/track/5uCax9HTNlzGybIStD3vDh?utm_source=generator',
        'type': 'main',
        'order': 1
    },
    {
        'title': '"A Thousand Years" - Christina Perri',
        'url': 'https://open.spotify.com/embed/track/3EzfjzgNaWtTJZbxfAU3vT?utm_source=generator',
        'type': 'main',
        'order': 2
    },
    {
        'title': '"Perfect" - Ed Sheeran',
        'url': 'https://open.spotify.com/embed/track/5h5CQwgjgQrBUacsqR2zR7?utm_source=generator',
        'type': 'bonus',
        'order': 3
    }
]

# Add songs
for song in songs:
    obj, created = Music.objects.get_or_create(
        title=song['title'],
        defaults={
            'spotify_embed_url': song['url'],
            'song_type': song['type'],
            'order': song['order'],
            'is_active': True
        }
    )
    if created:
        print(f"✅ Added: {song['title']}")

print(f"\n🎵 Total songs: {Music.objects.count()}")