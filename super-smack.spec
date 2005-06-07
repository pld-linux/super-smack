Summary:	super-smack - MySQL benchmarking and stress-testing tool
Summary(pl):	super-smack - narzêdzie do sprawdzania wydajno¶ci i testowania MySQL-a
Name:		super-smack
Version:	1.2
Release:	0.1
# I guess it's GPL
License:	GPL
Group:		Applications/Databases
Source0:	http://jeremy.zawodny.com/mysql/super-smack/%{name}-%{version}.tar.gz
# Source0-md5:	8d045e09876e3669caacc0fc026bd3e4
Patch0:		%{name}-lib.patch
URL:		http://jeremy.zawodny.com/mysql/super-smack/
BuildRequires:	mysql-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib

%description
MySQL Super Smack is a benchmarking, stress testing, and load
generation tool for MySQL. Like the apache bench (ab) tool that ships
with Apache, super smack helps to give you a handle on how well your
server will perform. It's an invaluable testing and tuning aid.

%description -l pl
MySQL Super Smack to narzêdzie do sprawdzania wydajno¶ci, testowania
pod obci±¿eniem oraz generowania obci±¿enia dla MySQL-a. Podobnie jak
narzêdzie apache bench (ab) dostarczane z Apachem, super smack pomaga
w ocenie, jak dobrze sprawuje siê serwer. Jest to nieoceniona pomoc
przy testowaniu i tuningu.

%prep
%setup -q
#%patch0 -p1

%build
# FCK. can't get it via autoconf
sed -i -e 's,libmysqlclient.a,libmysqlclient.so,' configure
%configure2_13 \
	--with-mysql

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	DATADIR=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	SMACKS_DIR=$RPM_BUILD_ROOT%{_localstatedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README MANUAL INSTALL CHANGES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_localstatedir}/%{name}
