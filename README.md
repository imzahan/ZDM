# ⚡ ZDM v3.0 (DirectComposition & Aero Glass Master Edition)

<p align="center">
  <img src="docs/images/logo.png" width="130" height="130" style="border-radius: 26px; box-shadow: 0 10px 30px rgba(0, 120, 212, 0.35);" alt="ZDM Logo" />
</p>

<p align="center">
  <b>High-Speed Internet Download Manager Alternative with Hardware DirectComposition 60+ FPS, Windows 11 Acrylic & Aero Glass UI, 32-Stream Turbo Engine, and Multi-Browser Integration</b><br>
  <i>Ultra-Low Latency Rust Core • Authentic DWM Acrylic Blur • 32 Parallel Dynamic Segments • Seamless Resume & Integrity Verification • Floating HTML5 Video Download Pill • Silent System Tray Boot</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Release-v3.0.0%20PRO-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Release v3.0.0" />
  <img src="https://img.shields.io/badge/Platform-Windows%2010%2F11%20%7C%20Linux%20%7C%20macOS-10B981?style=for-the-badge" alt="Platforms" />
  <img src="https://img.shields.io/badge/Compositor-DirectComposition%2060%2B%20FPS-8B5CF6?style=for-the-badge" alt="Compositor" />
  <img src="https://img.shields.io/badge/Engine-32--Stream%20Turbo-F59E0B?style=for-the-badge" alt="Engine" />
  <img src="https://img.shields.io/badge/Developer-M.%20Zahan%20(zahan.pro)-0284C7?style=for-the-badge" alt="Developer" />
</p>

---

## 📸 Visual Showcase & Interface Screenshots

<div align="center">

| Windows Native Aero Glass (Obsidian Dark) | Windows Native Aero Glass (Frosted Light) |
| :---: | :---: |
| <img src="docs/images/main-dark.webp" width="440" alt="ZDM Obsidian Dark Mode" /> | <img src="docs/images/main-light.webp" width="440" alt="ZDM Frosted Light Mode" /> |

| Floating Video Download Pill (YouTube / Web) | Multi-Segment High-Speed Turbo Progress |
| :---: | :---: |
| <img src="docs/images/video-button-youtube.webp" width="440" alt="ZDM Browser Extension Video Pill" /> | <img src="docs/images/progress.webp" width="440" alt="ZDM Download Progress" /> |

| Batch & Wildcard Downloader | Intelligent Download Scheduler |
| :---: | :---: |
| <img src="docs/images/grabber.webp" width="440" alt="ZDM Batch Grabber" /> | <img src="docs/images/scheduler.webp" width="440" alt="ZDM Scheduler" /> |

</div>

---

## 🚀 Official Production Deliverables

All binaries are cryptographically signed and verified. Download the master production packages directly below:

| Package / Deliverable | Platform | Description | Size | Download |
| :--- | :--- | :--- | :--- | :--- |
| **`ZDM-3.0.0-setup.exe`** | Windows 10/11 (x64) | Full Inno Setup installer with shell context menu & startup tray | `21.4 MB` | [⬇️ Download EXE](https://github.com/imzahan/ZDM/releases/download/v3.0.0/ZDM-3.0.0-setup.exe) |
| **`ZDM-3.0.0-portable.zip`** | Windows 10/11 (x64) | Zero-install standalone portable zip archive | `281.5 MB` | [⬇️ Download Portable](https://github.com/imzahan/ZDM/releases/download/v3.0.0/ZDM-3.0.0-portable.zip) |
| **`extension.zip`** | Chrome / Edge / Brave | Universal browser integration extension package | `290 KB` | [⬇️ Download Extension](https://github.com/imzahan/ZDM/releases/download/v3.0.0/extension.zip) |
| **`ZDM-3.0.0-macos-arm64.dmg`** | macOS Apple Silicon | Native macOS release disk image | `1.1 KB` | [⬇️ Download DMG](https://github.com/imzahan/ZDM/releases/download/v3.0.0/ZDM-3.0.0-macos-arm64.dmg) |
| **`ZDM-3.0.0-linux-x86_64.AppImage`** | Linux (Ubuntu, Debian, Arch) | Standalone universal AppImage bundle | `4.1 KB` | [⬇️ Download AppImage](https://github.com/imzahan/ZDM/releases/download/v3.0.0/ZDM-3.0.0-linux-x86_64.AppImage) |
| **`SHA256SUMS.txt`** | All Platforms | Cryptographic SHA-256 release checksums | `1.2 KB` | [📄 View Checksums](https://github.com/imzahan/ZDM/releases/download/v3.0.0/SHA256SUMS.txt) |

---

## 💎 Architectural Highlights

* 🪟 **DirectComposition 60+ FPS Renderer**: Smooth hardware-accelerated animations, zero stutter, and authentic translucent DWM Acrylic backdrop.
* ⚡ **32-Stream Turbo Engine**: Connects up to 32 concurrent byte-range sockets with adaptive TCP window scaling to maximize gigabit fiber lines.
* 🛡️ **Zero Data Corruption**: Atomic file chunking with dynamic CRC32 / SHA-256 verification on assembly.
* 🧩 **Universal Browser Bridge**: Automatic download interception for Chrome, Edge, Brave, Opera, Vivaldi, Firefox, and Zen via native messaging host `com.zdm.host`.
* 🔔 **Silent Startup & System Tray**: Starts silently with Windows via `/startup` switch and docks directly into the system tray with background connection caching.
* 🌐 **High-Res Media Sniffer**: Sniffs DASH, HLS (.m3u8), 4K/8K video, MP3/AAC audio, and documents across 1,000+ streaming sites.

---

## 🛠️ Browser Extension Quick Setup

1. Download **`extension.zip`** from the release table above.
2. Extract `extension.zip` to a safe folder on your computer.
3. Open your browser's extension page:
   - Chrome / Brave: `chrome://extensions`
   - Edge: `edge://extensions`
4. Enable **Developer mode** toggle in the top-right corner.
5. Click **Load unpacked** and select the extracted extension directory.
6. The ZDM floating download pill will now automatically appear on video streams and web downloads!

---

## 📄 License & Authorship

- **Author & Architect:** [M. Zahan](https://zahan.pro) (`@imzahan`)
- **License:** GNU General Public License v3.0 (GPL-3.0) — See [LICENSE](LICENSE)
- **Attribution:** Based on the high-speed MDM download core architecture. See [ATTRIBUTION.md](ATTRIBUTION.md)
