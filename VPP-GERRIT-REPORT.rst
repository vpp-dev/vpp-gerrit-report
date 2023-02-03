
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Friday 2023-02-03, 02:32:41
--------------------------------------------


Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - Comments resolved
    - Review incomplete (Code-Review < +1)
    - 23 days since last update


Committers:
-----------
| **These gerrit changes have been**

    - Verified
    - Not expired
    - Comments resolved
    - Approved by Maintainers

| **Please perform a final review & submit.**

  | `38005 <https:////gerrit.fd.io/r/c/vpp/+/38005>`_ [VECR 1]: vpp-swan: allow SAs to be used to the route-based IPsec
  | `38063 <https:////gerrit.fd.io/r/c/vpp/+/38063>`_ [VECR 5]: vppinfra: fix pool_get OOB crash with ASAN
  | `37788 <https:////gerrit.fd.io/r/c/vpp/+/37788>`_ [VECR 12]: nat: fix accidental o2i deletion/reuse

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `38059 <https:////gerrit.fd.io/r/c/vpp/+/38059>`_ [VECr 0]: af_xdp: fix netns configuration
  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VECr 2]: af_xdp: optimizing send performance

avf: **Damjan Marion** <damarion@cisco.com>
  | `38117 <https:////gerrit.fd.io/r/c/vpp/+/38117>`_ [VECr 0]: avf: fix checksum offload configuration
  | `37935 <https:////gerrit.fd.io/r/c/vpp/+/37935>`_ [VECr 2]: avf: fix incorrect flag for flow director
  | `37852 <https:////gerrit.fd.io/r/c/vpp/+/37852>`_ [VECr 15]: avf dpdk: fix incorrect handling of IPv6 src address in flow

build: **Damjan Marion** <damarion@cisco.com>
  | `38122 <https:////gerrit.fd.io/r/c/vpp/+/38122>`_ [VECr 0]: build: allow skipping external-deps
  | `37840 <https:////gerrit.fd.io/r/c/vpp/+/37840>`_ [VECr 0]: dpdk: bump to dpdk 22.11
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 9]: fateshare: a plugin for managing child processes

classify: **Dave Barach** <vpp@barachs.net>
  | `37941 <https:////gerrit.fd.io/r/c/vpp/+/37941>`_ [VECr 13]: classify: bypass drop filter on specific error

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `37871 <https:////gerrit.fd.io/r/c/vpp/+/37871>`_ [VECr 0]: crypto: make it easier to diagnose keys use-after-free
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 0]: ipsec: add per-SA error counters

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 0]: ip_session_redirect: add session redirect plugin
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 9]: fateshare: a plugin for managing child processes

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `37840 <https:////gerrit.fd.io/r/c/vpp/+/37840>`_ [VECr 0]: dpdk: bump to dpdk 22.11
  | `38064 <https:////gerrit.fd.io/r/c/vpp/+/38064>`_ [VECr 6]: dpdk: fix compatibility with DPDK < 21.11
  | `37852 <https:////gerrit.fd.io/r/c/vpp/+/37852>`_ [VECr 15]: avf dpdk: fix incorrect handling of IPv6 src address in flow

dpdk-cryptodev: **Sergio Gonzalez Monroy** <sergio.gonzalez.monroy@outlook.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37840 <https:////gerrit.fd.io/r/c/vpp/+/37840>`_ [VECr 0]: dpdk: bump to dpdk 22.11

fib: **Neale Ranns** <neale@graphiant.com>
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 0]: ip_session_redirect: add session redirect plugin
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VECr 1]: ip: IP address family common input node

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `38060 <https:////gerrit.fd.io/r/c/vpp/+/38060>`_ [VECr 0]: hs-test: add nginx perf tests

interface: **Dave Barach** <vpp@barachs.net>
  | `38045 <https:////gerrit.fd.io/r/c/vpp/+/38045>`_ [VECr 7]: interface: add the missing tag keyword in the cli helper
  | `37941 <https:////gerrit.fd.io/r/c/vpp/+/37941>`_ [VECr 13]: classify: bypass drop filter on specific error
  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VECr 24]: interface: fix crash if vnet_hw_if_get_rx_queue return zero

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VECr 1]: ip: IP address family common input node

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 0]: ipsec: add per-SA error counters
  | `37870 <https:////gerrit.fd.io/r/c/vpp/+/37870>`_ [VECr 0]: ipsec: fix async crypto linked keys memory leak

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `38082 <https:////gerrit.fd.io/r/c/vpp/+/38082>`_ [VECr 2]: lb: fix flow table update vector handing with ASAN
  | `38048 <https:////gerrit.fd.io/r/c/vpp/+/38048>`_ [VECr 6]: lb: keep AddressSanitizer happy

