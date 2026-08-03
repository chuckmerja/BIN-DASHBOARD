# Sun River Grain Storage Dashboard (v2.0)

Interactive site-map dashboard for tracking bin hardware specs, crop inventory, and sensor logs.

## 🚀 Version 2.0 Updates
- **Decoupled Architecture**: Hardware specs (`bin-specs.js`) separated from dynamic contents (`bin-contents.js`).
- **Dynamic Crop Color Mapping**: Bins color-code based on crop contents (`EMPTY`, `WW`, `BLY`, `SW`, `LENTILS`, `GPEAS`, `YPEAS`, `PELLETS`, `UNKNOWN`).
- **Google Sheets Workflow**: Python scripts in `scripts/` convert CSV exports straight into JavaScript files.

## 🛠️ Stack
- HTML5 / CSS3 (CSS Variables)
- Vanilla JS & SVG Overlay
- Chart.js
