# 👁️‍🕒 eye-on-the-clock 🚀

A friendly CLI departure timer to help you know exactly when to leave! 🎉

Powered by SerpApi’s Distance Matrix API—your go-to for accurate travel estimates. 🗺️✨

## 🔧 Requirements
- 🐍 Python 3 (no external dependencies required)
- 🔑 SerpApi API key in `SERP_API_KEY`
- 📍 (Optional) Custom origin in `DEPARTURE_ORIGIN` (default: `381 Yonge Street Toronto`)

## 🚀 Quick Start
```bash
# Run with a simple query:
python3 departure_timer.py "Pearson Airport by Public Transit"
```

Sample output:

```
⏰ Time to departure: 56 minutes
🎯 Destination: Pearson Airport
🚍 Transportation: Public transit
```

## 🐳 Docker

Build the Docker image:
```bash
docker build -t departure-timer .
```

Run the container (replace `<your_api_key>` and query):
```bash
docker run --rm \
  -e SERP_API_KEY=<your_api_key> \
  departure-timer "Pearson Airport by Public Transit"
```

Override default origin:
```bash
docker run --rm \
  -e SERP_API_KEY=<your_api_key> \
  -e DEPARTURE_ORIGIN="123 Main St Toronto" \
  departure-timer "Bloor & Christie by Walking"
```

## ❤️ Enjoy!

Contributions, feedback, and ⭐️ are welcome! Let's make punctuality fun. 🎈