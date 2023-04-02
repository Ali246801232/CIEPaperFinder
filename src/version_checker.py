# Function to check program version.

import requests  # to make HTTP requests to GitHub API

from popups import show_version  # to create error popup

#  Function to compare the current version with the latest version
def compare_version(current_version):
    # Fetch latest version from GitHub API
    repo = "Ali246801232/CIEPaperFinder"
    url = f"https://api.github.com/repos/{repo}/releases"

    # Check for latest version
    response = requests.get(url)
    if response.status_code == 200:
        releases = response.json()
        if releases:
            latest_version = releases[0]["tag_name"]
            # Compare versions and display message accordingly
            if latest_version != current_version:
                show_version(latest_version)
            return 0, "Success"
        else:
            return 1, "No releases were found. How did you even get the program?"
    else:
        return 1, "Failed to fetch version. You can continue to use the program, but it is recommended to check GitHub for newer versions. You can find the link to the repository by clicking the 'About CIEPaperFinder' button."
