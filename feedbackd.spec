%define libname %mklibname %{name} 0
%define develname %mklibname -d %{name}

Name:           feedbackd
Version:        0.0.0+git20211018
Release:        2
Summary:        Feedback library for GNOME

License:        GPLv3+
URL:            https://source.puri.sm/Librem5/feedbackd
Source0:        https://source.puri.sm/Librem5/feedbackd/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  vala
BuildRequires:  dbus-daemon
Requires: %{libname}%{?_isa} = %{version}-%{release}

%description
feedbackd provides a DBus daemon (feedbackd) to act on events to provide
haptic, visual and audio feedback. It offers a library (libfeedback) and
GObject introspection bindings to ease using it from applications.


%package -n %{libname}
Summary: Library for %{name}

%description -n %{libname}
The lib%{name} package contains libraries for %{name}


%package -n %{develname}
Summary: Development files for %{name}
Requires: %{libname}%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install
install -D -m 644 debian/feedbackd.udev %{buildroot}%{_udevrulesdir}/90-feedbackd.rules

%files
%{_bindir}/fbcli
%{_libexecdir}/feedbackd
%{_libexecdir}/fbd-ledctrl
%{_udevrulesdir}/90-feedbackd.rules
%{_datadir}/dbus-1/interfaces/org.sigxcpu.Feedback.xml
%{_datadir}/dbus-1/services/org.sigxcpu.Feedback.service
%{_datadir}/feedbackd
%{_datadir}/glib-2.0/schemas/org.sigxcpu.feedbackd.gschema.xml

%files -n %{libname}
%{_libdir}/libfeedback-0.0.so.0
%{_libdir}/girepository-1.0/Lfb-0.0.typelib

%files -n %{develname}
%{_libdir}/libfeedback-0.0.so
%{_includedir}/libfeedback-0.0/
%{_datadir}/vala/vapi/libfeedback-0.0.*
%{_datadir}/gir-1.0/Lfb-0.0.gir
%{_libdir}/pkgconfig/libfeedback-0.0.pc
