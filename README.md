# ZDM (Z Download Manager) ⚡

<h2 align="center">Next-Gen High-Speed Download Manager with Native Windows Aero Glass UI</h2>

<p align="center">
  <b>Built in 100% pure Rust for extreme speed, zero memory bloat, and authentic Windows 11 Acrylic & Windows 7 Aero Glass aesthetics.</b>
</p>

<p align="center">
  <a href="https://github.com/dmzahan/ZDM/releases"><img src="https://img.shields.io/badge/Download-ZDM%20v3.0.0-0078d4?style=for-the-badge&logo=windows&logoColor=white" alt="Download ZDM for Windows"></a>
  <a href="https://github.com/dmzahan/ZDM/stargazers"><img src="https://img.shields.io/badge/Star%20on-GitHub-24292e?style=for-the-badge&logo=github&logoColor=white" alt="Star ZDM on GitHub"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-success?style=for-the-badge" alt="GPL 3.0 License"></a>
</p>

---

## 💎 What Makes ZDM Unique?

ZDM (Z Download Manager) is a modern, privacy-first, ultra-fast download manager crafted as the ultimate successor to IDM and conventional bloated downloaders.

- 🪟 **Pure Windows Aero Glass UI:** Designed with frosted translucent glass textures, specular highlights, and seamless Windows DWM integration matching Windows 11 Acrylic & Windows 7 Aero Glass.
- ⚡ **Zero Simulation High-Performance Engine:** Real multi-threaded HTTP probing, concurrent byte-range connections, dynamic resume state, and high-throughput streaming directly to disk.
- 🎯 **Aero Glass Browser Extension:** Features an elegant floating frosted-glass video/audio download pill over any HTML5 video player (YouTube, Facebook, Vimeo, TikTok, Instagram, Twitter/X, and 1,000+ sites).
- 🧩 **Universal Browser Support:** Native integration for Google Chrome, Microsoft Edge, Brave, Opera, Vivaldi, Firefox, Zen, and Chromium browsers via `com.zdm.host`.
- 📦 **Wildcard & Batch Downloader:** Supports `(*)` wildcards with custom ranges, or paste hundreds of URLs at once with real-time preview.
- 🎯 **Floating Desktop Drop Target:** Sleek Aero Glass widget for instant drag-and-drop download additions from anywhere on your desktop.
- 🛡️ **100% Free & Open Source:** Zero adware, zero telemetry tracking, no subscriptions, and no trial limits.

---

## 🚀 Quick Start & Build

### Prerequisites
- Windows 10 or 11 (x64 / ARM64)
- Rust stable (MSVC toolchain)

### Build from source
```powershell
# Clone the repository
git clone https://github.com/dmzahan/ZDM.git
cd ZDM

# Build release binary
cargo build --release -p mdm-app

# Run ZDM
cargo run --release -p mdm-app
```

---

## 🧩 Browser Extension Setup

To intercept browser downloads and enable the floating video download button:

1. Open your browser extensions page:
   - **Chrome / Brave / Opera:** `chrome://extensions`
   - **Edge:** `edge://extensions`
2. Enable **Developer mode** (top-right toggle).
3. Click **Load unpacked** and select the `extension` folder inside ZDM.
4. Pin the **ZDM** icon to your browser toolbar.

---

## 👨‍💻 Author & Contact

- **Lead Developer & Creator:** MZ Tuhin (M. Zahan) ([@dmzahan](https://github.com/dmzahan))
- **Website:** [zahan.pro](https://zahan.pro)
- **WhatsApp:** `@dmzahan`
- **GitHub:** [https://github.com/dmzahan/ZDM](https://github.com/dmzahan/ZDM)

---

## 📄 License

ZDM (Z Download Manager) is licensed under the [GNU General Public License v3.0 (GPL-3.0)](LICENSE).  
Developed and designed with authentic Windows Aero Glass aesthetics by MZ Tuhin (M. Zahan).
