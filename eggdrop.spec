Summary:	Eggdrop is an IRC bot, written in C
Summary(pl):	Eggdrop jest botem IRC napisanym w C
Name:		eggdrop
Version:	2.0.0
Release:	1.ALPHA
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	%{name}%{version}-ALPHA.tar.gz
Source1:	eggdrop.sh
Patch0:		eggdrop-pld.patch
URL:		http://www.eggdrop.net/
Requires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eggdrop is an IRC bot, written in C. If you don't know what IRC is,
this is probably not whatever you're looking for! Eggdrop, being a
bot, sits on a channel and takes protective measures: to keep the
channel from being taken over (in the few ways that anything CAN), to
recognize banished users or sites and reject them, to recognize
privileged users and let them gain ops, etc. Eggdrop also contains
many modules and scripts, for example for sending files.

%description -l pl
Eggdrop jest IRCowym botem napisanym w C. Eggdrop, bêd±c botem jest na
kanale i zajmuje siê jego ochron±: zabezpieczeniem przed przejêciem,
nadawaniem odpowiednich przywilejów zarejestrowanym u¿ytkownikom,
pilnowanie tzw. banów itp. Eggdrop poza tymi funkcjami posiada tak¿e
wiele dodatków, jak przesy³anie plików czy inne skrypty dla rozrywki.

%prep
%setup -q -n %{name}%{version}-ALPHA
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=%{_bindir}

# Dziwny problem z -ldir w module filesys
cd src/mod/filesys.mod
rm -f config.cache config.log

CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform}

cd ../../..
CFLAGS="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/eggdrop,%{_mandir}/man1}

make install DEST=$RPM_BUILD_ROOT%{_libdir}/eggdrop

rm -rf `find $RPM_BUILD_ROOT%{_libdir}/eggdrop -name CVS`
rm -rf `find $RPM_BUILD_DIR/%{name}%{version}-ALPHA/doc -name CVS`
mv -f $RPM_BUILD_ROOT%{_libdir}/eggdrop/doc/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
rm -rf $RPM_BUILD_ROOT%{_libdir}/eggdrop/doc/*
install $RPM_SOURCE_DIR/eggdrop.sh $RPM_BUILD_ROOT%{_bindir}/eggdrop

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	FEATURES README doc/{patch.howto,tricks,[A-Z]*,*.doc}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc FEATURES.gz README.gz doc/*.gz doc/html
%attr(755,root,root) %{_bindir}/*
%{_libdir}/eggdrop/filesys
%{_libdir}/eggdrop/help
%{_libdir}/eggdrop/language
%ghost %{_libdir}/eggdrop/modules
%{_libdir}/eggdrop/modules-%{version}
%{_libdir}/eggdrop/scripts
%attr(755,root,root) %{_libdir}/eggdrop/eggdrop2-%{version}
%ghost %{_libdir}/eggdrop/eggdrop2
%{_libdir}/eggdrop/eggdrop2.conf.*
%{_libdir}/eggdrop/motd
%{_mandir}/man*/*
