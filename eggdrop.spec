Summary:	Eggdrop is an IRC bot, written in C
Summary(pl):	Eggdrop jest botem IRC napisanym w C
Name:		eggdrop
Version:	1.6.9
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.eggdropsrus.co.uk/downloads/eggdrop/%{name}%{version}.tar.gz
Patch0:		%{name}-FHS.patch
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
%setup -q -n %{name}%{version}
%patch0 -p1

%build
./configure
%{__make} config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/modules,%{_datadir}/%{name},%{_mandir}/man1,%{_datadir}/%{name}/{help,scripts,language},%{_datadir}/doc/%{name}-%{version}}

%{__make} DESTDIR="$RPM_BUILD_ROOT" install

cp $RPM_BUILD_ROOT/%{name}-%{version} $RPM_BUILD_ROOT%{_bindir}/%{name}

find $RPM_BUILD_ROOT/doc -type f | egrep -v "(\.html$|\.htm$)" | xargs gzip -9nf
gzip -9nf $RPM_BUILD_ROOT/README $RPM_BUILD_ROOT/%{name}.{simple,complete,advanced}.conf

cp $RPM_BUILD_ROOT/doc/man1/%{name}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1.gz
rm -r $RPM_BUILD_ROOT/doc/man1

cp -a $RPM_BUILD_ROOT/README.gz \
	$RPM_BUILD_ROOT/%{name}.{simple,complete,advanced}.conf.gz \
	$RPM_BUILD_ROOT/doc/* \
	$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/

cp -a $RPM_BUILD_ROOT/text/* \
	$RPM_BUILD_ROOT/help/ \
	$RPM_BUILD_ROOT/scripts/ \
	$RPM_BUILD_ROOT/language/ \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/

cp -a $RPM_BUILD_ROOT/modules/* \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/modules/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_datadir}/doc/%{name}-%{version}
%{_mandir}/man1/%{name}.1*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/modules/*.so
%{_datadir}/%{name}
