import docker

# Connect to Docker daemon
client = docker.from_env()

# List all images
images = client.images.list()

# Delete all images
for image in images:
    try:
        print(f"Removing image: {image.id}")
        client.images.remove(image.id, force=True)
    except Exception as e:
        print(f"Failed to remove {image.id}: {e}")
