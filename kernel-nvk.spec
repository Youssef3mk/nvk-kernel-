Name:           kernel-nvk
Version:        1.0
Release:        1%{?dist}
Summary:        Custom Linux Kernel NVK branch

License:        GPL-2.0
URL:            https://gitlab.freedesktop.org/gfxstrand/linux
Source0:        git+https://gitlab.freedesktop.org/gfxstrand/linux.git#branch=nvk

BuildRequires:  gcc, make, ncurses-devel, bc, elfutils-libelf-devel
Requires:       elfutils-libelf

%description
A custom-built Linux kernel from the NVK branch.

%prep
%autosetup -S git

%build
make defconfig
make -j$(nproc)

%install
make INSTALL_MOD_PATH=%{buildroot} modules_install
install -d %{buildroot}%{_bootdir}
install -m 644 arch/x86/boot/bzImage %{buildroot}%{_bootdir}/vmlinuz-nvk

%files
%license COPYING
%doc README.md
%{_bootdir}/vmlinuz-nvk
%{_libdir}/modules/%{version}

%changelog
* Thu Sep  1 2023 Your Name <your.email@example.com> - 1.0-1
- Initial build of kernel from NVK branch
