# ZDM (Z Download Manager) 3.0 - Technical Requirements Document (TRD.md)

**Document Status**: LOCKED & MANDATORY  
**Target Architecture**: `V3/` Clean Native Architecture (Rust Workspace)  
**Author & Publisher**: MZ Tuhin (M. Zahan) &bull; [https://zahan.pro/zdm](https://zahan.pro/zdm)  

---

## 1. Locked Dependency Baseline

| Component | Target Version | Purpose |
| :--- | :--- | :--- |
| **Rust Toolchain** | `1.80+ / 2024 Edition` | Core language standard |
| **GUI Framework** | `eframe / egui 0.37.0` | High-performance immediate-mode native GUI |
| **Windows API** | `windows-sys 0.59` | DWM backdrop, Win32 raw window handle, clipboard |
| **Network Engine** | `reqwest 0.12` (rustls-tls) | High-speed HTTP/1.1 & HTTP/2 connection pooling |
| **Async Runtime** | `tokio 1.40+` | Multi-threaded async engine & IPC named pipes |
| **Native Host** | `zdm-nmhost` | Chrome / Edge / Brave / Firefox Stdio JSON bridge |
| **Media Probe** | `yt-dlp` | Video quality enumeration & audio extraction |
| **BitTorrent** | `librqbit` | Magnet link resolution and torrent chunking |

---

## 2. Process Isolation & Silence Guarantee

To eliminate any chance of console/terminal window flashing:
1. `#![windows_subsystem = "windows"]` applied to all executable crates:
   - `crates/app`
   - `crates/nmhost`
   - `crates/cli` (when headless GUI flags are passed)
2. `CREATE_NO_WINDOW (0x0800_0000)` flag enforced on every `std::process::Command` spawned on Windows:
   - `reg.exe` registry configuration commands
   - `tasklist` running checks
   - `explorer.exe` open and folder navigation
   - External tools (`yt-dlp.exe`, `ffmpeg.exe`, `rasdial.exe`)

---

## 3. Native DWM Titlebar Glass Implementation

```rust
pub fn apply_acrylic_glass(hwnd: isize) {
    use std::ffi::c_void;
    use std::mem::size_of;
    use windows_sys::Win32::Graphics::Dwm::DwmSetWindowAttribute;

    let hwnd = hwnd as windows_sys::Win32::Foundation::HWND;
    if hwnd.is_null() {
        return;
    }

    // Windows 11: Set DWM backdrop to Acrylic (3)
    let backdrop_type: u32 = 3;
    unsafe {
        DwmSetWindowAttribute(
            hwnd,
            38, // DWMWA_SYSTEMBACKDROP_TYPE
            &backdrop_type as *const u32 as *const c_void,
            size_of::<u32>() as u32,
        );
        let dark_mode: i32 = 1;
        DwmSetWindowAttribute(
            hwnd,
            20, // DWMWA_USE_IMMERSIVE_DARK_MODE
            &dark_mode as *const i32 as *const c_void,
            size_of::<i32>() as u32,
        );
    }
}
```
