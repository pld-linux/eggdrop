Summary:     Eggdrop is an IRC bot, written in C
Name:        eggdrop
%define versionmajor 2.0.0
%define versionminor -ALPHA
Version:     %{versionmajor}%{versionminor}
Release:     1
Copyright:   GPL
Group:       Applications/Communications
Group(pl):   Aplikacje/Komunikacja
Source0:     %{name}%{version}.tar.gz
Source1:     eggdrop.sh
Patch:       eggdrop-pld.patch
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
Eggdrop also contains many modules and scripts, for example for
sending files.

%description -l pl
Eggdrop jest IRCowym botem napisanym w C. Eggdrop, bêd±c botem
jest na kanale i zajmuje siê jego ochron±: zabezpieczeniem przed
takeover-em, nadawaniem odpowiednich przywilejów zarejestrowanym
u¿ytkownikom, pilnowanie tzw. banów. itp.
Eggdrop poza tymi funkcjami posiada tak¿e wiele dodatków, jak
przesy³anie plików czy inne skrypty dla rozrywki.

%prep
%setup -q -n %{name}%{version}
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/bin
# Dziwny problem z -ldir w module filesys
cd src/mod/filesys.mod
rm -f config.cache config.log
CFLAGS="$RPM_OPT_FLAGS" ./configure
cd ../../..
CFLAGS="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,lib/eggdrop,man/man1}
make install DEST=$RPM_BUILD_ROOT/usr/lib/eggdrop
rm -rf `find $RPM_BUILD_ROOT/usr/lib/eggdrop -name CVS`
rm -rf $RPM_SOURCE_DIR/doc/CVS
mv $RPM_BUILD_ROOT/usr/lib/eggdrop/doc/man1/* $RPM_BUILD_ROOT/usr/man/man1
rm -rf $RPM_BUILD_ROOT/usr/lib/eggdrop/doc/*
install $RPM_SOURCE_DIR/eggdrop.sh $RPM_BUILD_ROOT/usr/bin/eggdrop

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644, root, root, 755)
%doc CONTENTS COPYING FEATURES INSTALL README doc/*
%attr(755, root, root) /usr/bin/*
/usr/lib/eggdrop/filesys
/usr/lib/eggdrop/help
/usr/lib/eggdrop/language
%ghost /usr/lib/eggdrop/modules
/usr/lib/eggdrop/modules-%{versionmajor}
/usr/lib/eggdrop/scripts
%attr(755, root, root) /usr/lib/eggdrop/eggdrop2-%{versionmajor}
%ghost /usr/lib/eggdrop/eggdrop2
/usr/lib/eggdrop/eggdrop2.conf.*
/usr/lib/eggdrop/motd
%attr(644, root, man) /usr/man/man*/*

%changelog
* Sat Feb 20 1999 Marek Obuchowicz <elephant@shadow.eu.org>
[2.0.0-ALPHA-1]
 - minor spec modifications
 - added polish translations
 - compressed man files
 - added RPM_OPT_FLAGS support 

* Mon Sep 7 1998  Ian Macdonald <ianmacd@xs4all.nl>
 - Upgraded to 1.3.19
 
