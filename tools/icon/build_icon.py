"""Builds every app icon size from art/zdm_aero_glass_v3.png (3D Aero Glass Z Icon).

- 16, 20, 24, 32, 48, 64, 128, 256 px: Authentic Lanczos anti-aliased scaling
- Writes crates/app/assets/icons/app/zdm-<size>.png, zdm.ico (all sizes),
  extension icons, and mirrors mdm-<size>.png / mdm.ico for safety.
Run from repository root: python tools/icon/build_icon.py
"""

from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "art" / "zdm_aero_glass_v3.png"
APP = ROOT / "crates" / "app" / "assets" / "icons" / "app"
EXT = ROOT / "extension" / "icons"
SIZES = [16, 20, 24, 32, 48, 64, 128, 256]


def square(im: Image.Image) -> Image.Image:
    w, h = im.size
    s = max(w, h)
    out = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    out.paste(im, ((s - w) // 2, (s - h) // 2), im)
    return out


def main() -> None:
    src = Image.open(SRC).convert("RGBA")
    sq = square(src)
    icons = {}
    for size in SIZES:
        resized = sq.resize((size, size), Image.LANCZOS)
        icons[size] = resized
        resized.save(APP / f"zdm-{size}.png")
        resized.save(APP / f"mdm-{size}.png")

    big = icons[256]
    for ico_name in ("zdm.ico", "mdm.ico"):
        big.save(
            APP / ico_name,
            format="ICO",
            sizes=[(s, s) for s in SIZES],
            append_images=[icons[s] for s in SIZES if s != 256],
        )

    for size in (16, 32, 48, 128):
        icons[size].save(EXT / f"icon-{size}.png")

    print("Successfully built ZDM Aero Glass icons:", ", ".join(str(s) for s in SIZES))


if __name__ == "__main__":
    main()
