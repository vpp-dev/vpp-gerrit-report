
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Tuesday 2023-06-13, 02:21:11
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
  | `38963 <https:////gerrit.fd.io/r/c/vpp/+/38963>`_ [VECr 0]: af_xdp: set frame_no_append flag

api: **Dave Barach** <vpp@barachs.net>
  | `38648 <https:////gerrit.fd.io/r/c/vpp/+/38648>`_ [VECr 0]: api: memclnt - Mark old message versions as deprecated

avf: **Damjan Marion** <damarion@cisco.com>
  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VECr 7]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 7]: interface dpdk avf: introducing setting RSS hash key feature

build: **Damjan Marion** <damarion@cisco.com>
  | `38782 <https:////gerrit.fd.io/r/c/vpp/+/38782>`_ [VECr 24]: af_xdp: fix the error of linking to libbpf.a

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VECr 13]: crypto: fix async frame memory crash if frame pool expanded when using

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `39005 <https:////gerrit.fd.io/r/c/vpp/+/39005>`_ [VECr 5]: docs: fix packages path in tutorial

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VECr 7]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 7]: interface dpdk avf: introducing setting RSS hash key feature
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VECr 18]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

dpdk-cryptodev: **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38749 <https:////gerrit.fd.io/r/c/vpp/+/38749>`_ [VECr 3]: dpdk-cryptodev: introduce sw_ring to the crypto op data path
  | `39018 <https:////gerrit.fd.io/r/c/vpp/+/39018>`_ [VECr 3]: dpdk-cryptodev: introduce sw_ring
  | `39019 <https:////gerrit.fd.io/r/c/vpp/+/39019>`_ [VECr 3]: dpdk-cryptodev: enq/deq scheme rework

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 18]: ethernet: run callbacks for subifs too when mac changes

fib: **Neale Ranns** <neale@graphiant.com>
  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VECr 19]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

flow: **Damjan Marion** <damarion@cisco.com>
  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VECr 7]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VECr 18]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

interface: **Dave Barach** <vpp@barachs.net>
  | `39002 <https:////gerrit.fd.io/r/c/vpp/+/39002>`_ [VECr 0]: vppapigen: fix crash with autoendian arrays
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 7]: interface dpdk avf: introducing setting RSS hash key feature

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38639 <https:////gerrit.fd.io/r/c/vpp/+/38639>`_ [VECr 0]: api: ip - Mark old message versions as deprecated
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VECr 21]: ip: make running_fragment_id thread safe

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38641 <https:////gerrit.fd.io/r/c/vpp/+/38641>`_ [VECr 0]: api: ipsec - Mark old message versions as deprecated
  | `38791 <https:////gerrit.fd.io/r/c/vpp/+/38791>`_ [VECr 3]: ipsec: move udp/esp packet processing in the inline function ipsec_udp_encap_esp_packet_process
  | `38793 <https:////gerrit.fd.io/r/c/vpp/+/38793>`_ [VECr 6]: ipsec: separate UDP and UDP-encapsulated ESP packet processing
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VECr 13]: crypto: fix async frame memory crash if frame pool expanded when using

libmemif: **Damjan Marion** <damarion@cisco.com>
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VECr 24]: libmemif: added tests

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `38654 <https:////gerrit.fd.io/r/c/vpp/+/38654>`_ [VECr 0]: api: lcp - Mark old message versions as deprecated
  | `38702 <https:////gerrit.fd.io/r/c/vpp/+/38702>`_ [VECr 5]: linux-cp: Basic MPLS support.

memif: **Damjan Marion** <damarion@cisco.com>
  | `38644 <https:////gerrit.fd.io/r/c/vpp/+/38644>`_ [VECr 0]: api: memif - Mark old message versions as deprecated

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 7]: interface dpdk avf: introducing setting RSS hash key feature
  | `38958 <https:////gerrit.fd.io/r/c/vpp/+/38958>`_ [VECr 10]: vcl: ldp support SO_ORIGINAL_DST

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `38958 <https:////gerrit.fd.io/r/c/vpp/+/38958>`_ [VECr 10]: vcl: ldp support SO_ORIGINAL_DST
  | `38442 <https:////gerrit.fd.io/r/c/vpp/+/38442>`_ [VECr 12]: nat: nat44-ed bug fix
  | `38440 <https:////gerrit.fd.io/r/c/vpp/+/38440>`_ [VECr 14]: nat: nat44-ed cli bug fix
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VECr 20]: nat: nat66 cli bug fix

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VECr 19]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node

pg: **Dave Barach** <vpp@barachs.net>
  | `38649 <https:////gerrit.fd.io/r/c/vpp/+/38649>`_ [VECr 0]: api: pg - Mark old message versions as deprecated

session: **Florin Coras** <fcoras@cisco.com>
  | `38958 <https:////gerrit.fd.io/r/c/vpp/+/38958>`_ [VECr 10]: vcl: ldp support SO_ORIGINAL_DST

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `38651 <https:////gerrit.fd.io/r/c/vpp/+/38651>`_ [VECr 0]: api: tapv2 - Mark old message versions as deprecated

