%define srcname	Synkron

%define debug_package %{nil}

Summary:	A synchronization tool with QT4 GUI
Name:		synkron
Version:	1.6.2
Release:	2
Group:		File tools
License:	GPLv2
URL:		https://sourceforge.net/projects/synkron/
Source0:	http://downloads.sourceforge.net/project/%name/%name/%version/%srcname-%{version}-src.tar.gz
Source1:	Synkron.desktop
BuildRequires:	qt4-devel >= 4:4.3 desktop-file-utils
Requires:	qt4-common >= 4:4.3

%description
Synkron is an application for folder synchronisation that allows you
to configure your synchronisations in detail. Despite having many
features, the user interface of Synkron is very user-friendly and easy
to use.

Synkron is able to synchronise multiple folders at once, analyse
folders before sync, restore overwritten or deleted files, plan
synchronisations and much more.

Synkron is a cross-platform application and runs on Mac OS X, Linux
and Windows.

Synkron is distributed under the terms of the GPL v2 licence.

%files
%doc gpl.txt readme.txt
%{_bindir}/synkron
%{_datadir}/icons/synkron/
%{_datadir}/applications/Synkron.desktop

#---------------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}-src

%build
lrelease Synkron.pro
qmake -config release
%make 

%install
#binary
install -d %{buildroot}/%{_bindir}
install -m 0755 synkron -s %{buildroot}/%{_bindir}

#icon
install -d %{buildroot}%{_datadir}/icons/%{name}
install -m 0644 images/Synkron48.png %{buildroot}/%{_datadir}/icons/%{name}


#desktop file
desktop-file-install  --dir="%{buildroot}/%{_datadir}/applications" %{SOURCE1}
# Fix perms
chmod 644  gpl.txt readme.txt
