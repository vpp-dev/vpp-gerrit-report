
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Saturday 2023-03-25, 02:10:57
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
  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VECr 18]: af_xdp: optimizing send performance

api: **Dave Barach** <vpp@barachs.net>
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VECr 4]: api: fix mp-safe mark for some messages and add more
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VECr 18]: api: fix memory error with pending_rpc_requests in multi-thread environment

build: **Damjan Marion** <damarion@cisco.com>
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 8]: fateshare: a plugin for managing child processes

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VECr 24]: cnat: remove rwlock on ts
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VECr 24]: cnat: add ip/client bihash
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [VECr 24]: cnat: dont compute offloaded cksums
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VECr 24]: cnat: flag to disable rsession

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VECr 15]: crypto: making crypto-dispatch node working in adaptive mode

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 8]: fateshare: a plugin for managing child processes
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 9]: ip_session_redirect: add session redirect plugin

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `38415 <https:////gerrit.fd.io/r/c/vpp/+/38415>`_ [VECr 16]: dpdk: fix format rx/tx burst function name failed
  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VECr 18]: dpdk: use adapter MTU in max_frame_size setting

dpdk-cryptodev: **Sergio Gonzalez Monroy** <sergio.gonzalez.monroy@outlook.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VECr 15]: crypto: making crypto-dispatch node working in adaptive mode

fib: **Neale Ranns** <neale@graphiant.com>
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VECr 6]: fib: fix interface resolve from unlinked fib entries
  | `38515 <https:////gerrit.fd.io/r/c/vpp/+/38515>`_ [VECr 6]: fib: fix freed mpls label disposition dpo access
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 9]: ip_session_redirect: add session redirect plugin
  | `38315 <https:////gerrit.fd.io/r/c/vpp/+/38315>`_ [VECr 9]: fib: fix load-balance and replicate dpos buckets overflow

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `38542 <https:////gerrit.fd.io/r/c/vpp/+/38542>`_ [VECr 1]: hs-test: containerize ab and wrk

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `34635 <https:////gerrit.fd.io/r/c/vpp/+/34635>`_ [VECr 3]: ip: punt socket - take the tags in Ethernet header into consideration
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VECr 4]: api: fix mp-safe mark for some messages and add more
  | `38285 <https:////gerrit.fd.io/r/c/vpp/+/38285>`_ [VECr 28]: ip: fix update checksum in ip4_ttl_inc
  | `36018 <https:////gerrit.fd.io/r/c/vpp/+/36018>`_ [VECr 29]: ip: fix ip4_ttl_inc calc checksum error when checksum is 0
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VECr 29]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VECr 29]: ip: IPv6 validate input packet's header length does not exist buffer size

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38535 <https:////gerrit.fd.io/r/c/vpp/+/38535>`_ [VECr 2]: ipsec: fix non-esp packet may be matched as esp packet if flow cache enabled
  | `38528 <https:////gerrit.fd.io/r/c/vpp/+/38528>`_ [VECr 4]: ipsec: manually binding an SA to a worker
  | `38500 <https:////gerrit.fd.io/r/c/vpp/+/38500>`_ [VECr 7]: ipsec: missing linear search when flow cache search failed
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VECr 15]: crypto: making crypto-dispatch node working in adaptive mode
  | `38408 <https:////gerrit.fd.io/r/c/vpp/+/38408>`_ [VECr 16]: ipsec: fix logic in ext_hdr_is_pre_esp
  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [VECr 16]: ipsec: intorduce function esp_prepare_packet_for_enc
  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [VECr 16]: ipsec: esp_encrypt prefetch and unroll - introduce new types
  | `38410 <https:////gerrit.fd.io/r/c/vpp/+/38410>`_ [VECr 16]: ipsec: esp_encrypt prefetch and unroll
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VECr 18]: ipsec: esp_encrypt prefetch and unroll

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VECr 4]: api: fix mp-safe mark for some messages and add more

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VECr 11]: linux-cp: auto select tap id when creating lcp pair