libmemif: **Damjan Marion** <damarion@cisco.com>
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VECr 8]: libmemif: added tests

memif: **Damjan Marion** <damarion@cisco.com>
  | `38078 <https:////gerrit.fd.io/r/c/vpp/+/38078>`_ [VECr 1]: vppinfra: refactor clib_socket_init, add linux netns support
  | `37912 <https:////gerrit.fd.io/r/c/vpp/+/37912>`_ [VECr 20]: memif: fix input vector rate of memif-input node

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 0]: ip_session_redirect: add session redirect plugin
  | `38091 <https:////gerrit.fd.io/r/c/vpp/+/38091>`_ [VECr 1]: stats: added log flag to pass in logging file destination
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 9]: fateshare: a plugin for managing child processes

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 24]: nat: nat44-ed get out2in workers failed for static mapping without port

packetforge: **Ting Xu** <ting.xu@intel.com>
  | `38094 <https:////gerrit.fd.io/r/c/vpp/+/38094>`_ [VECr 0]: packetforge: fix lack of edge for ipv6 after gtppsc

session: **Florin Coras** <fcoras@cisco.com>
  | `38080 <https:////gerrit.fd.io/r/c/vpp/+/38080>`_ [VECr 2]: session: consolidate port alloc logic

snort: **Damjan Marion** <damarion@cisco.com>
  | `38078 <https:////gerrit.fd.io/r/c/vpp/+/38078>`_ [VECr 1]: vppinfra: refactor clib_socket_init, add linux netns support

srv6-mobile: **Tetsuya Murakami** <tetsuya.mrk@gmail.com>, **Satoru Matsushima** <satoru.matsushima@gmail.com>
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECr 23]: srv6-mobile: Implement SRv6 mobile API funcs

tcp: **Florin Coras** <fcoras@cisco.com>
  | `38080 <https:////gerrit.fd.io/r/c/vpp/+/38080>`_ [VECr 2]: session: consolidate port alloc logic

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `38086 <https:////gerrit.fd.io/r/c/vpp/+/38086>`_ [VECr 0]: tests: use existing pip compiled req file for building the run.py venv
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 0]: ipsec: add per-SA error counters
  | `37672 <https:////gerrit.fd.io/r/c/vpp/+/37672>`_ [VECr 0]: ipsec: fix SA names consistency in tests
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 0]: ip_session_redirect: add session redirect plugin
  | `37829 <https:////gerrit.fd.io/r/c/vpp/+/37829>`_ [VECr 5]: tests: support tmp-dir on different filesystem
  | `38042 <https:////gerrit.fd.io/r/c/vpp/+/38042>`_ [VECr 7]: tests: enhance counter comparison error message
  | `38041 <https:////gerrit.fd.io/r/c/vpp/+/38041>`_ [VECr 7]: tests: refactor extra_vpp_punt_config
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECr 23]: srv6-mobile: Implement SRv6 mobile API funcs

udp: **Florin Coras** <fcoras@cisco.com>
  | `38080 <https:////gerrit.fd.io/r/c/vpp/+/38080>`_ [VECr 2]: session: consolidate port alloc logic

vcl: **Florin Coras** <fcoras@cisco.com>
  | `38125 <https:////gerrit.fd.io/r/c/vpp/+/38125>`_ [VECr 0]: vcl: better handlig of ldp apis that rely on gnu source
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 6]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38062 <https:////gerrit.fd.io/r/c/vpp/+/38062>`_ [VECr 6]: stats: fix node name compatison

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `38078 <https:////gerrit.fd.io/r/c/vpp/+/38078>`_ [VECr 1]: vppinfra: refactor clib_socket_init, add linux netns support

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38004 <https:////gerrit.fd.io/r/c/vpp/+/38004>`_ [VECr 6]: wireguard: move buffer when insufficient pre_data left

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `37066 <https:////gerrit.fd.io/r/c/vpp/+/37066>`_ [veC 150]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".
  | `37068 <https:////gerrit.fd.io/r/c/vpp/+/37068>`_ [veC 153]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `38011 <https:////gerrit.fd.io/r/c/vpp/+/38011>`_ [vEC 6]: wireguard: move buffer when insufficient pre_data left
  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [Vec 52]: arp: fix arp request for ip4-glean node

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `32164 <https:////gerrit.fd.io/r/c/vpp/+/32164>`_ [VeC 72]: acl: change the algorithm for cleaning the sessions from purgatory

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 45]: ip: add support for buffer offload metadata in ip midchain

