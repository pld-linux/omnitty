Summary:	Omnitty Multiple-Machine SSH Multiplexer
Summary(pl.UTF-8):   Rozdzielacz SSH wielu maszyn
Name:		omnitty
Version:	0.3.0
Release:	1
License:	GPL v2
Group:		Applications/Terminal
Source0:	http://dl.sourceforge.net/omnitty/%{name}-%{version}.tar.gz
# Source0-md5:	5d35c4dfdc3194de94527e28a27d8461
URL:		http://omnitty.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	rote-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Omnitty is a curses-based program that allows one to log into and
interact with several machines simultaneously, selectively directing
input to individual machines or groups of selected machines. Very
useful as a multiple-host network administration tool.

%description -l pl.UTF-8
Omnitty jest opartym na curses programem pozwalającym raz zalogować
się i pracować z wieloma maszynami jednocześnie, wybierając
bezpośrednie wejście na poszczególne maszyny lub grupy maszyn. Bardzo
użyteczny jako narzędzie administracyjne w wielokomputerowych
sieciach.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/%{name}.*