memif: **Damjan Marion** <damarion@cisco.com>
  | `38477 <https:////gerrit.fd.io/r/c/vpp/+/38477>`_ [VECr 10]: memif: support dma option

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `38545 <https:////gerrit.fd.io/r/c/vpp/+/38545>`_ [VECr 1]: stats: check if stats vector entry is empty
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 8]: fateshare: a plugin for managing child processes
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 9]: ip_session_redirect: add session redirect plugin
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VECr 15]: crypto: making crypto-dispatch node working in adaptive mode

mpls: **Neale Ranns** <neale@graphiant.com>
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 6]: mpls: fix possible crashes on tunnel create/delete

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 0]: nat: nat44-ed get out2in workers failed for static mapping without port
  | `38551 <https:////gerrit.fd.io/r/c/vpp/+/38551>`_ [VECr 0]: nat: adding a new api nat44_ed_vrf_tables_v2_dump
  | `38521 <https:////gerrit.fd.io/r/c/vpp/+/38521>`_ [VECr 6]: nat: improve nat44-ed outside address distribution
  | `38517 <https:////gerrit.fd.io/r/c/vpp/+/38517>`_ [VECr 6]: nat: distribute nat44-ed in2out sessions by rx vrf
  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VECr 8]: nat: fix address resolution
  | `38440 <https:////gerrit.fd.io/r/c/vpp/+/38440>`_ [VECr 16]: nat: nat44-ed cli bug fix
  | `38442 <https:////gerrit.fd.io/r/c/vpp/+/38442>`_ [VECr 16]: nat: nat44-ed bug fix

packetforge: **Ting Xu** <ting.xu@intel.com>
  | `38499 <https:////gerrit.fd.io/r/c/vpp/+/38499>`_ [VECr 2]: packetforge: add option to show spec and mask only

perfmon: **Damjan Marion** <damarion@cisco.com>, **Ray Kinsella** <mdr@ashroe.eu>
  | `38506 <https:////gerrit.fd.io/r/c/vpp/+/38506>`_ [VECr 3]: perfmon: fix perfmon start type argument

session: **Florin Coras** <fcoras@cisco.com>
  | `38526 <https:////gerrit.fd.io/r/c/vpp/+/38526>`_ [VECr 3]: session: cleanup ho lookup table on close
  | `38529 <https:////gerrit.fd.io/r/c/vpp/+/38529>`_ [VECr 4]: session: lock ct pending connects
  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VECr 18]: vppinfra: improve & test abstract socket

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <sykazmi@cisco.com>
  | `38312 <https:////gerrit.fd.io/r/c/vpp/+/38312>`_ [VECr 30]: tap: add interface type check

tcp: **Florin Coras** <fcoras@cisco.com>
  | `38526 <https:////gerrit.fd.io/r/c/vpp/+/38526>`_ [VECr 3]: session: cleanup ho lookup table on close

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `34635 <https:////gerrit.fd.io/r/c/vpp/+/34635>`_ [VECr 3]: ip: punt socket - take the tags in Ethernet header into consideration
  | `38528 <https:////gerrit.fd.io/r/c/vpp/+/38528>`_ [VECr 4]: ipsec: manually binding an SA to a worker
  | `38521 <https:////gerrit.fd.io/r/c/vpp/+/38521>`_ [VECr 6]: nat: improve nat44-ed outside address distribution
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 6]: mpls: fix possible crashes on tunnel create/delete
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 9]: ip_session_redirect: add session redirect plugin
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VECr 15]: crypto: making crypto-dispatch node working in adaptive mode
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VECr 29]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VECr 29]: ip: IPv6 validate input packet's header length does not exist buffer size

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `38315 <https:////gerrit.fd.io/r/c/vpp/+/38315>`_ [VECr 9]: fib: fix load-balance and replicate dpos buckets overflow

vapi: **Ole Troan** <ot@cisco.com>
  | `38491 <https:////gerrit.fd.io/r/c/vpp/+/38491>`_ [VECr 8]: vppapigen: c++ vapi stream message codegen

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 0]: misc: patch to test CI infra changes

