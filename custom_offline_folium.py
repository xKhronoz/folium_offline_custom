# custom_folium_offline.py
# This module patches folium to allow offline usage by loading JavaScript and CSS from local files.

import os

import folium
import folium.plugins
from folium.elements import Element
from jinja2 import Template


class Link(Element):
    def get_code(self):
        if self.code is None:
            with open(self.url, "r", encoding="utf-8") as f:
                self.code = f.read()
        return self.code

    def to_dict(self, depth=-1, **kwargs):
        out = super().to_dict(depth=-1, **kwargs)
        out["url"] = self.url
        return out


class JavascriptLink(Link):
    _template = Template("<script>{{ this.get_code() }}</script>")

    def __init__(self, url):
        super().__init__()
        self._name = "JavascriptLink"
        self.url = url
        self.code = None


class CssLink(Link):
    _template = Template("<style>{{ this.get_code() }}</style>")

    def __init__(self, url):
        super().__init__()
        self._name = "CssLink"
        self.url = url
        self.code = None


class FoliumOfflinePatcher:
    def __init__(self, static_dir="static"):
        self.js_dir = os.path.join(static_dir, "js")
        self.css_dir = os.path.join(static_dir, "css")

    def _localize_resources(self, resource_list, target_folder):
        return [
            (name, os.path.join(target_folder, os.path.basename(url)))
            for (name, url) in resource_list
        ]

    def apply(self):
        # Patch folium elements
        folium.elements.JavascriptLink = JavascriptLink
        folium.elements.CssLink = CssLink

        # Patch default folium core resources
        folium.folium._default_js = self._localize_resources(
            folium.folium._default_js, self.js_dir
        )
        folium.folium._default_css = self._localize_resources(
            folium.folium._default_css, self.css_dir
        )
        folium.Map.default_js = folium.folium._default_js
        folium.Map.default_css = folium.folium._default_css

        # Patch plugins
        plugins_to_patch = [
            folium.plugins.MeasureControl,
            folium.plugins.Fullscreen,
            folium.plugins.MiniMap,
            folium.plugins.MousePosition,
            folium.plugins.Terminator,
            folium.plugins.Geocoder,
            folium.plugins.LocateControl,
            folium.plugins.Search,
            folium.plugins.ScrollZoomToggler,
            folium.plugins.TimestampedGeoJson,
            folium.plugins.FloatImage,
            folium.plugins.Draw,
            folium.plugins.DualMap,
            folium.plugins.BoatMarker,
            folium.plugins.AntPath,
            folium.plugins.MarkerCluster,
            folium.plugins.FeatureGroupSubGroup,
            folium.plugins.FastMarkerCluster,
            folium.plugins.BeautifyIcon,
            folium.plugins.PolyLineTextPath,
            folium.plugins.SideBySideLayers,
        ]

        for plugin in plugins_to_patch:
            if hasattr(plugin, "default_js"):
                plugin.default_js = self._localize_resources(
                    plugin.default_js, self.js_dir
                )
            if hasattr(plugin, "default_css"):
                plugin.default_css = self._localize_resources(
                    plugin.default_css, self.css_dir
                )
