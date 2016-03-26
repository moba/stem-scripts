# stem scripts
a collection of small scripts for some Tor metrics that I needed, using the [stem](https://stem.torproject.org) library

## listrelaysbyspeed.py

```
❯ ./listrelaysbyspeed.py                                                                                                                                                                                     ✹
Fetching latest descriptors, can take a while...

7575 relays (1032 exits)
total bandwidth exit relays: 4939 MB/s
80% (3951 MB/s): 281 exit relays
Fastest: aurora (72 MB/s): 0x02225522 Frenn vun der Enn (FVDE) <info AT enn DOT lu>
Slowest: PiratenNDS2 (5 MB/s): technik@piraten-nds.de

Total contacts: 126

Fuzzy total: 126

MBit/s  | #Relays | Contact
4776    | 54      | <none>
2608    | 6       | 0x02225522 Frenn vun der Enn (FVDE) <info AT enn DOT lu>
1872    | 10      | Torservers.net <support .AT. torservers .DOT. net>
1360    | 7       | abuse[__aT   ]necto|doT--|onion
928     | 10      | Babylon Network | noc <AT> babylon <DOT> network | PGP 0x2A540FA5 | 1HiSG8pia5DdDLUMyYNkF9sicGozojZLnH
872     | 4       | tor-relay-admin robgjansen com
848     | 3       | https://www.torservers.net/donate.html <support .AT. torservers .DOT. net>
840     | 4       | 0x9F29C15D42A8B6F3 Nos oignons <adminsys@nos-oignons.net> - 17WLwtW63FrHeMAEVkALnwhfmizBxGXDW1
776     | 7       | http://www.privacyfoundation.ch/abuse/  BTC: 15s5e8u9NcAZUie6ivMXLa2AvatvmtxqXu
776     | 5       | DFRI <tor AT dfri dot se> - 1Muz37TfXVBiJKRJkAqTNo7MnEZN8hhmJQ
744     | 5       | Privacy Republic <abuse-team _at_ PrivacyRepublic _dot_ org>
728     | 5       | drift@multinet.no - 1Geq8GGC7qTh7dfptneAYtpeARPAL8B2kh
688     | 6       | TNinja <abuse-team _at_ tor _dot_ ninja>
664     | 11      | Accessnow.org <abuse .AT. accessnow .DOT. org>
608     | 10      | Nicholas Merrill <nick AT calyx dot com> BTC - 14wntQ8cBdnhUVfYmDjXz6PbpSSX8nCtkr
424     | 1       | YWJ1c2VAaXByZWRhdG9yLnNl
408     | 2       | tor-admin AT torland DOT is
392     | 2       | TvdW <tor AT tvdw DOT eu> - bitcoin 1NKKoCQwKs67eKBGedMD8wYoAs3Z4mMAex
344     | 2       | Abuse Department <abuse AT hartvoorinternetvrijheid dot nl>
320     | 2       | Umich Tor <tor-exit-admin@umich.edu>
304     | 5       | Random Person <tor0102.10.swsnyder AT spamgourmet dot com>
264     | 1       | http://as250.peeringdb.com/ - BTC 15y79y3vc1RjidRTUc8vPb7fejrvi1FAdg
256     | 2       | tor-relays@coldhak.ca
232     | 1       | 0x70E87597 Patrick ZAJDA <gansta93 AT free dot fr> - 1BCkTjnkrXodEsBUh8mbpKS9eGg8BwoJJa
216     | 1       | Walter Heukels <walter@badexample.net>
192     | 2       | kolus riseup net
184     | 1       | sysop[at]openinternet.io BTC: 1N1s2BmWqbRH4Af5jjrNkm8XChnsRmPgA5
176     | 1       | dhalgren.tor@gmail.com
168     | 2       | apx <kenan@sly.mn> - 1HdGP8Tu8oNoiHPtyFUJbq3emPknBug45m
168     | 2       | Administrator <contact@tor-node.net>
```