vhost: **Steven Luong** <sluong@cisco.com>
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VECr 4]: api: fix mp-safe mark for some messages and add more

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VECr 18]: api: fix memory error with pending_rpc_requests in multi-thread environment

vpp: **Dave Barach** <vpp@barachs.net>
  | `38545 <https:////gerrit.fd.io/r/c/vpp/+/38545>`_ [VECr 1]: stats: check if stats vector entry is empty
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VECr 4]: api: fix mp-safe mark for some messages and add more

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `38544 <https:////gerrit.fd.io/r/c/vpp/+/38544>`_ [VECr 1]: vppinfra: small improvement and polishing of AES GCM code
  | `38415 <https:////gerrit.fd.io/r/c/vpp/+/38415>`_ [VECr 16]: dpdk: fix format rx/tx burst function name failed
  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VECr 18]: vppinfra: improve & test abstract socket

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VECr 15]: crypto: making crypto-dispatch node working in adaptive mode

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `38011 <https:////gerrit.fd.io/r/c/vpp/+/38011>`_ [veC 56]: wireguard: move buffer when insufficient pre_data left
  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [Vec 102]: arp: fix arp request for ip4-glean node

**Andrew Ying** <hi@andrewying.com>:

  | `38064 <https:////gerrit.fd.io/r/c/vpp/+/38064>`_ [VeC 56]: dpdk: fix compatibility with DPDK < 21.11

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `38540 <https:////gerrit.fd.io/r/c/vpp/+/38540>`_ [vEC 1]: For triaging.
  | `32164 <https:////gerrit.fd.io/r/c/vpp/+/32164>`_ [VeC 122]: acl: change the algorithm for cleaning the sessions from purgatory

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 95]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VEc 1]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

**Daniel Beres** <daniel.beres@pantheon.tech>:

  | `38459 <https:////gerrit.fd.io/r/c/vpp/+/38459>`_ [VEc 0]: nat: fix nat44 vrf handlers

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [VEc 18]: ebuild: adding libmemif to debian packages
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 58]: libmemif: added tests

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37836 <https:////gerrit.fd.io/r/c/vpp/+/37836>`_ [VEc 0]: dpdk-cryptodev: enq/deq scheme rework
  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 37]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37420 <https:////gerrit.fd.io/r/c/vpp/+/37420>`_ [Vec 127]: tests: remove intermittent failing tests on vpp_debug image

**Dmitry Valter** <dvalter@protonmail.com>:

  | `38082 <https:////gerrit.fd.io/r/c/vpp/+/38082>`_ [VeC 52]: lb: fix flow table update vector handing with ASAN
  | `38062 <https:////gerrit.fd.io/r/c/vpp/+/38062>`_ [VeC 56]: stats: fix node name compatison

**Duncan Eastoe** <duncaneastoe+github@gmail.com>:

  | `37750 <https:////gerrit.fd.io/r/c/vpp/+/37750>`_ [VeC 106]: stats: fix memory leak in stat_segment_dump_r()

**Filip Varga** <fivarga@cisco.com>:

  | `35444 <https:////gerrit.fd.io/r/c/vpp/+/35444>`_ [veC 149]: nat: nat44-ed cleanup & improvements
  | `35966 <https:////gerrit.fd.io/r/c/vpp/+/35966>`_ [veC 149]: nat: nat44-ed update timeout api
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VeC 149]: nat: nat66 cli bug fix
  | `34929 <https:////gerrit.fd.io/r/c/vpp/+/34929>`_ [veC 149]: nat: det44 map configuration improvements
  | `36724 <https:////gerrit.fd.io/r/c/vpp/+/36724>`_ [VeC 149]: nat: fixing incosistency in use of sw_if_index
  | `36480 <https:////gerrit.fd.io/r/c/vpp/+/36480>`_ [VeC 149]: nat: nat64 fix add_del calls requirements

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `37764 <https:////gerrit.fd.io/r/c/vpp/+/37764>`_ [VEc 28]: wireguard: under-load state determination update

