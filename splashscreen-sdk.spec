Name:       splashscreen-sdk
Summary:    Splashscreen for Mer SDK
Version:    0.1
Release:    1
Group:      System/Daemon
License:    Public Domain
Source0:    splash.png
Provides:   boot-splash-screen

%description
Splashscreen for Mer SDK

%prep
#%setup -q -n %{name}-%{version}

%build

%install
install -D -m 644 %{_sourcedir}/splash.png %{buildroot}/usr/share/plymouth/splash.png

%files
#%defattr(-,root,root,-)
/usr/share/plymouth/splash.png