tcp: **Florin Coras** <fcoras@cisco.com>
  | `38958 <https:////gerrit.fd.io/r/c/vpp/+/38958>`_ [VECr 10]: vcl: ldp support SO_ORIGINAL_DST

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `38792 <https:////gerrit.fd.io/r/c/vpp/+/38792>`_ [VECr 4]: ipsec: modify IPsec related tests to send and verify UDP-encapsulated ESP traffics
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 18]: ethernet: run callbacks for subifs too when mac changes

udp: **Florin Coras** <fcoras@cisco.com>
  | `38958 <https:////gerrit.fd.io/r/c/vpp/+/38958>`_ [VECr 10]: vcl: ldp support SO_ORIGINAL_DST

vapi: **Ole Troan** <ot@cisco.com>
  | `38491 <https:////gerrit.fd.io/r/c/vpp/+/38491>`_ [VECr 28]: vppapigen: c++ vapi stream message codegen

vcl: **Florin Coras** <fcoras@cisco.com>
  | `38958 <https:////gerrit.fd.io/r/c/vpp/+/38958>`_ [VECr 10]: vcl: ldp support SO_ORIGINAL_DST
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 12]: misc: patch to test CI infra changes

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [VECr 10]: virtio: use fast-path for ethernet-input if possible

vppapigen: **Ole Troan** <otroan@employees.org>
  | `39002 <https:////gerrit.fd.io/r/c/vpp/+/39002>`_ [VECr 0]: vppapigen: fix crash with autoendian arrays

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VECr 13]: crypto: fix async frame memory crash if frame pool expanded when using

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `38011 <https:////gerrit.fd.io/r/c/vpp/+/38011>`_ [veC 136]: wireguard: move buffer when insufficient pre_data left

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `38788 <https:////gerrit.fd.io/r/c/vpp/+/38788>`_ [vEC 18]: TEST: blank out the SVM fifo tests
  | `38781 <https:////gerrit.fd.io/r/c/vpp/+/38781>`_ [vEC 28]: TEST: remove the rdma mappings
  | `38567 <https:////gerrit.fd.io/r/c/vpp/+/38567>`_ [veC 76]: TEST: make test string a test crash, for testing
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VeC 88]: fateshare: a plugin for managing child processes

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 175]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VeC 34]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

**Damjan Marion** <dmarion@0xa5.net>:

  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [VEc 12]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 98]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37836 <https:////gerrit.fd.io/r/c/vpp/+/37836>`_ [VEc 6]: dpdk-cryptodev: enq/deq scheme rework
  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [VEc 12]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 98]: ipsec: esp_encrypt prefetch and unroll

**Dave Wallace** <dwallacelf@gmail.com>:

  | `39029 <https:////gerrit.fd.io/r/c/vpp/+/39029>`_ [vEC 0]: tests: run interface tests as a regular test
  | `39021 <https:////gerrit.fd.io/r/c/vpp/+/39021>`_ [vEC 3]: tests: save api trace for testcases in json format

**Dmitry Valter** <dvalter@protonmail.com>:

  | `38082 <https:////gerrit.fd.io/r/c/vpp/+/38082>`_ [VeC 132]: lb: fix flow table update vector handing with ASAN
  | `38071 <https:////gerrit.fd.io/r/c/vpp/+/38071>`_ [veC 133]: vppinfra: fix preallocated pool_put OOB with ASAN
  | `38070 <https:////gerrit.fd.io/r/c/vpp/+/38070>`_ [veC 133]: lb: fix flow table update vector handing with ASAN
  | `38062 <https:////gerrit.fd.io/r/c/vpp/+/38062>`_ [VeC 136]: stats: fix node name compatison

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 55]: dpdk: use adapter MTU in max_frame_size setting

**GaoChX** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 33]: nat: nat44-ed get out2in workers failed for static mapping without port
  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VeC 153]: interface: fix crash if vnet_hw_if_get_rx_queue return zero

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `38285 <https:////gerrit.fd.io/r/c/vpp/+/38285>`_ [VeC 108]: ip: fix update checksum in ip4_ttl_inc

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 88]: nat: fix address resolution

**Matz von Finckenstein** <matz.vf@gmail.com>:

  | `38091 <https:////gerrit.fd.io/r/c/vpp/+/38091>`_ [Vec 119]: stats: Updated go version URL for the install script Added log flag to pass in logging file destination as an alternate logging destination from syslog

**Maxime Peim** <mpeim@cisco.com>:

  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VEc 11]: ipsec: huge anti-replay window support
  | `38528 <https:////gerrit.fd.io/r/c/vpp/+/38528>`_ [VeC 74]: ipsec: manually binding an SA to a worker
  | `37941 <https:////gerrit.fd.io/r/c/vpp/+/37941>`_ [VeC 143]: classify: bypass drop filter on specific error

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 73]: nat: fix tcp session reopen in nat44-ed

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `38997 <https:////gerrit.fd.io/r/c/vpp/+/38997>`_ [VEc 0]: vnet: turn vnet_is_packet_traced into callback
  | `39017 <https:////gerrit.fd.io/r/c/vpp/+/39017>`_ [VEc 0]: misc: bpf_trace_filter

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 70]: cnat: remove rwlock on ts
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [VeC 70]: cnat: dont compute offloaded cksums
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 70]: cnat: flag to disable rsession
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 70]: cnat: add ip/client bihash
  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 98]: vppinfra: improve & test abstract socket

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [vEc 24]: ip: IP address family common input node
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VeC 109]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 109]: ip: IPv6 validate input packet's header length does not exist buffer size