**GaoChX** <chiso.gao@gmail.com>:

  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VeC 73]: interface: fix crash if vnet_hw_if_get_rx_queue return zero

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `37248 <https:////gerrit.fd.io/r/c/vpp/+/37248>`_ [VeC 178]: urpf: add show urpf cli

**Huawei LI** <lihuawei_zzu@163.com>:

  | `37727 <https:////gerrit.fd.io/r/c/vpp/+/37727>`_ [Vec 100]: nat: make nat44 session limit api reinit flow_hash with new buckets.
  | `37726 <https:////gerrit.fd.io/r/c/vpp/+/37726>`_ [Vec 111]: nat: fix crash when set nat44 session limit with nonexisted vrf.
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VeC 122]: policer: fix crash when delete interface policer classify.
  | `37651 <https:////gerrit.fd.io/r/c/vpp/+/37651>`_ [VeC 122]: classify: fix classify session cli.

**Jieqiang Wang** <jieqiang.wang@arm.com>:

  | `38527 <https:////gerrit.fd.io/r/c/vpp/+/38527>`_ [vEC 4]: rdma: do not set txq cq attribute to be compressed

**Jing Peng** <jing@meter.com>:

  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VeC 149]: nat: fix nat44-ed outside address selection
  | `36597 <https:////gerrit.fd.io/r/c/vpp/+/36597>`_ [VeC 149]: nat: fix nat44-ed API

**Kai Luo** <kailuo.nk@gmail.com>:

  | `37269 <https:////gerrit.fd.io/r/c/vpp/+/37269>`_ [VeC 167]: memif: fix uninitialized variable warning

**Klement Sekera** <klement.sekera@gmail.com>:

  | `38042 <https:////gerrit.fd.io/r/c/vpp/+/38042>`_ [VEc 17]: tests: enhance counter comparison error message
  | `38041 <https:////gerrit.fd.io/r/c/vpp/+/38041>`_ [VeC 57]: tests: refactor extra_vpp_punt_config

**Matz von Finckenstein** <matz.vf@gmail.com>:

  | `38091 <https:////gerrit.fd.io/r/c/vpp/+/38091>`_ [Vec 39]: stats: Updated go version URL for the install script Added log flag to pass in logging file destination as an alternate logging destination from syslog

**Maxime Peim** <mpeim@cisco.com>:

  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VEc 7]: ipsec: huge anti-replay window support
  | `37941 <https:////gerrit.fd.io/r/c/vpp/+/37941>`_ [VeC 63]: classify: bypass drop filter on specific error

**Miguel Borges de Freitas** <miguel-r-freitas@alticelabs.com>:

  | `37532 <https:////gerrit.fd.io/r/c/vpp/+/37532>`_ [Vec 108]: cnat: fix cnat_translation_cli_add_del call for del with INVALID_INDEX

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 149]: nat: fix tcp session reopen in nat44-ed

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `33726 <https:////gerrit.fd.io/r/c/vpp/+/33726>`_ [VeC 163]: vlib: introduce an inter worker interrupts efds

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32820 <https:////gerrit.fd.io/r/c/vpp/+/32820>`_ [VeC 175]: cnat: better cnat snat-policy cli
  | `33264 <https:////gerrit.fd.io/r/c/vpp/+/33264>`_ [VeC 175]: pbl: Port based balancer

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VEc 17]: ip: IP address family common input node

**Ondrej Fabry** <ondrej@fabry.dev>:

  | `38498 <https:////gerrit.fd.io/r/c/vpp/+/38498>`_ [vEc 0]: Update info about GoVPP

