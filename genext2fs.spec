Summary:	Tools for the second extended (ext2) filesystem
Summary(pl):	Narzêdzia do systemu plikowego ext2
Name:		genext2fs
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://xavier.bestel.free.fr/%{name}-%{version}.tgz
Source1:	%{name}-Makefile
#URL:		
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
genext2fs generates an ext2 filesystem without the need to be root.
You can generate a filesystem image, symlinks and device nodes
included, as a normal user.

%prep
%setup  -q -n %{name}-%{version}

install %{SOURCE1} Makefile

%build
%{__make}
head -61 genext2fs.c >README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install genext2fs $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README dev.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
