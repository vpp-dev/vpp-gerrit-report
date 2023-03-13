
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Monday 2023-03-13, 02:19:07
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


Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VECr 6]: af_xdp: optimizing send performance

api: **Dave Barach** <vpp@barachs.net>
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VECr 6]: api: fix memory error with pending_rpc_requests in multi-thread environment

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VECr 12]: cnat: remove rwlock on ts
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VECr 12]: cnat: add ip/client bihash
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [VECr 12]: cnat: dont compute offloaded cksums
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VECr 12]: cnat: flag to disable rsession

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VECr 3]: crypto: making crypto-dispatch node working in adaptive mode

dma_intel: **Marvin Liu** <yong.liu@intel.com>
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VECr 6]: dma_intel: add native dsa device driver
  | `37819 <https:////gerrit.fd.io/r/c/vpp/+/37819>`_ [VECr 6]: vlib: pre-alloc dma batch structure

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `38415 <https:////gerrit.fd.io/r/c/vpp/+/38415>`_ [VECr 4]: dpdk: fix format rx/tx burst function name failed
  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VECr 6]: dpdk: use adapter MTU in max_frame_size setting

dpdk-cryptodev: **Sergio Gonzalez Monroy** <sergio.gonzalez.monroy@outlook.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VECr 3]: crypto: making crypto-dispatch node working in adaptive mode

feature: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VECr 30]: misc: fix feature dispatch possible crashed when feature config changed by user

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `38446 <https:////gerrit.fd.io/r/c/vpp/+/38446>`_ [VECr 4]: hs-test: create temporary folder at init

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38285 <https:////gerrit.fd.io/r/c/vpp/+/38285>`_ [VECr 16]: ip: fix update checksum in ip4_ttl_inc
  | `36018 <https:////gerrit.fd.io/r/c/vpp/+/36018>`_ [VECr 17]: ip: fix ip4_ttl_inc calc checksum error when checksum is 0
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VECr 17]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VECr 17]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VECr 30]: misc: fix feature dispatch possible crashed when feature config changed by user

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VECr 3]: crypto: making crypto-dispatch node working in adaptive mode
  | `38408 <https:////gerrit.fd.io/r/c/vpp/+/38408>`_ [VECr 4]: ipsec: fix logic in ext_hdr_is_pre_esp
  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [VECr 4]: ipsec: intorduce function esp_prepare_packet_for_enc
  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [VECr 4]: ipsec: esp_encrypt prefetch and unroll - introduce new types
  | `38410 <https:////gerrit.fd.io/r/c/vpp/+/38410>`_ [VECr 4]: ipsec: esp_encrypt prefetch and unroll
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VECr 6]: ipsec: esp_encrypt prefetch and unroll
  | `38252 <https:////gerrit.fd.io/r/c/vpp/+/38252>`_ [VECr 16]: ipsec: set fast path 5tuple ip addresses based on sa traffic selector values

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VECr 3]: linux-cp: auto select tap id when creating lcp pair

memif: **Damjan Marion** <damarion@cisco.com>
  | `38445 <https:////gerrit.fd.io/r/c/vpp/+/38445>`_ [VECr 4]: memif: don't leak error strings in API handlers

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VECr 3]: crypto: making crypto-dispatch node working in adaptive mode
  | `38445 <https:////gerrit.fd.io/r/c/vpp/+/38445>`_ [VECr 4]: memif: don't leak error strings in API handlers
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VECr 30]: misc: fix feature dispatch possible crashed when feature config changed by user

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VECr 2]: nat: fix address resolution
  | `38459 <https:////gerrit.fd.io/r/c/vpp/+/38459>`_ [VECr 2]: nat: fix nat44 vrf table and route handlers
  | `38440 <https:////gerrit.fd.io/r/c/vpp/+/38440>`_ [VECr 4]: nat: nat44-ed cli bug fix
  | `38442 <https:////gerrit.fd.io/r/c/vpp/+/38442>`_ [VECr 4]: nat: nat44-ed bug fix
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VECr 30]: misc: fix feature dispatch possible crashed when feature config changed by user

session: **Florin Coras** <fcoras@cisco.com>
  | `38462 <https:////gerrit.fd.io/r/c/vpp/+/38462>`_ [VECr 2]: session vcl: refactor builtin tx event for main tx
  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VECr 6]: vppinfra: improve & test abstract socket
  | `37819 <https:////gerrit.fd.io/r/c/vpp/+/37819>`_ [VECr 6]: vlib: pre-alloc dma batch structure

