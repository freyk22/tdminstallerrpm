#defines
%define _target_cpu i586
#%define _target_cpu x86_64

#Packge information
Summary: The Dark Mod, a stealth first person shooter
Name: darkmod
Version: 2.04
Release: 1
License: GPL
Group: Games
#SOURCE0 : %{name}-%{version}.tar.gz
SOURCE0 : darkmod-%{version}.tar.gz
URL: http://www.thedarkmod.com
Vendor: Broken Glass Studios
Packager: Freek, Freyk, Borgerink

#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRoot: %{_tmppath}/darkmod-%{version}-%{release}-root

%description
%{summary}.
Get more info at www.thedarkmod.com.

WARNING - This package installs only the TDM updater.

IMPORTANT - Please run the tdm updater after installation.

This packages creates the darkmod folder, put the TDM updater in there and set some shortcuts.
After the installation, the updater needs to run mannualy to download the required TDM-files.

RPM Packed by Freyk.


%prep
%setup -q

%build
# Empty section.

%install
rm -rf %{buildroot}
install -d $RPM_BUILD_ROOT/usr/share/games/darkmod
install -d $RPM_BUILD_ROOT/usr/share/games/darkmod/gfx
install AUTHORS.txt $RPM_BUILD_ROOT/usr/share/games/darkmod/AUTHORS.txt
install description.txt $RPM_BUILD_ROOT/usr/share/games/darkmod/description.txt
install LICENSE.txt $RPM_BUILD_ROOT/usr/share/games/darkmod/LICENSE.txt
install TDM_icon.ico $RPM_BUILD_ROOT/usr/share/games/darkmod/gfx/TDM_icon.ico
install TDM_icon.png $RPM_BUILD_ROOT/usr/share/games/darkmod/gfx/TDM_icon.png
install tdm_update.linux $RPM_BUILD_ROOT/usr/share/games/darkmod/tdm_update.linux
install TheDarkMod.desktop $RPM_BUILD_ROOT/usr/share/games/darkmod/TheDarkMod.desktop
install TheDarkMod-Updater.desktop $RPM_BUILD_ROOT/usr/share/games/darkmod/TheDarkMod-Updater.desktop

%clean
rm -rf %{buildroot}

%files
%dir %attr(0776, nobody, users) /usr/share/games/darkmod
%defattr(0666,nobody, users)
/usr/share/games/darkmod/AUTHORS.txt
/usr/share/games/darkmod/description.txt
/usr/share/games/darkmod/LICENSE.txt
/usr/share/games/darkmod/gfx/TDM_icon.ico
/usr/share/games/darkmod/gfx/TDM_icon.png
/usr/share/games/darkmod/TheDarkMod-Updater.desktop
/usr/share/games/darkmod/TheDarkMod.desktop
%attr(0777, nobody, users) /usr/share/games/darkmod/tdm_update.linux
%dir %attr(0776, nobody, users) /usr/share/games/darkmod/gfx

%post 
# Update KDE menu so the icons are added immediately after install
cp /usr/share/games/darkmod/TheDarkMod-Updater.desktop /usr/share/applications/TheDarkMod-Updater.desktop
cp /usr/share/games/darkmod/TheDarkMod.desktop /usr/share/applications/TheDarkMod.desktop
#update-menus


%postun
#remove folder
rm -rf /usr/share/games/darkmod/
rm /usr/share/applications/TheDarkMod-Updater.desktop
rm /usr/share/applications/TheDarkMod.desktop


# Update KDE menu so icon is removed immediately after uninstalling
#update-menus

#%changelog
# * Sun Jan 31 2016  freyk <team@thedarmod.com> 1.0-1
# - Second Build
# * Sun Jan 31 2016  freyk <team@thedarkmod.com> 1.0-2
# -blaat