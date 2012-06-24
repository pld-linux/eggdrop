$Revision$, $Date$

Ten plik zawiera informacje dotyczace zmian, jakie wprowadzono w stosunku
do oryginalnego eggdropa.

Wszystkie ze wspomianych ni�ej plik�w dost�pne s� tak�e poprzez interfejs
CVSweb: http://cvs.pld.org.pl/

Nast�puj�ce �atki zosta�y na�o�one:
* eggdrop-FHS.patch dost�pne pod adresem:
  http://pld.mysza.eu.org/sources/eggdrop-FHS.patch
  �ata ta modyfikuje r�zne pliki sprawiaj�c, �e Eggdrop jest bardziej
  kompatybilny ze standardem Filesystem Hierarchy Standard
  
* eggdrop1.6.13+ipv6.patch.gz dost�pne pod adresem:
  http://www.egghelp.org/files/patches/eggdrop1.6.3+ipv6.patch.gz
  Ta �ata dodaje wsparcie dla protoko�u IPv6.

* eggdrop1.6.13+ipv6_config.patch dost�pne pod adresem
  http://pld.mysza.eu.org/sources/eggdrop1.6.13+ipv6_config.patch
  Ta �ata dodaje nowe zmienne (my-hostname6 i my-ip6) do pliku
  konfiguracyjnego.
  
* eggdrop-config_encryption.patch dostpne pod adresem
  http://pld.mysza.eu.org/sources/eggdrop-config_encryption.patch
  Ta prosta �ata dodaje informacje o trzech nowych modu�ach szyfruj�cych
  do pliku eggdrop.conf
  
* eggdrop-doc_makefile.patch dost�pne pod adresem
  http://pld.mysza.eu.org/sources/eggdrop-doc_makefile.patch
  Ta �ata modyfikuje plik doc/Makefile.in tak, aby dodatkowa dokumentacja
  zosta�a zainstalowana.
  
* eggdrop1.6.13-multilevel_sharing.patch.gz dostepne pod adresem
  ftp://ftp.eggheads.org/pub/eggdrop/patches/1.6/multilevel_sharing1.6.13.patch.gz
  (zmieniono nazw� pliku, ale nie zmodyfikowano go w �aden spos�b)
  Ta �ata dodaje nowe ustawienia, kt�re sprawiaj�, �e botnet staje si�
  bezpieczniejszy - od tej pory bot mo�e akceptowac zmiany w userli�cie
  tylko od huba (hub�w), i odrzuci� wszelkie zmiany wys�ane przez boty mu
  podleg�e (leaves).
  
* eggdrop1.6.13-unlinkedby.patch dost�pne pod adresem
  ftp://ftp.eggheads.org/pub/eggdrop/patches/1.6/unlinkedby1.6.13.patch
  (zmieniono nazw� pliku, ale nie zmodyfikowano go w �aden spos�b)
  Ta �ata rozszerza wiadomo�� rozsy�an� do botnetu podczas od��czania bota
  o pseudonim osoby, kt�ra u�y�a komendy .unlink.

* eggdrop1.6.13-topicprot.patch dost�pne pod adresem
  http://pld.mysza.eu.org/sources/eggdrop1.6.13-topicprot.patch
  Ta �ata, bazowana na �atce topicprot.patch dla eggdrop1.6.12 dodaje mo�liwo��
  zablokowania topicu na danym kanale.

  
Dodano t�umaczenia plik�w pomocy na nast�puj�ce j�zyki.
* du�ski (dannish)
* fi�ski (finnish)
* w�oski (italian)
* norweski (norwegian)
* portugalski (portuguese)
* brazyliska odmiana portugalskiego (portuguese_br)
* rumu�ski (romanian)
  T�umaczenia dla poszczeg�lnych j�zyk�w dost�pne s� pod adresem
  http://pld.mysza.eu.org/sources/eggdrop-language-{language}.tar.gz
  gdzie {language} jest angielsk� nazw� danego j�zyka (podana w nawiasach)
  Pliki te zosta�y znalezione pod adresem http://www.egghelp.org/ . Zosta�y
  one przepakowane.
  
Dodano nast�puj�ce dodatkowe modu�y:  
* away 1.0
* botnetop 1.0.1
* fakebotnet 1.3
* gseen 1.1.0
* irctree 1.1
* megahal 2.5
* stats 1.3.3dev1
  Ka�dy z tych modu��w dostepny jest pod adresem:
  http://pld.mysza.eu.org/sources/eggdrop-module-{module}-{version}.tar.gz
  Zosta�y one wzi�te z r�nych miejsc, wliczaj�c w to:
  * http://www.visions-of-fantasy.de/
  * http://johoho.eggheads.org/
  * ftp://ftp.eggheads.org/
  Pliki te mog� by� �atwo znaleziono u�ywaj�c google.

