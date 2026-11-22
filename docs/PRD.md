# ZDM (Z Download Manager) 3.0 - Product Requirements Document (PRD.md)

**Document Status**: LOCKED & MANDATORY  
**Target Architecture**: `V3/` Clean Native Architecture (Rust eframe/egui + DWM Glass Titlebar)  
**Author & Publisher**: MZ Tuhin (M. Zahan) &bull; [https://zahan.pro/zdm](https://zahan.pro/zdm)  
**Governance**: Six-Blueprint Architecture Guardian Protocol  

---

## 1. Product Vision & Goals

ZDM (Z Download Manager) 3.0 is a professional, ultra-fast, high-precision desktop download manager designed as an authoritative modern alternative to Internet Download Manager (IDM). It is engineered natively in Rust to deliver zero-latency startup, true multi-segmented chunk streaming, seamless browser video grabbing, and an aesthetic Windows 11/10 DWM Acrylic/Mica Glass titlebar while maintaining high-contrast, crystal-clear readability for tables, dialogs, and controls.

---

## 2. Inviolable Scope Boundaries & Constraints

1. **Clean Rebrand to ZDM**:
   - Software Name: `ZDM (Z Download Manager) 3.0`
   - Creator: `MZ Tuhin (M. Zahan)`
   - Official URLs: `https://zahan.pro` and `https://zahan.pro/zdm`
   - Complete removal of all upstream contributor names, foreign sponsor links, and third-party donation addresses.
2. **Titlebar Glass Only ("titlebar ta sudhu glass koro")**:
   - The window titlebar leverages Windows DWM Acrylic/Mica backdrop with top specular sheen.
   - The main client body (download table, side category pane, menus, properties dialog) utilizes crisp, opaque, high-contrast theme styling for optimal data visibility.
3. **Help Menu & Verified Creator Identity**:
   - Dedicated Help Menu with:
     - Help Topics & Online Guide (`https://zahan.pro/zdm`)
     - Verified Creator / Developer Profile Modal (MZ Tuhin / M. Zahan)
     - About ZDM (Z Download Manager) 3.0
     - Check for Updates
     - Keyboard Shortcuts
4. **Extension Aero Glass Aesthetic & Full Parity**:
   - The browser extension popup features Windows Aero Glass styling (`backdrop-filter: blur(24px)`, glossy highlights, translucent status pills).
   - All background interception mechanics, video download buttons, and native messaging communication with `com.zdm.host` function at 100% parity.
5. **Zero Terminal Window Flashing**:
   - `#![windows_subsystem = "windows"]` and `CREATE_NO_WINDOW (0x0800_0000)` enforced on 100% of child processes (`reg`, `powershell`, tools, ffmpeg, yt-dlp). Zero conhost processes created.
6. **Strict Git Offline Policy**:
   - Strictly NO `git push`. All development remains 100% local and offline.

---

## 3. Core Functional Capabilities

- **Engine Acceleration**: Up to 32 concurrent TCP connections per file using byte-range chunk streaming.
- **Dynamic File Segment Allocation**: Real-time seek-write streaming directly to disk without intermediate memory bloat.
- **Protocol Parity**: Direct HTTP/HTTPS, FTP, Magnet, and Torrent streaming via `librqbit`.
- **Media Video Interception**: Automatic video quality sniffing via `yt-dlp` bridge and content script buttons over web video players.
- **Full 12-Tab Configuration Suite**: General, File Types, Connection, Downloads, Save To, Scheduler, Limiter, Dial-Up, Proxy, Passwords, Antivirus, Remote.
