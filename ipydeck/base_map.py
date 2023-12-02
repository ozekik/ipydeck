class BaseMap:
    pass


class CartoBaseMap(BaseMap):
    base_url = "https://basemaps.cartocdn.com/gl/{basemap}-gl-style/style.json"

    VOYAGER = base_url.replace("{basemap}", "voyager")
    POSITRON = base_url.replace("{basemap}", "positron")
    DARK_MATTER = base_url.replace("{basemap}", "dark-matter")
    VOYAGER_NOLABELS = base_url.replace("{basemap}", "voyager-nolabels")
    POSITRON_NOLABELS = base_url.replace("{basemap}", "positron-nolabels")
    DARK_MATTER_NOLABELS = base_url.replace("{basemap}", "dark-matter-nolabels")

    short_names = {
        "light": POSITRON,
        "dark": DARK_MATTER,
        "road": VOYAGER,
        # satellite
        "light_no_labels": POSITRON_NOLABELS,
        "dark_no_labels": DARK_MATTER_NOLABELS,
    }


DefaultBaseMap = CartoBaseMap