**Atzm Watanabe** <atzmism@gmail.com>:

  | `36935 <https:////gerrit.fd.io/r/c/vpp/+/36935>`_ [VeC 149]: ikev2: accept rekey request for IKE SA

**Benoît Ganne** <bganne@cisco.com>:

  | `37313 <https:////gerrit.fd.io/r/c/vpp/+/37313>`_ [VeC 114]: build: add sanitizer option to configure script

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [VEc 8]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 49]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 152]: ipsec: esp_encrypt prefetch and unroll

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37420 <https:////gerrit.fd.io/r/c/vpp/+/37420>`_ [Vec 77]: tests: remove intermittent failing tests on vpp_debug image

**Duncan Eastoe** <duncaneastoe+github@gmail.com>:

  | `37750 <https:////gerrit.fd.io/r/c/vpp/+/37750>`_ [VeC 56]: stats: fix memory leak in stat_segment_dump_r()

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 111]: dpdk: use adapter MTU in max_frame_size setting

**Filip Varga** <fivarga@cisco.com>:

  | `35444 <https:////gerrit.fd.io/r/c/vpp/+/35444>`_ [veC 99]: nat: nat44-ed cleanup & improvements
  | `35966 <https:////gerrit.fd.io/r/c/vpp/+/35966>`_ [veC 99]: nat: nat44-ed update timeout api
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VeC 99]: nat: nat66 cli bug fix
  | `34929 <https:////gerrit.fd.io/r/c/vpp/+/34929>`_ [veC 99]: nat: det44 map configuration improvements
  | `36724 <https:////gerrit.fd.io/r/c/vpp/+/36724>`_ [VeC 99]: nat: fixing incosistency in use of sw_if_index
  | `36480 <https:////gerrit.fd.io/r/c/vpp/+/36480>`_ [VeC 99]: nat: nat64 fix add_del calls requirements

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `37764 <https:////gerrit.fd.io/r/c/vpp/+/37764>`_ [VEc 1]: wireguard: under-load state determination update

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `37248 <https:////gerrit.fd.io/r/c/vpp/+/37248>`_ [VeC 128]: urpf: add show urpf cli

**Huawei LI** <lihuawei_zzu@163.com>:

  | `37727 <https:////gerrit.fd.io/r/c/vpp/+/37727>`_ [Vec 50]: nat: make nat44 session limit api reinit flow_hash with new buckets.
  | `37726 <https:////gerrit.fd.io/r/c/vpp/+/37726>`_ [Vec 61]: nat: fix crash when set nat44 session limit with nonexisted vrf.
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VeC 72]: policer: fix crash when delete interface policer classify.
  | `37651 <https:////gerrit.fd.io/r/c/vpp/+/37651>`_ [VeC 72]: classify: fix classify session cli.

**Jing Peng** <jing@meter.com>:

  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VeC 99]: nat: fix nat44-ed outside address selection
  | `36597 <https:////gerrit.fd.io/r/c/vpp/+/36597>`_ [VeC 99]: nat: fix nat44-ed API
  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 155]: vppapigen: fix json build error

**Kai Luo** <kailuo.nk@gmail.com>:

  | `37269 <https:////gerrit.fd.io/r/c/vpp/+/37269>`_ [VeC 117]: memif: fix uninitialized variable warning

**Leyi Rong** <leyi.rong@intel.com>:

  | `37853 <https:////gerrit.fd.io/r/c/vpp/+/37853>`_ [VeC 42]: avf: performance optimization when CLIB_HAVE_VEC512 is enabled

**Luo Yaozu** <luoyaozu@foxmail.com>:

  | `37691 <https:////gerrit.fd.io/r/c/vpp/+/37691>`_ [VeC 35]: vlib: fix vlib_log for elog

**Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>:

  | `38040 <https:////gerrit.fd.io/r/c/vpp/+/38040>`_ [VEc 2]: hs-test: configure VPP from test context

**Maxime Peim** <mpeim@cisco.com>:

  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VEc 8]: ipsec: huge anti-replay window support