**Sergey Matov** <sergey.matov@travelping.com>:

  | `31319 <https:////gerrit.fd.io/r/c/vpp/+/31319>`_ [VeC 149]: nat: DET: Allow unknown protocol translation

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `38305 <https:////gerrit.fd.io/r/c/vpp/+/38305>`_ [VeC 31]: teib: fix nh-table-id
  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [Vec 59]: virtio: allocate frame per interface

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37939 <https:////gerrit.fd.io/r/c/vpp/+/37939>`_ [VEc 20]: ip: support flow-hash gtpv1teid
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 40]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `37162 <https:////gerrit.fd.io/r/c/vpp/+/37162>`_ [VeC 149]: nat: fix the wrong unformat type
  | `36790 <https:////gerrit.fd.io/r/c/vpp/+/36790>`_ [VeC 176]: map: lpm 128 lookup error.

**Tianyu Li** <tianyu.li@arm.com>:

  | `37530 <https:////gerrit.fd.io/r/c/vpp/+/37530>`_ [vec 147]: dpdk: fix interface name w/ the same PCI bus/slot/function

**Vladimir Bernolak** <vladimir.bernolak@pantheon.tech>:

  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VeC 149]: nat: det44 map configuration improvements + tests

**Vladislav Grishenko** <themiron@mail.ru>:

  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VeC 116]: nat: fix nat44_ed set_session_limit crash
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 149]: nat: add nat44-ed session filtering by fib table

**Vratko Polak** <vrpolak@cisco.com>:

  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 67]: api: fix vl_socket_write_ready

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38336 <https:////gerrit.fd.io/r/c/vpp/+/38336>`_ [VEc 28]: ip: IPv4 Fragmentation - fix fragment id alloc not multi-thread safe
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VeC 42]: misc: fix feature dispatch possible crashed when feature config changed by user
  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [Vec 65]: api: fix api msg thread safe setting not work
  | `37681 <https:////gerrit.fd.io/r/c/vpp/+/37681>`_ [Vec 118]: udp: hand off packet to right session thread
  | `36704 <https:////gerrit.fd.io/r/c/vpp/+/36704>`_ [VeC 149]: nat: auto forward inbound packet for local server session app with snat
  | `37376 <https:////gerrit.fd.io/r/c/vpp/+/37376>`_ [VeC 166]: vlib: unix cli - fix input's buffer may be freed when using
  | `37375 <https:////gerrit.fd.io/r/c/vpp/+/37375>`_ [VeC 167]: ipsec: fix ipsec linked key not freed when sa deleted

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `37840 <https:////gerrit.fd.io/r/c/vpp/+/37840>`_ [vEc 2]: dpdk: bump to dpdk 22.11
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VEc 15]: interface dpdk avf: introducing setting RSS hash key feature

**Yulong Pei** <yulong.pei@intel.com>:

  | `38135 <https:////gerrit.fd.io/r/c/vpp/+/38135>`_ [VEc 10]: af_xdp: change default queue size as kernel xsk default

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vEC 16]: vrrp: dump vrrp vr peer Type: fix

**jinshaohui** <jinsh11@chinatelecom.cn>:

  | `38400 <https:////gerrit.fd.io/r/c/vpp/+/38400>`_ [vEC 17]: vlib:process node scheduling use timing_wheel have problem.
  | `30929 <https:////gerrit.fd.io/r/c/vpp/+/30929>`_ [Vec 129]: vppinfra: fix memory issue in mhash
  | `37297 <https:////gerrit.fd.io/r/c/vpp/+/37297>`_ [Vec 132]: ping: fix ping ipv6 address set packet size greater than  mtu,packet drop

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 117]: nat: add local addresses correctly in nat lb static mapping
  | `37566 <https:////gerrit.fd.io/r/c/vpp/+/37566>`_ [veC 137]: policer: add policer classify to output path

**steven luong** <sluong@cisco.com>:

  | `37105 <https:////gerrit.fd.io/r/c/vpp/+/37105>`_ [VeC 163]: vppinfra: add time error counters to stats segment

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `38497 <https:////gerrit.fd.io/r/c/vpp/+/38497>`_ [vEC 8]: crypto:  0UDP packet dropped when ipsec policy configured

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
authors          75
maintainers      49
committers       0
abandoned        0
================ ===

