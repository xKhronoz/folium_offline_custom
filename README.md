# Usage

### main.py

Downloads assets of leaflet

### custom_offline_folium.py

Custom class to patch Folium for offline usage.

Patches folium to allow offline usage by loading JavaScript and CSS from local files.

#### Usage of `FoliumOfflinePatcher`

Call `FoliumOfflinePatcher("path_to_local_assets").apply()` in your main script to patch Folium to use local assets, before calling any Folium functions.

```python
# Patch Folium to use local assets
FoliumOfflinePatcher("static").apply()
```