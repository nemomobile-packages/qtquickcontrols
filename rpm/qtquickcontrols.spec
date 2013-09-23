Name:       qt5-qtquickcontrols
Summary:    Qt Quick Controls
Version:    5.1.0
Release:    nemo1
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.xz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qtv8-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Quick Controls library

#### Build section

%prep
%setup -q -n %{name}-%{version}/qtquickcontrols

%build
export QTDIR=/usr/share/qt5
touch .git # To make sure syncqt is used

%qmake5
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake5_install

#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

#### File section

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/Controls/
%{_libdir}/qt5/qml/QtQuick/Layouts/libqquicklayoutsplugin.so
%{_libdir}/qt5/qml/QtQuick/Layouts/plugins.qmltypes
%{_libdir}/qt5/qml/QtQuick/Layouts/qmldir