**Miguel Borges de Freitas** <miguel-r-freitas@alticelabs.com>:

  | `37532 <https:////gerrit.fd.io/r/c/vpp/+/37532>`_ [Vec 58]: cnat: fix cnat_translation_cli_add_del call for del with INVALID_INDEX

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 99]: nat: fix tcp session reopen in nat44-ed

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `33726 <https:////gerrit.fd.io/r/c/vpp/+/33726>`_ [VeC 113]: vlib: introduce an inter worker interrupts efds

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 119]: vppinfra: improve & test abstract socket
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [veC 125]: cnat: dont compute offloaded cksums
  | `32820 <https:////gerrit.fd.io/r/c/vpp/+/32820>`_ [VeC 125]: cnat: better cnat snat-policy cli
  | `33264 <https:////gerrit.fd.io/r/c/vpp/+/33264>`_ [VeC 125]: pbl: Port based balancer
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 125]: cnat: add ip/client bihash
  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 125]: cnat: remove rwlock on ts
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 125]: cnat: flag to disable rsession
  | `32271 <https:////gerrit.fd.io/r/c/vpp/+/32271>`_ [VeC 125]: memif: add support for ns abstract sockets

**Neale Ranns** <neale@graphiant.com>:

  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [vEC 0]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [vEC 0]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `36821 <https:////gerrit.fd.io/r/c/vpp/+/36821>`_ [VeC 175]: vlib: "sh errors" shows error severity counters

**Ole Troan** <otroan@employees.org>:

  | `37766 <https:////gerrit.fd.io/r/c/vpp/+/37766>`_ [veC 50]: papi: vla list of fixed strings

**Sergey Matov** <sergey.matov@travelping.com>:

  | `31319 <https:////gerrit.fd.io/r/c/vpp/+/31319>`_ [VeC 99]: nat: DET: Allow unknown protocol translation

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [VEc 9]: virtio: allocate frame per interface

**Takanori Hirano** <me@hrntknr.net>:

  | `36781 <https:////gerrit.fd.io/r/c/vpp/+/36781>`_ [VeC 163]: ip6-nd: add fixed flag

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37863 <https:////gerrit.fd.io/r/c/vpp/+/37863>`_ [VEc 0]: sr: support define src ipv6 per encap policy
  | `37939 <https:////gerrit.fd.io/r/c/vpp/+/37939>`_ [VEc 0]: ip: support flow-hash gtpv1teid

**Ted Chen** <znscnchen@gmail.com>:

  | `37162 <https:////gerrit.fd.io/r/c/vpp/+/37162>`_ [VeC 99]: nat: fix the wrong unformat type
  | `36790 <https:////gerrit.fd.io/r/c/vpp/+/36790>`_ [VeC 126]: map: lpm 128 lookup error.
  | `37143 <https:////gerrit.fd.io/r/c/vpp/+/37143>`_ [VeC 138]: classify: remove unnecessary reallocation

**Tianyu Li** <tianyu.li@arm.com>:

  | `37530 <https:////gerrit.fd.io/r/c/vpp/+/37530>`_ [vec 97]: dpdk: fix interface name w/ the same PCI bus/slot/function

**Vladimir Bernolak** <vladimir.bernolak@pantheon.tech>:

  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VeC 99]: nat: det44 map configuration improvements + tests

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `38038 <https:////gerrit.fd.io/r/c/vpp/+/38038>`_ [VEc 0]: abf: fix next DPO on ABF

**Vladislav Grishenko** <themiron@mail.ru>:

  | `35796 <https:////gerrit.fd.io/r/c/vpp/+/35796>`_ [VeC 59]: vlib: avoid non-mp-safe cli process node updates
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VeC 66]: nat: fix nat44_ed set_session_limit crash
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 99]: nat: add nat44-ed session filtering by fib table
  | `37264 <https:////gerrit.fd.io/r/c/vpp/+/37264>`_ [VeC 99]: nat: fix nat44-ed outside address distribution
  | `37270 <https:////gerrit.fd.io/r/c/vpp/+/37270>`_ [VeC 127]: vppinfra: fix pool free bitmap allocation
  | `35721 <https:////gerrit.fd.io/r/c/vpp/+/35721>`_ [VeC 133]: vlib: stop worker threads on main loop exit
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 133]: papi: fix socket api max message id calculation

