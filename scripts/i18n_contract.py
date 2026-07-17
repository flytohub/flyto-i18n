"""Shared Flyto2 i18n contract used by build, validation, and SEO tooling."""

from __future__ import annotations

from copy import deepcopy


PROJECT_DIRS = [
    "cloud",
    "modules",
    "landing",
    "shared",
    "app",
    "code",
    "console",
    "data",
    "engine",
]

LOCALE_PRIORITY = [
    "en",
    "zh-TW",
    "zh-CN",
    "ja",
    "ko",
    "fr",
    "es",
    "de",
    "pt-BR",
    "it",
    "vi",
    "th",
    "id",
    "hi",
    "tr",
    "pl",
]

LANGUAGE_META = {
    "en": {
        "name": "English",
        "native": "English",
        "region": "US",
        "hreflang": "en",
        "og_locale": "en_US",
        "flag": "us.svg",
        "direction": "ltr",
    },
    "zh-TW": {
        "name": "Traditional Chinese",
        "native": "繁體中文",
        "region": "TW",
        "hreflang": "zh-TW",
        "og_locale": "zh_TW",
        "flag": "tw.svg",
        "direction": "ltr",
    },
    "zh-CN": {
        "name": "Simplified Chinese",
        "native": "简体中文",
        "region": "CN",
        "hreflang": "zh-CN",
        "og_locale": "zh_CN",
        "flag": "cn.svg",
        "direction": "ltr",
    },
    "ja": {
        "name": "Japanese",
        "native": "日本語",
        "region": "JP",
        "hreflang": "ja",
        "og_locale": "ja_JP",
        "flag": "jp.svg",
        "direction": "ltr",
    },
    "ko": {
        "name": "Korean",
        "native": "한국어",
        "region": "KR",
        "hreflang": "ko",
        "og_locale": "ko_KR",
        "flag": "kr.svg",
        "direction": "ltr",
    },
    "es": {
        "name": "Spanish",
        "native": "Español",
        "region": "ES",
        "hreflang": "es",
        "og_locale": "es_ES",
        "flag": "es.svg",
        "direction": "ltr",
    },
    "fr": {
        "name": "French",
        "native": "Français",
        "region": "FR",
        "hreflang": "fr",
        "og_locale": "fr_FR",
        "flag": "fr.svg",
        "direction": "ltr",
    },
    "de": {
        "name": "German",
        "native": "Deutsch",
        "region": "DE",
        "hreflang": "de",
        "og_locale": "de_DE",
        "flag": "de.svg",
        "direction": "ltr",
    },
    "pt": {
        "name": "Portuguese",
        "native": "Português",
        "region": "PT",
        "hreflang": "pt",
        "og_locale": "pt_PT",
        "flag": "pt.svg",
        "direction": "ltr",
    },
    "pt-BR": {
        "name": "Portuguese (Brazil)",
        "native": "Português (Brasil)",
        "region": "BR",
        "hreflang": "pt-BR",
        "og_locale": "pt_BR",
        "flag": "br.svg",
        "direction": "ltr",
    },
    "it": {
        "name": "Italian",
        "native": "Italiano",
        "region": "IT",
        "hreflang": "it",
        "og_locale": "it_IT",
        "flag": "it.svg",
        "direction": "ltr",
    },
    "ru": {
        "name": "Russian",
        "native": "Русский",
        "region": "RU",
        "hreflang": "ru",
        "og_locale": "ru_RU",
        "flag": "ru.svg",
        "direction": "ltr",
    },
    "th": {
        "name": "Thai",
        "native": "ภาษาไทย",
        "region": "TH",
        "hreflang": "th",
        "og_locale": "th_TH",
        "flag": "th.svg",
        "direction": "ltr",
    },
    "vi": {
        "name": "Vietnamese",
        "native": "Tiếng Việt",
        "region": "VN",
        "hreflang": "vi",
        "og_locale": "vi_VN",
        "flag": "vn.svg",
        "direction": "ltr",
    },
    "ar": {
        "name": "Arabic",
        "native": "العربية",
        "region": "SA",
        "hreflang": "ar",
        "og_locale": "ar_SA",
        "flag": "sa.svg",
        "direction": "rtl",
    },
    "hi": {
        "name": "Hindi",
        "native": "हिन्दी",
        "region": "IN",
        "hreflang": "hi",
        "og_locale": "hi_IN",
        "flag": "in.svg",
        "direction": "ltr",
    },
    "id": {
        "name": "Indonesian",
        "native": "Bahasa Indonesia",
        "region": "ID",
        "hreflang": "id",
        "og_locale": "id_ID",
        "flag": "id.svg",
        "direction": "ltr",
    },
    "ms": {
        "name": "Malay",
        "native": "Bahasa Melayu",
        "region": "MY",
        "hreflang": "ms",
        "og_locale": "ms_MY",
        "flag": "my.svg",
        "direction": "ltr",
    },
    "nl": {
        "name": "Dutch",
        "native": "Nederlands",
        "region": "NL",
        "hreflang": "nl",
        "og_locale": "nl_NL",
        "flag": "nl.svg",
        "direction": "ltr",
    },
    "pl": {
        "name": "Polish",
        "native": "Polski",
        "region": "PL",
        "hreflang": "pl",
        "og_locale": "pl_PL",
        "flag": "pl.svg",
        "direction": "ltr",
    },
    "tr": {
        "name": "Turkish",
        "native": "Türkçe",
        "region": "TR",
        "hreflang": "tr",
        "og_locale": "tr_TR",
        "flag": "tr.svg",
        "direction": "ltr",
    },
    "uk": {
        "name": "Ukrainian",
        "native": "Українська",
        "region": "UA",
        "hreflang": "uk",
        "og_locale": "uk_UA",
        "flag": "ua.svg",
        "direction": "ltr",
    },
}

