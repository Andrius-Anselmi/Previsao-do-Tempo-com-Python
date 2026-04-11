<div align="center">

# Weather Forecast

### The cleanest way to get a 7-day forecast in your terminal. No API key. No account. No cloud.

&nbsp;

Every weather app wants your email. Every widget wants a subscription. Every CLI tool requires you to register for a key, wait for approval, and paste a 40-character string into a `.env` file before you can ask a simple question: *will it rain on Friday?*

This doesn't.

&nbsp;

[![Python](https://img.shields.io/badge/python-3.12+-4dc9f6?style=flat-square&labelColor=0a0e14&logo=python&logoColor=4dc9f6)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-009688?style=flat-square&labelColor=0a0e14&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Open-Meteo](https://img.shields.io/badge/data-Open--Meteo-f5a623?style=flat-square&labelColor=0a0e14)](https://open-meteo.com/)
[![License](https://img.shields.io/badge/license-MIT-b0e8ff?style=flat-square&labelColor=0a0e14)](./LICENSE)

&nbsp;

[Quick Start](#quick-start) · [How It Works](#how-it-works) · [API Reference](#api-reference) · [Accessibility](#accessibility) · [Comparison](#comparison)

&nbsp;

| | | |
|---|---|---|
| **7 days** min/max for any city on Earth | **$0** forever — Open-Meteo is free and open | **2 interfaces** terminal menu + REST API |

</div>

---

## The Problem

Weather data is everywhere. Usable weather tooling for developers is not.

OpenWeatherMap requires an API key. WeatherAPI requires registration and throttles free accounts. AccuWeather limits you to 50 calls a day. Even the ones that are technically free make you jump through hoops before you can get a single temperature reading.

[Open-Meteo](https://open-meteo.com/) is different — it's a fully open, no-auth, no-rate-limit weather API built for exactly this kind of use. It just needed a decent interface.

**Weather Forecast** is that interface. Type a city name, get a 7-day outlook, export it to PDF if you need it, or hit the REST API from any other tool. That's it.

---

## Quick Start

```bash
git clone https://github.com/your-username/weather-forecast
cd weather-forecast

python3 -m venv venv
source venv/bin/activate
pip install requests fpdf2 fastapi uvicorn

# Terminal menu
python3 main.py

# REST API
uvicorn api:app --reload
# → docs at http://localhost:8000/docs
```

No `.env`. No secrets. No setup beyond this.

---

## How It Works

Type a city. The app geocodes it, hits Open-Meteo, and renders the next 7 days — min and max temperatures per day, formatted right in your terminal.

```
┌─────────────────────────────────────────────┐
│  city name                                  │
│       │                                     │
│       ▼                                     │
│  [ geocoding ]  →  lat / lon                │
│       │                                     │
│       ▼                                     │
│  [ Open-Meteo ]  →  7-day forecast data     │
│       │                                     │
│       ├──▶  terminal menu  (main.py)        │
│       │         │                           │
│       │         └──▶  PDF export            │
│       │                                     │
│       └──▶  REST API  (api.py)              │
│                 │                           │
│                 ├──▶  GET /forecast/{city}  │
│                 └──▶  GET /forecast/{city}/pdf
└─────────────────────────────────────────────┘
```

Everything flows through `previsao.py`, which handles the API calls and data normalization. The terminal interface and REST server are independent consumers of the same core functions — so adding a new interface later is straightforward.

---

## Terminal Interface

The menu is built for keyboard navigation and real terminal use — not a quick demo, but something you'd actually leave in your workflow.

- **City search by name** — no coordinates needed
- **7-day outlook** — daily min and max, clearly formatted
- **Customizable colors** — pick the palette that works for your terminal theme
- **Accessibility modes** — high contrast and forced uppercase for low-vision use
- **PDF export** — save any forecast to a file with one keypress

---

## API Reference

Two endpoints. Both work with any city name, URL-encoded.

| Method | Route | Returns |
|--------|-------|---------|
| `GET` | `/forecast/{city}` | 7-day forecast as JSON |
| `GET` | `/forecast/{city}/pdf` | Forecast as downloadable PDF |

**Example response — `GET /forecast/tokyo`**

```json
{
  "city": "Tokyo",
  "forecast": [
    { "date": "2025-06-01", "min": 18.2, "max": 26.7 },
    { "date": "2025-06-02", "min": 17.9, "max": 25.1 },
    ...
  ]
}
```

Interactive docs with a live "try it" UI: `http://localhost:8000/docs`

---

## Accessibility

Most CLI weather tools are built for one kind of user. This one isn't.

High-contrast mode swaps the default color scheme for a palette that meets WCAG AA contrast ratios. Uppercase mode forces all output to caps — useful for screen readers and certain terminal setups that handle mixed-case text poorly. Both modes are toggled from the menu, no config files required.

---

## Project Structure

```
weather-forecast/
├── main.py        # Interactive terminal menu and color engine
├── previsao.py    # Open-Meteo integration and data normalization
├── exportar.py    # PDF generation via fpdf2
└── api.py         # FastAPI server — two endpoints, auto-documented
```

Four files. No framework magic. Easy to read, easy to fork, easy to extend.

---

## Comparison

| Tool | API key required | Free tier limit | Terminal UI | PDF export | Local |
|------|-----------------|-----------------|-------------|------------|-------|
| **Weather Forecast** | **No** | **Unlimited** | **Yes** | **Yes** | **Yes** |
| wttr.in | No | Rate limited | Partial | No | No |
| OpenWeatherMap CLI | Yes | 1,000 calls/day | Varies | No | No |
| WeatherAPI CLI | Yes | 1M calls/month | No | No | No |
| met.no tools | No | Fair use | No | No | No |

---

## Requirements

- Python 3.12+
- [`requests`](https://pypi.org/project/requests/) — HTTP calls
- [`fpdf2`](https://pypi.org/project/fpdf2/) — PDF generation
- [`fastapi`](https://fastapi.tiangolo.com/) + [`uvicorn`](https://www.uvicorn.org/) — REST server

---

## Contributing

Issues and PRs are welcome. If you add a new interface (TUI, web UI, Discord bot), open a PR — the core in `previsao.py` is already decoupled for exactly that.

## License

MIT — see [LICENSE](./LICENSE).
