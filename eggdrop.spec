Summary:     Eggdrop is an IRC bot, written in C
Name:        eggdrop
Version:     1.3.19
Release:     2
Copyright:   GPL
Group:       Applications/Communications
Group(pl):   Aplikacje/Komunikacja
Source0:     ftp://ftp.eggdrop.net/pub/eggdrop/official/%{name}%{version}.tar.gz
Source1:     eggdrop.sh
Patch:       eggdrop.diff
URL:         http://www.eggdrop.net/
Requires:    tcl
BuildRoot:   /tmp/buildroot-%{name}-%{version}
Summary(pl): Eggdrop jest botem IRC napisanym w C

%description
Eggdrop is an IRC bot, written in C.  If you don't know what IRC is,
this is probably not whatever you're looking for!  Eggdrop, being a
bot, sits on a channel and takes protective measures: to keep the
channel from being taken over (in the few ways that anything CAN),
to recognize banished users or sites and reject them, to recognize
privileged users and let them gain ops, etc.

%description -l pl
Eggdrop jest IRCowym botem napisanym w C. Eggdrop, bêd±c 'bot'em
jest na kanale i zajmuje siê jego ochron±: zabezpieczeniem przed
takeover-em, nadawaniem odpowiednich przywilejów zarejestrowanym
u¿ytkownikom, pilnowanie tzw. banów. itp.

%prep
%setup -n %{name}%{version}
%patch -p1

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,lib/eggdrop,man/man1}

make install DEST=$RPM_BUILD_ROOT/usr/lib/eggdrop
install  $RPM_BUILD_ROOT/usr/lib/eggdrop/doc/man1/eggdrop.1 \
	$RPM_BUILD_ROOT/usr/man/man1
rm -rf doc/man1/
install $RPM_SOURCE_DIR/eggdrop.sh $RPM_BUILD_ROOT/usr/bin/eggdrop

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644, root, root, 755)
%doc README doc/BOTNET doc/KNOWN-PROBLEMS doc/MODULES doc/UPDATES*
%doc doc/eggdrop.doc doc/nets.list doc/tcl-commands.doc doc/tricks
%attr(755, root, root) /usr/bin/*
/usr/lib/eggdrop/eggdrop
/usr/lib/eggdrop/motd
/usr/lib/eggdrop/filesys
/usr/lib/eggdrop/help
/usr/lib/eggdrop/language
/usr/lib/eggdrop/modules
/usr/lib/eggdrop/scripts
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Sat Feb 6 1999 Marek Obuchowicz <elephant@shadow.eu.org
[1.3.19-2]
- added polish translations
- compressed man files
- modified spec layout

* Mon Sep 7 1998  Ian Macdonald <ianmacd@xs4all.nl>
- Upgraded to 1.3.19
