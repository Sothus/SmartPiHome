import os
import channels.asgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'super_smartpihome.settings')
channel_layer = channel.asgi.get_channel_layer()
