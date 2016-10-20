# mm_download
mm_download.py is a script to download daily MAPS.ME maps by mask. MAPS.ME app has a convenient download interface,
but maps are refreshed only with application release.
If you need fresh maps for mapping or to have latest changes you can download daily-updated maps.

# Usage
1) Download maps:

**python mm_download.py pattern [output_dir]**

2) Upload to your phone (for example, to /mnt/sdcard/MapsWithMe in Andoid).

# Examples

**python mm_download.py austria** - download all files for Austria to the current directory

**python mm_download.py bavaria c:\Temp** - download all files for Bavaria to c:\Temp