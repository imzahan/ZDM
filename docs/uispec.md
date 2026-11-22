# ZDM (Z Download Manager) 3.0 - UI Specification & Visual Design Tokens (uispec.md)

**Document Status**: LOCKED & MANDATORY  
**Target Architecture**: `V3/` Clean Native Architecture  
**Author & Publisher**: MZ Tuhin (M. Zahan) &bull; [https://zahan.pro/zdm](https://zahan.pro/zdm)  

---

## 1. Titlebar Glass Specification ("titlebar ta sudhu glass koro")

The main window titlebar uses Windows Desktop Window Manager (DWM) Acrylic/Mica hardware-accelerated composition while keeping the body solid and crisp:

| Component | Rendering Specification | Visual Value |
| :--- | :--- | :--- |
| **DWM Attribute** | `DWMWA_SYSTEMBACKDROP_TYPE (38)` | `3` (Acrylic) or `2` (Mica) |
| **Titlebar Background** | Shaded Translucent Gradient | `rgba(16, 24, 38, 0.45)` to `rgba(24, 36, 56, 0.55)` |
| **Top Sheen Line** | Inset specular line | `1px solid rgba(255, 255, 255, 0.35)` |
| **Window Caption Icon** | ZDM Aero Glass Z Icon | 16x16 / 24x24 / 32x32 multi-resolution |
| **Title Typography** | System DirectWrite / Segoe UI Variable | 12px, Weight 600, Color `#ffffff` |
| **Caption Buttons** | Minimize, Maximize, Close | Native hit-tested with standard Windows hover/active states |

---

## 2. Main Window Client Area (Solid & High-Contrast)

To ensure 100% data legibility without text blurring or washed-out backgrounds:

| UI Region | Light Mode Token | Dark Mode Token |
| :--- | :--- | :--- |
| **Window Client BG** | `#f8fafc` | `#181c24` |
| **Toolbar Background** | `#ffffff` | `#1f242e` |
| **Category Sidebar** | `#f1f5f9` | `#141820` |
| **Download Table Row** | Alternating `#ffffff` / `#f8fafc` | Alternating `#181c24` / `#1c212b` |
| **Selected Row** | `#0078d4` (Text: `#ffffff`) | `#0078d4` (Text: `#ffffff`) |
| **Status Bar** | `#e2e8f0` | `#161a22` |
| **Speed Graph** | High-contrast Emerald Green `#10b981` with grid lines |

---

## 3. Browser Extension Aero Glass Specification (`popup.css`)

The browser extension retains the modern Aero Glass aesthetic matching ZDM:

```css
:root {
  --bg: linear-gradient(135deg, rgba(16, 28, 48, 0.28) 0%, rgba(8, 18, 34, 0.18) 100%);
  --text: #f2f7ff;
  --muted: #94a3b8;
  --edge: rgba(255, 255, 255, 0.28);
  --edge-shadow: rgba(0, 0, 0, 0.35);
  --field: linear-gradient(180deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.02) 100%);
  --field-border: rgba(255, 255, 255, 0.20);
  --accent: #38bdf8;
  --accent-grad: linear-gradient(180deg, rgba(56, 189, 248, 0.9) 0%, rgba(2, 132, 199, 0.95) 100%);
  --accent-text: #041021;
  --ok: #4ade80;
  --bad: #f87171;
  --warn: #facc15;
  --glass-gloss: inset 0 1px 0 rgba(255, 255, 255, 0.25);
  --glass-shadow: 0 6px 24px rgba(0, 0, 0, 0.45);
}
```

- **Popup Dimensions**: 310px width, dynamic height.
- **Glass Blur**: `backdrop-filter: blur(24px) saturate(190%) contrast(102%)`.
- **Status Indicator**: Animated glowing dot (Green = Connected, Red = Disconnected, Yellow = Intercepting).