srv6-mobile: **Tetsuya Murakami** <tetsuya.mrk@gmail.com>, **Satoru Matsushima** <satoru.matsushima@gmail.com>
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECr 28]: srv6-mobile: Implement SRv6 mobile API funcs

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <sykazmi@cisco.com>
  | `38312 <https:////gerrit.fd.io/r/c/vpp/+/38312>`_ [VECr 18]: tap: add interface type check

teib: **Neale Ranns** <neale@graphiant.com>
  | `38305 <https:////gerrit.fd.io/r/c/vpp/+/38305>`_ [VECr 19]: teib: fix nh-table-id

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VECr 3]: crypto: making crypto-dispatch node working in adaptive mode
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VECr 17]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VECr 17]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECr 28]: srv6-mobile: Implement SRv6 mobile API funcs

vcl: **Florin Coras** <fcoras@cisco.com>
  | `38462 <https:////gerrit.fd.io/r/c/vpp/+/38462>`_ [VECr 2]: session vcl: refactor builtin tx event for main tx
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 3]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VECr 6]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `37819 <https:////gerrit.fd.io/r/c/vpp/+/37819>`_ [VECr 6]: vlib: pre-alloc dma batch structure
  | `38344 <https:////gerrit.fd.io/r/c/vpp/+/38344>`_ [VECr 16]: stats: fix collector

vpp: **Dave Barach** <vpp@barachs.net>
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VECr 6]: dma_intel: add native dsa device driver

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `38415 <https:////gerrit.fd.io/r/c/vpp/+/38415>`_ [VECr 4]: dpdk: fix format rx/tx burst function name failed
  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VECr 6]: vppinfra: improve & test abstract socket

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VECr 3]: crypto: making crypto-dispatch node working in adaptive mode

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `38011 <https:////gerrit.fd.io/r/c/vpp/+/38011>`_ [veC 44]: wireguard: move buffer when insufficient pre_data left
  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [Vec 90]: arp: fix arp request for ip4-glean node

**Andrew Ying** <hi@andrewying.com>:

  | `38064 <https:////gerrit.fd.io/r/c/vpp/+/38064>`_ [VeC 44]: dpdk: fix compatibility with DPDK < 21.11

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VeC 47]: fateshare: a plugin for managing child processes
  | `32164 <https:////gerrit.fd.io/r/c/vpp/+/32164>`_ [VeC 110]: acl: change the algorithm for cleaning the sessions from purgatory

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VEc 16]: ipsec: add per-SA error counters
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 83]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `34965 <https:////gerrit.fd.io/r/c/vpp/+/34965>`_ [VEc 3]: ipsec: make pre-shared keys harder to misuse
  | `38315 <https:////gerrit.fd.io/r/c/vpp/+/38315>`_ [vEC 19]: fib: fix load-balance and replicate dpos buckets overflow
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VeC 38]: ip_session_redirect: add session redirect plugin

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [VEc 6]: ebuild: adding libmemif to debian packages
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 46]: libmemif: added tests

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37836 <https:////gerrit.fd.io/r/c/vpp/+/37836>`_ [VEc 24]: dpdk-cryptodev: enq/deq scheme rework
  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [VEc 25]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37420 <https:////gerrit.fd.io/r/c/vpp/+/37420>`_ [Vec 115]: tests: remove intermittent failing tests on vpp_debug image

**Dmitry Valter** <dvalter@protonmail.com>:

  | `38082 <https:////gerrit.fd.io/r/c/vpp/+/38082>`_ [VeC 40]: lb: fix flow table update vector handing with ASAN
  | `38062 <https:////gerrit.fd.io/r/c/vpp/+/38062>`_ [VeC 44]: stats: fix node name compatison

**Duncan Eastoe** <duncaneastoe+github@gmail.com>:

  | `37750 <https:////gerrit.fd.io/r/c/vpp/+/37750>`_ [VeC 94]: stats: fix memory leak in stat_segment_dump_r()

**Filip Varga** <fivarga@cisco.com>:

  | `35444 <https:////gerrit.fd.io/r/c/vpp/+/35444>`_ [veC 137]: nat: nat44-ed cleanup & improvements
  | `35966 <https:////gerrit.fd.io/r/c/vpp/+/35966>`_ [veC 137]: nat: nat44-ed update timeout api
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VeC 137]: nat: nat66 cli bug fix
  | `34929 <https:////gerrit.fd.io/r/c/vpp/+/34929>`_ [veC 137]: nat: det44 map configuration improvements
  | `36724 <https:////gerrit.fd.io/r/c/vpp/+/36724>`_ [VeC 137]: nat: fixing incosistency in use of sw_if_index
  | `36480 <https:////gerrit.fd.io/r/c/vpp/+/36480>`_ [VeC 137]: nat: nat64 fix add_del calls requirements

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `37764 <https:////gerrit.fd.io/r/c/vpp/+/37764>`_ [VEc 16]: wireguard: under-load state determination update

