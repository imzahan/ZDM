# ZDM (Z Download Manager) 3.0 - Sequential Implementation Plan (plan.md)

**Document Status**: LOCKED & MANDATORY  
**Target Architecture**: `V3/` Clean Native Architecture  
**Author & Publisher**: MZ Tuhin (M. Zahan) &bull; [https://zahan.pro/zdm](https://zahan.pro/zdm)  

---

## 1. Master Phased Implementation Roadmap

```
+-----------------------------------------------------------------------------------+
| PHASE 1: BLUEPRINTS LOCK & WORKSPACE INITIALIZATION                               |
| [x] Clean-wipe V3 directory                                                        |
| [x] Generate 6 Blueprints (PRD, appflow, uispec, TRD, schema, plan) in V3/docs/    |
| [ ] Copy native crates (app, cli, cnl, crash, debrid, engine, extract, geo,        |
|     ipc, labserver, mcp, nmhost, remote, tools, torrent) and Cargo workspace into V3|
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| PHASE 2: COMPLETE REBRANDING & CONTRIBUTOR REMOVAL                                |
| [ ] Audit all crates for "Mister Download Manager" / "MDM" and rebrand to "ZDM"   |
| [ ] Purge all upstream contributor lists and foreign sponsor/donation links       |
| [ ] Integrate MZ Tuhin (M. Zahan) Verified Creator profile & links in Help/About   |
| [ ] Verify documentation links point to https://zahan.pro/zdm                     |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| PHASE 3: TITLEBAR GLASS IMPLEMENTATION                                            |
| [ ] Verify DWM Acrylic/Mica titlebar backdrop in crates/app/src/win32.rs          |
| [ ] Ensure client area remains solid, crisp, and high-contrast                    |
| [ ] Add specular gloss sheen to titlebar in winui.rs                              |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| PHASE 4: EXTENSION AERO GLASS DESIGN & SEAMLESS IPC                               |
| [ ] Ensure popup.html and popup.css utilize modern Aero Glass styling             |
| [ ] Verify background.js and video.js register com.zdm.host cleanly               |
| [ ] Ensure 100% video grabber and download interception parity                    |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| PHASE 5: PROCESS ISOLATION & COMPILATION                                          |
| [ ] Verify #![windows_subsystem = "windows"] and CREATE_NO_WINDOW across all tools|
| [ ] Run cargo check --all in V3                                                   |
| [ ] Run cargo build --release in V3                                               |
| [ ] Assemble portable distribution in V3/dist/ZDM-3.0.0-portable/                 |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| PHASE 6: RIGOROUS EMPIRICAL VERIFICATION & GIT HYGIENE                            |
| [ ] Test launch zdm.exe from portable folder                                      |
| [ ] Verify 0 terminal windows flash                                               |
| [ ] Verify Help menu, Creator Profile, and About dialog                           |
| [ ] Strict Git Hygiene: ZERO git push                                             |
+-----------------------------------------------------------------------------------+
```
