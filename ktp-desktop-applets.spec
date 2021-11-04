#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ktp-desktop-applets
Version  : 21.08.3
Release  : 33
URL      : https://download.kde.org/stable/release-service/21.08.3/src/ktp-desktop-applets-21.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.3/src/ktp-desktop-applets-21.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.3/src/ktp-desktop-applets-21.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: ktp-desktop-applets-data = %{version}-%{release}
Requires: ktp-desktop-applets-lib = %{version}-%{release}
Requires: ktp-desktop-applets-license = %{version}-%{release}
Requires: ktp-desktop-applets-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package data
Summary: data components for the ktp-desktop-applets package.
Group: Data

%description data
data components for the ktp-desktop-applets package.


%package lib
Summary: lib components for the ktp-desktop-applets package.
Group: Libraries
Requires: ktp-desktop-applets-data = %{version}-%{release}
Requires: ktp-desktop-applets-license = %{version}-%{release}

%description lib
lib components for the ktp-desktop-applets package.


%package license
Summary: license components for the ktp-desktop-applets package.
Group: Default

%description license
license components for the ktp-desktop-applets package.


%package locales
Summary: locales components for the ktp-desktop-applets package.
Group: Default

%description locales
locales components for the ktp-desktop-applets package.


%prep
%setup -q -n ktp-desktop-applets-21.08.3
cd %{_builddir}/ktp-desktop-applets-21.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636066612
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1636066612
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktp-desktop-applets
cp %{_builddir}/ktp-desktop-applets-21.08.3/COPYING %{buildroot}/usr/share/package-licenses/ktp-desktop-applets/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/ktp-desktop-applets-21.08.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/ktp-desktop-applets/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/ktp-desktop-applets-21.08.3/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/ktp-desktop-applets/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd clr-build
%make_install
popd
%find_lang plasma_applet_org.kde.ktp-chat
%find_lang plasma_applet_org.kde.person
%find_lang plasma_applet_org.kde.ktp-contactlist

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/plasma-applet-org.kde.ktp-chat.desktop
/usr/share/kservices5/plasma-applet-org.kde.ktp-contactlist.desktop
/usr/share/kservices5/plasma-applet-org.kde.person.desktop
/usr/share/plasma/plasmoids/org.kde.ktp-chat/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.ktp-chat/contents/ui/ActionDelegate.qml
/usr/share/plasma/plasmoids/org.kde.ktp-chat/contents/ui/ChatWidget.qml
/usr/share/plasma/plasmoids/org.kde.ktp-chat/contents/ui/ConversationDelegate.qml
/usr/share/plasma/plasmoids/org.kde.ktp-chat/contents/ui/ConversationDelegateButton.qml
/usr/share/plasma/plasmoids/org.kde.ktp-chat/contents/ui/FullChatList.qml
/usr/share/plasma/plasmoids/org.kde.ktp-chat/contents/ui/OutgoingDelegate.qml
/usr/share/plasma/plasmoids/org.kde.ktp-chat/contents/ui/TextDelegate.qml
/usr/share/plasma/plasmoids/org.kde.ktp-chat/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.ktp-chat/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.ktp-contactlist/contents/ui/ContactList.qml
/usr/share/plasma/plasmoids/org.kde.ktp-contactlist/contents/ui/ListContactDelegate.qml
/usr/share/plasma/plasmoids/org.kde.ktp-contactlist/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.ktp-contactlist/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.person/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.person/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.person/contents/ui/Person.qml
/usr/share/plasma/plasmoids/org.kde.person/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.person/contents/ui/settingsGeneral.qml
/usr/share/plasma/plasmoids/org.kde.person/metadata.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/qml/org/kde/ktpchat/libktpchatplugin.so
/usr/lib64/qt5/qml/org/kde/ktpchat/qmldir
/usr/lib64/qt5/qml/org/kde/ktpcontactlist/libktpcontactlistplugin.so
/usr/lib64/qt5/qml/org/kde/ktpcontactlist/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktp-desktop-applets/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/ktp-desktop-applets/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/ktp-desktop-applets/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f plasma_applet_org.kde.ktp-chat.lang -f plasma_applet_org.kde.person.lang -f plasma_applet_org.kde.ktp-contactlist.lang
%defattr(-,root,root,-)