**GaoChX** <chiso.gao@gmail.com>:

  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VeC 61]: interface: fix crash if vnet_hw_if_get_rx_queue return zero
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 62]: nat: nat44-ed get out2in workers failed for static mapping without port

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `37248 <https:////gerrit.fd.io/r/c/vpp/+/37248>`_ [VeC 166]: urpf: add show urpf cli

**Huawei LI** <lihuawei_zzu@163.com>:

  | `37727 <https:////gerrit.fd.io/r/c/vpp/+/37727>`_ [Vec 88]: nat: make nat44 session limit api reinit flow_hash with new buckets.
  | `37726 <https:////gerrit.fd.io/r/c/vpp/+/37726>`_ [Vec 99]: nat: fix crash when set nat44 session limit with nonexisted vrf.
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VeC 110]: policer: fix crash when delete interface policer classify.
  | `37651 <https:////gerrit.fd.io/r/c/vpp/+/37651>`_ [VeC 110]: classify: fix classify session cli.

**Jing Peng** <jing@meter.com>:

  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VeC 137]: nat: fix nat44-ed outside address selection
  | `36597 <https:////gerrit.fd.io/r/c/vpp/+/36597>`_ [VeC 137]: nat: fix nat44-ed API

**Kai Luo** <kailuo.nk@gmail.com>:

  | `37269 <https:////gerrit.fd.io/r/c/vpp/+/37269>`_ [VeC 155]: memif: fix uninitialized variable warning

**Klement Sekera** <klement.sekera@gmail.com>:

  | `38042 <https:////gerrit.fd.io/r/c/vpp/+/38042>`_ [VEc 5]: tests: enhance counter comparison error message
  | `38041 <https:////gerrit.fd.io/r/c/vpp/+/38041>`_ [VeC 45]: tests: refactor extra_vpp_punt_config

**Leyi Rong** <leyi.rong@intel.com>:

  | `37853 <https:////gerrit.fd.io/r/c/vpp/+/37853>`_ [VEc 2]: avf: performance optimization when CLIB_HAVE_VEC512 is enabled

**Matz von Finckenstein** <matz.vf@gmail.com>:

  | `38091 <https:////gerrit.fd.io/r/c/vpp/+/38091>`_ [VEc 27]: stats: Updated go version URL for the install script Added log flag to pass in logging file destination as an alternate logging destination from syslog

**Maxime Peim** <mpeim@cisco.com>:

  | `38139 <https:////gerrit.fd.io/r/c/vpp/+/38139>`_ [VeC 31]: vnet: throttling configuration improvement
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [Vec 46]: ipsec: huge anti-replay window support
  | `37941 <https:////gerrit.fd.io/r/c/vpp/+/37941>`_ [VeC 51]: classify: bypass drop filter on specific error

**Miguel Borges de Freitas** <miguel-r-freitas@alticelabs.com>:

  | `37532 <https:////gerrit.fd.io/r/c/vpp/+/37532>`_ [Vec 96]: cnat: fix cnat_translation_cli_add_del call for del with INVALID_INDEX

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 137]: nat: fix tcp session reopen in nat44-ed

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `33726 <https:////gerrit.fd.io/r/c/vpp/+/33726>`_ [VeC 151]: vlib: introduce an inter worker interrupts efds

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32820 <https:////gerrit.fd.io/r/c/vpp/+/32820>`_ [VeC 163]: cnat: better cnat snat-policy cli
  | `33264 <https:////gerrit.fd.io/r/c/vpp/+/33264>`_ [VeC 163]: pbl: Port based balancer

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VEc 5]: ip: IP address family common input node

**Ole Troan** <otroan@employees.org>:

  | `37766 <https:////gerrit.fd.io/r/c/vpp/+/37766>`_ [veC 88]: papi: vla list of fixed strings

**Sergey Matov** <sergey.matov@travelping.com>:

  | `31319 <https:////gerrit.fd.io/r/c/vpp/+/31319>`_ [VeC 137]: nat: DET: Allow unknown protocol translation

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [Vec 47]: virtio: allocate frame per interface

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37939 <https:////gerrit.fd.io/r/c/vpp/+/37939>`_ [VEc 8]: ip: support flow-hash gtpv1teid

