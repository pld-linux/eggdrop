#
# Conditional build:
Summary:	Eggdrop is an IRC bot, written in C
Summary(pl.UTF-8):	Eggdrop jest botem IRC napisanym w C
Summary(pt_BR.UTF-8):	Bot de IRC escrito em C
Summary(ru.UTF-8):	Eggdrop, это IRC-бот написанный на языке C.
Name:		eggdrop
Version:	1.8.3
Release:	2
License:	GPL v2
Group:		Applications/Communications
Source0:	ftp://ftp.eggheads.org/pub/eggdrop/source/1.8/%{name}-%{version}.tar.gz
# Source0-md5:	30b076b813a6b04f7421ab709309af7b
# In order to unify filenames, following language packs and third-party modules were
# repackaged. Some files were renamed, but none modified. Original archives can be
# found by looking at http://www.egghelp.org/
Source10:	%{name}-language-danish.tar.gz
# Source10-md5:	86b9bbab196f64b09e4daf2dec93fd50
Source11:	%{name}-language-finnish.tar.gz
# Source11-md5:	d720c6ad3f19deb8d51eeb753d0da390
Source12:	%{name}-language-italian.tar.gz
# Source12-md5:	9c568bc516ecb202ed9e76c1523e4d6a
Source13:	%{name}-language-norwegian.tar.gz
# Source13-md5:	118e14c8dfe0a6917e8e7b191a733e3f
Source14:	%{name}-language-portuguese.tar.gz
# Source14-md5:	1b96f1ba51a0162665be892327c405cf
Source15:	%{name}-language-portuguese_br.tar.gz
# Source15-md5:	93d4afae51dfa4cd7512fa6236868960
Source16:	%{name}-language-romanian.tar.gz
# Source16-md5:	3664b4f4870eb099d3a291284a076561
# Additional modules taken from various places
Source20:	%{name}-module-away-1.0.tar.gz
# Source20-md5:	89b0529d024d8c29a855fb26e9e24a58
Source21:	%{name}-module-botnetop-1.0.1.tar.gz
# Source21-md5:	1815a88748529d2ce6a221d560678285
Source22:	%{name}-module-fakebotnet-1.3.tar.gz
# Source22-md5:	bf6e0ecc97bbe154137dba5f47c6e518
Source23:	%{name}-module-gseen-1.1.0.tar.gz
# Source23-md5:	d1b5ff929c360581647a2baf7281a7a6
Source24:	%{name}-module-irctree-1.1.tar.gz
# Source24-md5:	8bf884c57adbb131228fe47bffc69836
Source25:	%{name}-module-megahal-2.6b.tar.gz
# Source25-md5:	1c8762d63d16c95bee3a2399614b8ac5

Source27:	%{name}-module-idea-1.0.2.tar.gz
# Source27-md5:	dce4a43dfcfb72e143c71e8f6c6fc8c8
Source28:	%{name}-module-twofish-1.0.tar.gz
# Source28-md5:	861957c170b4af105199202e724be2a3
#Source29:	%{name}-module-rijndael-1.0.tar.gz
# http://eggdrop.msk.ru/files/irc/eggdrop1.6.19-patch-sp0009+SSL.tar.bz2
Source30:	http://eggdrop.msk.ru/files/irc/%{name}1.6.19-patch-sp0009.tar.bz2
# Source30-md5:	37df8dbb76a2b2283e2e80c182dc9967
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-doc_makefile.patch

# http://www.egghelp.org/files.htm#patches

Patch4:		%{name}-config_encryption.patch
Patch5:		%{name}-autobotchk.patch
# http://www.egghelp.org/files.htm#patches

Patch7:		%{name}-nolibs.patch

Patch9:		%{name}-nmu.patch

Patch12:	%{name}-build.patch
URL:		http://www.eggheads.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.453
BuildRequires:	tcl-devel
Requires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eggdrop is an IRC bot, written in C. If you don't know what IRC is,
this is probably not whatever you're looking for! Eggdrop, being a
bot, sits on a channel and takes protective measures: to keep the
channel from being taken over (in the few ways that anything CAN), to
recognize banished users or sites and reject them, to recognize
privileged users and let them gain ops, etc. Eggdrop also contains
many modules and scripts, for example for sending files. Here is the
list of new features as opposed to vanilla eggdrop:
- Additional modules, including:
  - away
  - botnetop
  - fakebotnet
  - gseen
  - irctree
  - megahal
  - stats
  - three new encryption modules: idea, twofish, rijndael