**Ondrej Fabry** <ondrej@fabry.dev>:

  | `38650 <https:////gerrit.fd.io/r/c/vpp/+/38650>`_ [vEC 0]: api: sr - Mark old message versions as deprecated
  | `38646 <https:////gerrit.fd.io/r/c/vpp/+/38646>`_ [vEC 0]: api: vxlan - Mark old message versions as deprecated
  | `38643 <https:////gerrit.fd.io/r/c/vpp/+/38643>`_ [vEC 0]: api: af_packet - Mark old message versions as deprecated

**Pim van Pelt** <pim@ipng.nl>:

  | `39022 <https:////gerrit.fd.io/r/c/vpp/+/39022>`_ [VEc 0]: mpls: add mpls_interface_dump

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [Vec 33]: ipsec: esp_encrypt prefetch and unroll - introduce new types
  | `38408 <https:////gerrit.fd.io/r/c/vpp/+/38408>`_ [VeC 96]: ipsec: fix logic in ext_hdr_is_pre_esp
  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [VeC 96]: ipsec: intorduce function esp_prepare_packet_for_enc
  | `38410 <https:////gerrit.fd.io/r/c/vpp/+/38410>`_ [VeC 96]: ipsec: esp_encrypt prefetch and unroll

**Rune Jensen** <runeerle@wgtwo.com>:

  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [veC 74]: gtpu: support non-G-PDU packets and PDU Session

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VeC 42]: linux-cp: auto select tap id when creating lcp pair

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [Vec 47]: srv6-mobile: Implement SRv6 mobile API funcs

**Ting Xu** <ting.xu@intel.com>:

  | `38708 <https:////gerrit.fd.io/r/c/vpp/+/38708>`_ [VEc 19]: idpf: add native idpf driver plugin

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [Vec 60]: mpls: fix possible crashes on tunnel create/delete
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VeC 73]: nat: fix nat44_ed set_session_limit crash
  | `38521 <https:////gerrit.fd.io/r/c/vpp/+/38521>`_ [VeC 73]: nat: improve nat44-ed outside address distribution
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VeC 84]: api: fix mp-safe mark for some messages and add more
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 86]: fib: fix interface resolve from unlinked fib entries
  | `38515 <https:////gerrit.fd.io/r/c/vpp/+/38515>`_ [VeC 86]: fib: fix freed mpls label disposition dpo access

**Vratko Polak** <vrpolak@cisco.com>:

  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 147]: api: fix vl_socket_write_ready

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38733 <https:////gerrit.fd.io/r/c/vpp/+/38733>`_ [VeC 40]: ipsec: improve fast path policy searching performance
  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [veC 45]: linux-cp: fix compiler error with libnl 3.2.x
  | `38728 <https:////gerrit.fd.io/r/c/vpp/+/38728>`_ [veC 47]: ipsec: remove redundant match in ipsec4-input-feature with decrypted esp/ah packet
  | `38535 <https:////gerrit.fd.io/r/c/vpp/+/38535>`_ [VeC 82]: ipsec: fix non-esp packet may be matched as esp packet if flow cache enabled
  | `38500 <https:////gerrit.fd.io/r/c/vpp/+/38500>`_ [VeC 87]: ipsec: missing linear search when flow cache search failed
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 98]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `38336 <https:////gerrit.fd.io/r/c/vpp/+/38336>`_ [Vec 108]: ip: IPv4 Fragmentation - fix fragment id alloc not multi-thread safe
  | `36018 <https:////gerrit.fd.io/r/c/vpp/+/36018>`_ [VeC 109]: ip: fix ip4_ttl_inc calc checksum error when checksum is 0
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VeC 122]: misc: fix feature dispatch possible crashed when feature config changed by user
  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [Vec 145]: api: fix api msg thread safe setting not work

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 53]: af_xdp: optimizing send performance
  | `38312 <https:////gerrit.fd.io/r/c/vpp/+/38312>`_ [VeC 110]: tap: add interface type check

**Yulong Pei** <yulong.pei@intel.com>:

  | `38135 <https:////gerrit.fd.io/r/c/vpp/+/38135>`_ [vec 70]: af_xdp: change default queue size as kernel xsk default

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vEC 18]: vrrp: dump vrrp vr peer

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 73]: nat: add local addresses correctly in nat lb static mapping

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**Huawei LI** <lihuawei_zzu@163.com>:

  | `37727 <https:////gerrit.fd.io/r/c/vpp/+/37727>`_ [A 180]: nat: make nat44 session limit api reinit flow_hash with new buckets.

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
authors          72
maintainers      34
committers       0
abandoned        1
================ ===

