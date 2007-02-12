Summary:	Tools for the second extended (ext2) filesystem
Summary(pl.UTF-8):   Narzędzia do systemu plikowego ext2
Name:		genext2fs
Version:	1.3
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://xavier.bestel.free.fr/%{name}-%{version}.tgz
# Source0-md5:	91c06c5c7ec27ce886e67b3b28d78d9b
Source1:	%{name}-Makefile
Patch0:		%{name}-blkdev.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
genext2fs generates an ext2 filesystem without the need to be root.
You can generate a filesystem image, symlinks and device nodes
included, as a normal user.

%description -l pl.UTF-8
genext2fs generuje system plików ext2 bez potrzeby posiadania
uprawnień superużytkownia. Możesz wygenerować obraz systemu plików, z
linkami symbolicznymi i plikami urządzeń jako normalny użytkownik.

%prep
%setup -q
%patch0 -p1

install %{SOURCE1} Makefile

%build
%{__make}
head -n 61 genext2fs.c >README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install genext2fs $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README dev.txt
%attr(755,root,root) %{_bindir}/*
