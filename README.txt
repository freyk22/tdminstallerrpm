Darkmod installer (for tdm 2.02) - Debian Software Package

Created by
freyk
https://sites.google.com/site/freykssite01
http://forums.thedarkmod.com/user/13309-freyk/


** Introduction **
This is the source for creating a rpm softwarepackage, 
for installing the darkmod updater.
When compiled, this softwarepackage instructs the packagemanager,
to create a darkmod-folder in /usr/share/games, extracts the updater to that
folder and set the right permissions.
It also creates kde menu shortcuts to these files.

** Thanks **
Thanks thanks to:
Bikerdude
Bedhead


** Preparing build environment **
install rpm-build
go to the source-folder.
Copy folder "rpmbuild" to the home folder
And copy file "rpmmacros" also to this folder and then rename it to .rpmmacros 

** Compiling **
open the terminal and navigate to the rpmbuild folder.
Execute the following command: rpmbuild -ba SPECS/darkmod.spec
The result is a compiled RPM file inside the RPM-folder

** Bugs **
Tested with opensuse 13.2
- None found at the monment

** Changes **
0.0.4 (20160221)
- Package - changed the packagename from "TheDarkMod" to "darkmod"
- Files - Added "path" to .desktop files
- Files - Added "$SHELL" to execute command of the tdm updater shortcut.
- Files - Added .desktop files to the source package
- SPEC - Added to spec file, an uninstaller script.
- SPEC - Removed the lines who generate the desktop files
- SPEC - Added to script that the .desktop files will be copied to the correct applications folder.
- SPEC - commented out the changelog.

0.0.3 (20160217)
- Added lines to create shortcuts for the binary and updater in the kde menu

0.0.2 (date unknown)
- Cleaned up the source folder (remove old dev files)
- repackaged the Source 
- Added in Specfile, permissions
- changed in Specfile, package information

0.0.1 (date unknown)
- first build