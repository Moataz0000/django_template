from django.templatetags.static import static

UNFOLD = {
    "SITE_TITLE": "elearning Admin Prod",
    "SITE_HEADER": "elearning",
    "SHOW_HISTORY": True,
    # "SITE_URL": "",
    "LOGIN": {
        "image": lambda request: static("images/login.png"),
    },
    "STYLES": [
        lambda request: static("css/style.css"),
    ],
    "SCRIPTS": [
        lambda request: static("js/script.js"),
    ],
    "SITE_SYMBOL": "anchor",
    "SITE_ICON": {
        "light": lambda request: static("images/identity.png"),
        "dark": lambda request: static("images/identity.png"),
    },
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "48x48",
            "type": "image/svg+xml",
            "href": lambda request: static("images/identity.png"),
        },
    ],
    "DASHBOARD_CALLBACK": "common.insights.dashboard_callback.dashboard_callback",
    "COLORS": {
        "primary": {
            "50": "235 245 255",
            "100": "207 232 252",
            "200": "174 216 248",
            "300": "140 199 244",
            "400": "100 181 240",
            "500": "60 162 236",
            "600": "30 144 232",
            "700": "20 126 204",
            "800": "15 108 176",
            "900": "10 90 148",
            "950": "5 72 120",
        },
    },
}
