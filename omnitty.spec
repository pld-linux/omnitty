Summary:	Omnitty Multiple-Machine SSH Multiplexer
Summary(pl):	Rozdzielacz SSH wielu maszyn
Name:		omnitty
Version:	0.2.8
Release:	1
License:	GPL
Group:		Applications/Terminal
Source0:	http://dl.sourceforge.net/omnitty/%{name}-%{version}.tar.gz
# Source0-md5:	b83a3a756dfbfb1c6b1d2344ef0ab3fc
# Source0-size:	51200
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

%description -l pl
Omnitty jest opartym na curses programem pozwalającym raz zalogować
się i pracować z wieloma maszynami jednocześnie, wybierając
bezpośrednie wejście na poszczególne maszyny lub grupy maszyn. Bardzo
użyteczny jako narzędzie administracyjne w wielokomputerowych
sieciach.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
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
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/%{name}.*