**Vratko Polak** <vrpolak@cisco.com>:

  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [VEc 17]: api: fix vl_socket_write_ready
  | `37083 <https:////gerrit.fd.io/r/c/vpp/+/37083>`_ [Vec 141]: avf: tolerate socket events in avf_process_request

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [VEc 15]: api: fix api msg thread safe setting not work
  | `37793 <https:////gerrit.fd.io/r/c/vpp/+/37793>`_ [VeC 52]: dpdk: plugin init should be protect by thread barrier
  | `37789 <https:////gerrit.fd.io/r/c/vpp/+/37789>`_ [VeC 54]: vlib: fix ASAN fake stack size set error when switching to process
  | `37777 <https:////gerrit.fd.io/r/c/vpp/+/37777>`_ [VeC 56]: stats: fix node name compare error when updating stats segment
  | `37776 <https:////gerrit.fd.io/r/c/vpp/+/37776>`_ [VeC 56]: vlib: fix macro define command not work in startup config exec script
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VeC 65]: crypto: fix async frame memory crash if frame pool expanded when using
  | `37681 <https:////gerrit.fd.io/r/c/vpp/+/37681>`_ [Vec 68]: udp: hand off packet to right session thread
  | `36704 <https:////gerrit.fd.io/r/c/vpp/+/36704>`_ [VeC 99]: nat: auto forward inbound packet for local server session app with snat
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 104]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `37427 <https:////gerrit.fd.io/r/c/vpp/+/37427>`_ [veC 109]: crypto: fix crypto dequeue handlers should be setted by VNET_CRYPTO_ASYNC_OP_XX
  | `37376 <https:////gerrit.fd.io/r/c/vpp/+/37376>`_ [VeC 116]: vlib: unix cli - fix input's buffer may be freed when using
  | `37375 <https:////gerrit.fd.io/r/c/vpp/+/37375>`_ [VeC 117]: ipsec: fix ipsec linked key not freed when sa deleted
  | `36808 <https:////gerrit.fd.io/r/c/vpp/+/36808>`_ [Vec 157]: arp: add support for Microsoft NLB unicast
  | `36880 <https:////gerrit.fd.io/r/c/vpp/+/36880>`_ [VeC 174]: ip: only set rx_sw_if_index when connection found to avoid following crash like tcp punt
  | `36812 <https:////gerrit.fd.io/r/c/vpp/+/36812>`_ [VeC 175]: cjson: json realloced output truncated if actual lenght more then 256

**Xie Long** <barryxie@tencent.com>:

  | `30268 <https:////gerrit.fd.io/r/c/vpp/+/30268>`_ [veC 154]: ip: fixup crash when reassemble a lots of fragments.

**Yong Liu** <yong.liu@intel.com>:

  | `37821 <https:////gerrit.fd.io/r/c/vpp/+/37821>`_ [Vec 51]: session: map new segment when dma enabled
  | `37819 <https:////gerrit.fd.io/r/c/vpp/+/37819>`_ [VeC 51]: vlib: pre-alloc dma batch structure
  | `37823 <https:////gerrit.fd.io/r/c/vpp/+/37823>`_ [veC 51]: memif: support dma option
  | `37572 <https:////gerrit.fd.io/r/c/vpp/+/37572>`_ [VeC 51]: vlib: support dma map extended memory
  | `37574 <https:////gerrit.fd.io/r/c/vpp/+/37574>`_ [VeC 51]: dma_intel: add cbdma device support
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VeC 51]: dma_intel: add native dsa device driver

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `36901 <https:////gerrit.fd.io/r/c/vpp/+/36901>`_ [VeC 140]: interface: fix 4 or more interfaces equality comparison bug with xor operation using (a^a)^(b^b)

**jinshaohui** <jinsh11@chinatelecom.cn>:

  | `30929 <https:////gerrit.fd.io/r/c/vpp/+/30929>`_ [Vec 79]: vppinfra: fix memory issue in mhash
  | `37297 <https:////gerrit.fd.io/r/c/vpp/+/37297>`_ [Vec 82]: ping: fix ping ipv6 address set packet size greater than  mtu,packet drop

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 67]: nat: add local addresses correctly in nat lb static mapping
  | `37566 <https:////gerrit.fd.io/r/c/vpp/+/37566>`_ [veC 87]: policer: add policer classify to output path
  | `34812 <https:////gerrit.fd.io/r/c/vpp/+/34812>`_ [Vec 99]: interface: more cleaning after set flags is failed in vnet_create_sw_interface

**steven luong** <sluong@cisco.com>:

  | `37105 <https:////gerrit.fd.io/r/c/vpp/+/37105>`_ [VeC 113]: vppinfra: add time error counters to stats segment
  | `30866 <https:////gerrit.fd.io/r/c/vpp/+/30866>`_ [Vec 178]: bonding: Add failover-mac active support

Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - Comments resolved
    - Review incomplete (Code-Review < +1)
    - 23 days since last update


Statistics:
-----------
================ ===
Patches assigned
================ ===
authors          99
maintainers      37
committers       3
abandoned        0
================ ===