LOCALE_NAMES = {locale: meta["name"] for locale, meta in LANGUAGE_META.items()}

REGION_MAP = {
    "en": "US",
    "en-US": "US",
    "en-GB": "GB",
    "en-AU": "AU",
    "zh": "TW",
    "zh-TW": "TW",
    "zh-CN": "CN",
    "zh-HK": "HK",
    "ja": "JP",
    "ja-JP": "JP",
    "ko": "KR",
    "ko-KR": "KR",
    "fr": "FR",
    "fr-FR": "FR",
    "de": "DE",
    "de-DE": "DE",
    "es": "ES",
    "es-ES": "ES",
    "it": "IT",
    "it-IT": "IT",
    "pt": "PT",
    "pt-BR": "BR",
    "pt-PT": "PT",
    "hi": "IN",
    "hi-IN": "IN",
    "vi": "VN",
    "vi-VN": "VN",
    "th": "TH",
    "th-TH": "TH",
    "id": "ID",
    "id-ID": "ID",
    "tr": "TR",
    "tr-TR": "TR",
    "pl": "PL",
    "pl-PL": "PL",
    "ru": "RU",
    "ru-RU": "RU",
}


def language_meta(locale: str) -> dict:
    """Return a complete metadata record for a locale."""
    default_region = locale.split("-")[-1].upper() if "-" in locale else locale[:2].upper()
    default = {
        "name": locale,
        "native": locale,
        "region": default_region,
        "hreflang": locale,
        "og_locale": f"{locale.split('-')[0]}_{default_region}",
        "flag": f"{default_region.lower()}.svg",
        "direction": "ltr",
    }
    meta = deepcopy(LANGUAGE_META.get(locale, default))
    for key, value in default.items():
        meta.setdefault(key, value)
    return meta


def locale_sort_key(locale: str) -> tuple[int, str]:
    """Sort known locales by Flyto2 launch priority, then unknown locales by code."""
    if locale in LOCALE_PRIORITY:
        return (LOCALE_PRIORITY.index(locale), locale)
    return (len(LOCALE_PRIORITY), locale)


def build_locale_meta(locales: list[str]) -> dict:
    """Build the CDN locale metadata document consumed by public surfaces."""
    ordered_locales = sorted(locales, key=locale_sort_key)
    return {
        "version": "2.0.0",
        "description": "Shared locale metadata for Flyto2 projects: flags, regions, display names, hreflang, and Open Graph locale codes.",
        "flagBaseUrl": "/flags",
        "cdnFlagUrl": "https://raw.githubusercontent.com/flytohub/flyto-i18n/main/dist/flags",
        "defaultLocale": "en",
        "xDefaultLocale": "en",
        "locales": {
            locale: language_meta(locale)
            for locale in ordered_locales
        },
        "regionMap": REGION_MAP,
    }
