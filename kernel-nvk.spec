Name:           kernel-nvk
Version:        6.15
Release:        1%{?dist}
Summary:        Custom Linux Kernel NVK branch

License:        GPL-2.0
URL:            https://gitlab.freedesktop.org/gfxstrand/linux
Source0:        git+https://gitlab.freedesktop.org/gfxstrand/linux.git#branch=nvk

BuildRequires:  gcc, make, ncurses-devel, bc
Requires:       elfutils-libelf

%description
A custom-built Linux kernel from the NVK branch.

%prep
%autosetup -S git

%build
make defconfig
make -j$(nproc)

%install
make modules_install INSTALL_MOD_PATH=%{buildroot}
make install INSTALL_PATH=%{buildroot}/boot
%files
%{_bootdir}/*


%changelog
* Thu Sep 01 2025 Your Name <your.email@example.com> - 1.0-1
- Initial build
