# ZDM (Z Download Manager) 3.0 - Data & Wire Protocol Schemas (schema.md)

**Document Status**: LOCKED & MANDATORY  
**Target Architecture**: `V3/` Clean Native Architecture  
**Author & Publisher**: MZ Tuhin (M. Zahan) &bull; [https://zahan.pro/zdm](https://zahan.pro/zdm)  

---

## 1. Native Messaging Wire Framing (`com.zdm.host`)

Standard WebExtension Native Messaging protocol over Standard Input / Output:

```
+--------------------------+-------------------------------------+
| 4-byte Length (u32-LE)   | UTF-8 JSON Payload                  |
+--------------------------+-------------------------------------+
```

### Action Intercept Wire Payload
```json
{
  "action": "download",
  "url": "https://example.com/archive.zip",
  "filename": "archive.zip",
  "cookies": "session=xyz; token=abc",
  "referrer": "https://example.com/downloads",
  "user_agent": "Mozilla/5.0 ...",
  "post_data": null
}
```

---

## 2. Options Schema (`options.json` / `settings.toml`)

Stored in `data/options.json` (portable) or `%APPDATA%\zdm\settings.toml`:

```toml
[general]
startup = false
clipboard_monitor = true
alt_click_capture = true

[connection]
max_connections = 8
speed_limit = 0

[file_types]
extensions = "00* 3DM 3DS 3GP 3MF 7Z AAB AAC ABC ACE AFDESIGN AFPHOTO AI AIF AIFF APE APK APKM APKS APPIMAGE APPX APPXBUNDLE ARJ ARROW ARW ASF AU AVI AVRO AZW AZW3 BAK BAM BIN BLEND BZ BZ2 C4D CAB CAF CBR CBZ CCD CHD CKPT CPIO CR2 CR3 CRAM CSO DAE DAT DCM DDS DEB DFF DIVX DJVU DMG DNG DOC DOCX DSF DWG DXF EPS EPUB EXE EXR F3D F4V FASTA FASTQ FB2 FBX FEATHER FIG FITS FLAC FLATPAK FQ GCODE GCZ GEM GGML GGUF GLB GLTF GPKG GRIB GRIB2 GZ GZIP H5 HDF5 HDR IGES IGS IMG INDD IPA ISO ISZ JAR JOBLIB JSONL KERAS KRA LAS LAZ LLAMAFILE LWO LZ LZ4 LZH LZMA M2T M2TS M2V M4A M4B M4V MA MAT MAX MB MBTILES MDF MDS MID MIDI MKA MKV MLMODEL MOBI MOV MP3 MP4 MPA MPE MPEG MPG MSI MSIX MSIXBUNDLE MSP MSU MTS MXF NC NDJSON NEF NEMO NII NPY NPZ NRG NSP NSZ NUPKG OBJ ODP ODS ODT OGG OGM OGV ONNX OPUS ORC ORF OTF OVA OVF PAK PARQUET PB PBF PDF PICKLE PK3 PK4 PKG PKL PLJ PLY POTX PPS PPSX PPT PPTX PSB PSD PT PTH QCOW QCOW2 QT R0* R1* R2* R3* R4* R5* R6* R7* R8* R9* RA RAF RAR RDS RM RMVB RPM RTF RUN RVZ RW2 SAFETENSORS SEA SF2 SFZ SHP SIT SITX SKETCH SKP SLDASM SLDPRT SNAP SQLITE SQLITE3 STEP STL STP TAR TBZ TBZ2 TFLITE TGA TGZ TIF TIFF TLZ TORRENT TTA TTC TTF TXT TXZ TZST UNITYPACKAGE USD USDA USDC USDZ VDB VDI VHD VHDX VMDK VOB VPK VSIX WAV WBFS WEBM WHL WIM WMA WMV WRL WTV WUA WV X3D XAPK XCF XCI XLS XLSB XLSM XLSX XZ Z Z0* ZIP ZIPX ZPR ZST ZTL"
ignored_sites = "*.youtube.com *.googlevideo.com update.microsoft.com *.windowsupdate.com live.com"
```
