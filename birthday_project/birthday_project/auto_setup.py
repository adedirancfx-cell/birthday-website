"""
WSGI config for birthday_project project.
"""

import os
import sys

# Add your project directory to the path
sys.path.append('/opt/render/project/src/birthday_project')

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday_project.settings')

# Run auto setup BEFORE creating application
try:
    print("=" * 50)
    print("🚀 WSGI: Running auto setup...")
    print("=" * 50)
    
    # Import and run setup
    import auto_setup
    
    # Try to run Django setup
    import django
    django.setup()
    
    # Run migrations if needed
    from django.core.management import call_command
    from django.db import connection
    from django.contrib.auth import get_user_model
    
    # Check if auth_user table exists
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1 FROM auth_user LIMIT 1")
        cursor.fetchone()
        
except Exception as e:
    print(f"⚠️ Setup note: {e}")
    print("Will run migrations on first request")

# Create WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

print("✅ WSGI application ready")