**Ted Chen** <znscnchen@gmail.com>:

  | `37162 <https:////gerrit.fd.io/r/c/vpp/+/37162>`_ [VeC 137]: nat: fix the wrong unformat type
  | `36790 <https:////gerrit.fd.io/r/c/vpp/+/36790>`_ [VeC 164]: map: lpm 128 lookup error.
  | `37143 <https:////gerrit.fd.io/r/c/vpp/+/37143>`_ [VeC 176]: classify: remove unnecessary reallocation

**Tianyu Li** <tianyu.li@arm.com>:

  | `37530 <https:////gerrit.fd.io/r/c/vpp/+/37530>`_ [vec 135]: dpdk: fix interface name w/ the same PCI bus/slot/function

**Vladimir Bernolak** <vladimir.bernolak@pantheon.tech>:

  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VeC 137]: nat: det44 map configuration improvements + tests

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VEc 3]: mpls: fix possible crashes on tunnel create/delete
  | `37270 <https:////gerrit.fd.io/r/c/vpp/+/37270>`_ [VEc 5]: vppinfra: fix pool free bitmap allocation
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VeC 104]: nat: fix nat44_ed set_session_limit crash
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 137]: nat: add nat44-ed session filtering by fib table
  | `37264 <https:////gerrit.fd.io/r/c/vpp/+/37264>`_ [VeC 137]: nat: fix nat44-ed outside address distribution
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 171]: papi: fix socket api max message id calculation

**Vratko Polak** <vrpolak@cisco.com>:

  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 55]: api: fix vl_socket_write_ready
  | `37083 <https:////gerrit.fd.io/r/c/vpp/+/37083>`_ [Vec 179]: avf: tolerate socket events in avf_process_request

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38336 <https:////gerrit.fd.io/r/c/vpp/+/38336>`_ [VEc 16]: ip: IPv4 Fragmentation - fix fragment id alloc not multi-thread safe
  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [Vec 53]: api: fix api msg thread safe setting not work
  | `37681 <https:////gerrit.fd.io/r/c/vpp/+/37681>`_ [Vec 106]: udp: hand off packet to right session thread
  | `36704 <https:////gerrit.fd.io/r/c/vpp/+/36704>`_ [VeC 137]: nat: auto forward inbound packet for local server session app with snat
  | `37376 <https:////gerrit.fd.io/r/c/vpp/+/37376>`_ [VeC 154]: vlib: unix cli - fix input's buffer may be freed when using
  | `37375 <https:////gerrit.fd.io/r/c/vpp/+/37375>`_ [VeC 155]: ipsec: fix ipsec linked key not freed when sa deleted

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VEc 3]: interface dpdk avf: introducing setting RSS hash key feature
  | `37840 <https:////gerrit.fd.io/r/c/vpp/+/37840>`_ [VEc 5]: dpdk: bump to dpdk 22.11

**Yong Liu** <yong.liu@intel.com>:

  | `37572 <https:////gerrit.fd.io/r/c/vpp/+/37572>`_ [VEc 3]: vlib: support dma map extended memory
  | `37821 <https:////gerrit.fd.io/r/c/vpp/+/37821>`_ [VEc 6]: session: map new segment when dma enabled
  | `37574 <https:////gerrit.fd.io/r/c/vpp/+/37574>`_ [VEc 6]: dma_intel: add cbdma device support
  | `37823 <https:////gerrit.fd.io/r/c/vpp/+/37823>`_ [veC 89]: memif: support dma option

**Yulong Pei** <yulong.pei@intel.com>:

  | `38135 <https:////gerrit.fd.io/r/c/vpp/+/38135>`_ [VEc 6]: af_xdp: change default queue size as kernel xsk default

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vEC 4]: vrrp: dump vrrp vr peer Type: fix

**jinshaohui** <jinsh11@chinatelecom.cn>:

  | `38400 <https:////gerrit.fd.io/r/c/vpp/+/38400>`_ [vEC 5]: vlib:process node scheduling use timing_wheel have problem.
  | `30929 <https:////gerrit.fd.io/r/c/vpp/+/30929>`_ [Vec 117]: vppinfra: fix memory issue in mhash
  | `37297 <https:////gerrit.fd.io/r/c/vpp/+/37297>`_ [Vec 120]: ping: fix ping ipv6 address set packet size greater than  mtu,packet drop

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 105]: nat: add local addresses correctly in nat lb static mapping
  | `37566 <https:////gerrit.fd.io/r/c/vpp/+/37566>`_ [veC 125]: policer: add policer classify to output path

**steven luong** <sluong@cisco.com>:

  | `37105 <https:////gerrit.fd.io/r/c/vpp/+/37105>`_ [VeC 151]: vppinfra: add time error counters to stats segment

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
authors          85
maintainers      36
committers       0
abandoned        0
================ ===

