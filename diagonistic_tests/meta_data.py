import subprocess
from logging.logger import logger


def get_instance_tags():
    """Retrieve tags associated with the EC2 instance using curl."""
    try:
        # Execute curl command to fetch tags associated with the instance
        tags_response = subprocess.run(
            ["curl", "-s", "http://169.254.169.254/latest/meta-data/tags/instance"],
            capture_output=True,
            text=True,
        )
        if tags_response.returncode == 0:
            tags = tags_response.stdout.split("\n")
            tags = {
                tag: subprocess.run(
                    [
                        "curl",
                        "-s",
                        f"http://169.254.169.254/latest/meta-data/tags/instance/{tag}",
                    ],
                    capture_output=True,
                    text=True,
                ).stdout.replace("\n", "")
                for tag in tags
            }  # Tags are returned as newline-separated values
            return tags
        else:
            print("Failed to retrieve instance tags.")
            return None
    except Exception as e:
        print(f"Error retrieving instance tags: {e}")
        return None


instance_tags = get_instance_tags()
if instance_tags:
    print("Instance tags:")
    for tag in instance_tags:
        print(tag)
        print(instance_tags[tag])
else:
    print("No instance tags found.")
