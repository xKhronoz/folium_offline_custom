import os
from urllib.request import urlopen

# List of URLs to download
urls_to_download = [
    "https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js",
    "https://code.jquery.com/jquery-3.7.1.min.js",
    "https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js",
    "https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css",
    "https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css",
    "https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css",
    "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css",
    "https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/leaflet.markercluster.js",
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/MarkerCluster.css",
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/MarkerCluster.Default.css",
    "https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/images/layers-2x.png",
    "https://unpkg.com/leaflet@1.9.3/dist/images/layers.png",
    "https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/images/marker-icon-2x.png",
    "https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/images/marker-icon.png",
    "https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/images/marker-shadow.png",
    "https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/images/markers-shadow@2x.png",
    "https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/images/markers-soft@2x.png",
    "https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/images/markers-soft.png",
    "https://netdna.bootstrapcdn.com/bootstrap/3.0.0/fonts/glyphicons-halflings-regular.woff",
    "https://netdna.bootstrapcdn.com/bootstrap/3.0.0/fonts/glyphicons-halflings-regular.ttf",
    "https://netdna.bootstrapcdn.com/bootstrap/3.0.0/fonts/glyphicons-halflings-regular.svg",
    "https://netdna.bootstrapcdn.com/bootstrap/3.0.0/fonts/glyphicons-halflings-regular.eot",
    "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/webfonts/fa-solid-900.woff2",
]

dest_path = os.path.join(os.path.dirname(__file__), "downloaded_assets")


def download_url_to_folder(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.basename(url.split("?")[0])
    output_path = os.path.join(folder, filename)
    print(f"Downloading {url} -> {output_path}")
    # Download as binary for all file types
    contents = urlopen(url).read()
    with open(output_path, "wb") as f:
        f.write(contents)


if __name__ == "__main__":
    print(f"Downloading files to {dest_path}")
    for url in urls_to_download:
        download_url_to_folder(url, dest_path)