- Additional language packs:
  - dannish
  - finnish
  - italian
  - norwegian
  - portuguese
  - brazillian portuguese
  - romanian
- Various small patches were applied
For more information, see README.PLD.en file located under
%{_docdir}/%{name}-%{version}

%description -l pl.UTF-8
Eggdrop jest IRCowym botem napisanym w C. Eggdrop, będąc botem jest na
kanale i zajmuje się jego ochroną: zabezpieczeniem przed przejęciem,
nadawaniem odpowiednich przywilejów zarejestrowanym użytkownikom,
pilnowanie tzw. banów itp. Eggdrop poza tymi funkcjami posiada także
wiele dodatków, jak przesyłanie plików czy inne skrypty dla rozrywki.
Oto lista nowych możliwości w odróżnieniu od 'czystego' eggdropa:
- Dodatkowe moduły, takie jak:
  - away
  - botnetop
  - fakebotnet
  - gseen
  - irctree
  - megahal
  - stats
  - trzy nowe moduły szyfrujące: idea, twofish, rijndael
- Dodatkowe
  - duński
  - fiński
  - włoski
  - norweski
  - portugalski
  - brazylijska odmiana portugalskiego
  - rumuński
- Zaaplikowano różne mniejsze lub większe łaty
Więcej informacji znajdziesz w pliku README.PLD.pl znajdującym się
w katalogu %{_docdir}/%{name}-%{version}

%description -l pt_BR.UTF-8
Eggdrop é um bot de IRC, escrito em linguagem C.

Eggdrop, sendo um bot, permanece em um canal e toma medidas de
proteç?o: evitando que o canal seja tomado (usando as poucas maneiras
possíveis), reconhecendo usuários ou sites expulsos e os rejeitando,
reconhecendo usuários privilegiados e permitindo que estes recebam OPS
etc.

%description -l ru.UTF-8
Eggdrop, это IRC-бот написанный на языке C. Если вы не знаете,
что такое IRC, то это вероятно не то, что вы ищете!
Eggdrop находится на канале в целях оказания защитных мер:
охраны канала от перехвата управления злоумышленниками,
распознования пользователей или сайтов, для которых канал
блокирован, с последующим отказом в доступе,
распознавания операторов канала, с присвоением им
соответствующих прав и привилегий.

%prep
%setup -q -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a20 -a21 -a22 -a23 -a24 -a25 -a27 -a28 -a30
mv aclocal.m4 acinclude.m4
%patch -P0 -p1
%patch -P1 -p1

%patch -P4 -p1
%patch -P5 -p1
%patch -P7 -p1

#%%patch9 -p0 - wtf is this?

%patch -P12 -p1

# detect threaded tcl version
sed -i -e 's#TclpFinalizeThreadData#Tcl_FinalizeThread#g' acinclude.m4

%build
cp -f /usr/share/automake/config.sub misc/
cp -f %{name}.conf doc/%{name}.conf.example
%{__aclocal}
%{__autoheader}
%{__autoconf}
cd src/mod/compress.mod
%{__autoconf}
%configure
cd ../dns.mod
%{__autoconf}
%configure
cd ../../..
%configure \
	--enable-tcl-threads \
	--enable-ipv6
%{__make} config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/modules,%{_mandir}/man1,%{_datadir}/%{name}}

%{__make} install \
	INSTALL="install -p" \
	DEST=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/%{name}-%{version} $RPM_BUILD_ROOT%{_bindir}/%{name}
mv $RPM_BUILD_ROOT{/{text/*,help,scripts,language},%{_datadir}/%{name}/}
mv $RPM_BUILD_ROOT/modules/* $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/
mv $RPM_BUILD_ROOT{/doc,%{_mandir}}/man1/%{name}.1
rm -rf $RPM_BUILD_ROOT/{doc,README,logs,eggdrop.conf}
%{__rm} $RPM_BUILD_ROOT/{eggdrop,modules}

rm -rf docs
cp -a doc docs
rm -rf docs/{man1,Makefile*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%attr(755,root,root) %{_libdir}/%{name}/modules/*.so
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
