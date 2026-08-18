
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Tuesday 2026-08-18, 02:19:57
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

abf: **Neale Ranns** <neale@graphiant.com>
  | `46339 <https:////gerrit.fd.io/r/c/vpp/+/46339>`_ [VECr 5]: abf: reject attachment to a non-existent policy instead of asserting

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `46474 <https:////gerrit.fd.io/r/c/vpp/+/46474>`_ [VECr 0]: vlib crypto ipsec: preserve scalar frame metadata

build: **Damjan Marion** <damarion@cisco.com>
  | `46433 <https:////gerrit.fd.io/r/c/vpp/+/46433>`_ [VECr 0]: dpdk: bump to DPDK 26.07 and rdma-core 64.0
  | `46462 <https:////gerrit.fd.io/r/c/vpp/+/46462>`_ [VECr 3]: build: update to openssl 4.0.1 in optional deps
  | `46392 <https:////gerrit.fd.io/r/c/vpp/+/46392>`_ [VECr 7]: octeon: update octeon roc version

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `46474 <https:////gerrit.fd.io/r/c/vpp/+/46474>`_ [VECr 0]: vlib crypto ipsec: preserve scalar frame metadata

dev: **Damjan Marion** <damarion@cisco.com>
  | `46393 <https:////gerrit.fd.io/r/c/vpp/+/46393>`_ [VECr 9]: dev: add port attribute for speed capability
  | `46282 <https:////gerrit.fd.io/r/c/vpp/+/46282>`_ [VECr 14]: dev: advertise TX UDP GSO

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `46503 <https:////gerrit.fd.io/r/c/vpp/+/46503>`_ [VECr 0]: docs: Add Ubuntu prerequisites for vpp build
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 1]: misc: patch to test CI infra
  | `46457 <https:////gerrit.fd.io/r/c/vpp/+/46457>`_ [VECr 5]: sfdp: add example custom parser

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `46433 <https:////gerrit.fd.io/r/c/vpp/+/46433>`_ [VECr 0]: dpdk: bump to DPDK 26.07 and rdma-core 64.0
  | `45699 <https:////gerrit.fd.io/r/c/vpp/+/45699>`_ [VECr 10]: dpdk: buffer bug fixes

fib: **Neale Ranns** <neale@graphiant.com>
  | `46338 <https:////gerrit.fd.io/r/c/vpp/+/46338>`_ [VECr 5]: fib: tolerate a NULL rewrite in vnet_rewrite_for_sw_interface
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VECr 20]: fib: dump by src not only contributing routes

flow: **Damjan Marion** <damarion@cisco.com>
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 0]: flow: add flow template and async range infrastructure

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `46432 <https:////gerrit.fd.io/r/c/vpp/+/46432>`_ [VECr 0]: hs-test: tag docker images per test run
  | `46369 <https:////gerrit.fd.io/r/c/vpp/+/46369>`_ [VECr 18]: hs-test: switch hsi suite to tap interfaces
  | `46341 <https:////gerrit.fd.io/r/c/vpp/+/46341>`_ [VECr 24]: hsa: make TLS client CLI MP-safe

iavf: **Damjan Marion** <damarion@cisco.com>
  | `46271 <https:////gerrit.fd.io/r/c/vpp/+/46271>`_ [VECr 15]: iavf: fix iavf_tx_fill_ctx_desc ph buf seg fault
  | `46261 <https:////gerrit.fd.io/r/c/vpp/+/46261>`_ [VECr 15]: iavf: fix rx queue max_pkt_size value set on init
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 19]: iavf: fix native TSO datapath

interface: **Dave Barach** <vpp@barachs.net>
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 0]: flow: add flow template and async range infrastructure

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `46051 <https:////gerrit.fd.io/r/c/vpp/+/46051>`_ [VECr 13]: ip: fix punt socket rx when multiple FDs are ready
  | `46355 <https:////gerrit.fd.io/r/c/vpp/+/46355>`_ [VECr 20]: ip: fix fragmentation with negative buffer offset
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VECr 20]: fib: dump by src not only contributing routes

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `46442 <https:////gerrit.fd.io/r/c/vpp/+/46442>`_ [VECr 4]: vnet: install missing vnet headers

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `46425 <https:////gerrit.fd.io/r/c/vpp/+/46425>`_ [VECr 12]: octeon: add support to set link-speed

papi: **Ole Troan** <otroan@employees.org>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46459 <https:////gerrit.fd.io/r/c/vpp/+/46459>`_ [VECr 4]: papi: fix ip address family version to use public api

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `46315 <https:////gerrit.fd.io/r/c/vpp/+/46315>`_ [VECr 25]: quic: quic_quicly add uso support

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `46506 <https:////gerrit.fd.io/r/c/vpp/+/46506>`_ [VECr 0]: rdma: fix mlx5 RX CQ doorbell byte order

session: **Florin Coras** <fcoras@cisco.com>
  | `46473 <https:////gerrit.fd.io/r/c/vpp/+/46473>`_ [VECr 3]: session: revalidate ct listener during accept
  | `46452 <https:////gerrit.fd.io/r/c/vpp/+/46452>`_ [VECr 6]: session: handle failed ct half-open migration
  | `46180 <https:////gerrit.fd.io/r/c/vpp/+/46180>`_ [VECr 12]: session: check event collector lookups
  | `46379 <https:////gerrit.fd.io/r/c/vpp/+/46379>`_ [VECr 18]: session: add half_close support for cut-through transport
  | `46178 <https:////gerrit.fd.io/r/c/vpp/+/46178>`_ [VECr 20]: session: validate app for async connect RPC
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 26]: udp: add segmentation offload support

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `46457 <https:////gerrit.fd.io/r/c/vpp/+/46457>`_ [VECr 5]: sfdp: add example custom parser

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `46424 <https:////gerrit.fd.io/r/c/vpp/+/46424>`_ [VECr 3]: sfdp: add lifecycle records to session stats ring

sfdp_services_sample: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>
  | `46457 <https:////gerrit.fd.io/r/c/vpp/+/46457>`_ [VECr 5]: sfdp: add example custom parser

tcp: **Florin Coras** <fcoras@cisco.com>
  | `46311 <https:////gerrit.fd.io/r/c/vpp/+/46311>`_ [VECr 26]: tcp: handle retransmitted SYN-ACK in TIME-WAIT

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46474 <https:////gerrit.fd.io/r/c/vpp/+/46474>`_ [VECr 0]: vlib crypto ipsec: preserve scalar frame metadata
  | `46424 <https:////gerrit.fd.io/r/c/vpp/+/46424>`_ [VECr 3]: sfdp: add lifecycle records to session stats ring
  | `46460 <https:////gerrit.fd.io/r/c/vpp/+/46460>`_ [VECr 4]: tests: remove TestNAT44EDMW from normal test list
  | `46338 <https:////gerrit.fd.io/r/c/vpp/+/46338>`_ [VECr 5]: fib: tolerate a NULL rewrite in vnet_rewrite_for_sw_interface
  | `46339 <https:////gerrit.fd.io/r/c/vpp/+/46339>`_ [VECr 5]: abf: reject attachment to a non-existent policy instead of asserting
  | `46457 <https:////gerrit.fd.io/r/c/vpp/+/46457>`_ [VECr 5]: sfdp: add example custom parser

udp: **Florin Coras** <fcoras@cisco.com>
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 26]: udp: add segmentation offload support

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `46474 <https:////gerrit.fd.io/r/c/vpp/+/46474>`_ [VECr 0]: vlib crypto ipsec: preserve scalar frame metadata
  | `46178 <https:////gerrit.fd.io/r/c/vpp/+/46178>`_ [VECr 20]: session: validate app for async connect RPC
  | `46311 <https:////gerrit.fd.io/r/c/vpp/+/46311>`_ [VECr 26]: tcp: handle retransmitted SYN-ACK in TIME-WAIT

vcl: **Florin Coras** <fcoras@cisco.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 1]: misc: patch to test CI infra
  | `46265 <https:////gerrit.fd.io/r/c/vpp/+/46265>`_ [VECr 18]: vcl: add vls_unregister_vcl_worker for explicit worker teardown

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46434 <https:////gerrit.fd.io/r/c/vpp/+/46434>`_ [VECr 9]: vlib: fix log2 histogram overflow bin writing past the bin vector
  | `46370 <https:////gerrit.fd.io/r/c/vpp/+/46370>`_ [VECr 18]: vlib: fix cli mem leak in line mode

vperf: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `46341 <https:////gerrit.fd.io/r/c/vpp/+/46341>`_ [VECr 24]: hsa: make TLS client CLI MP-safe

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `46372 <https:////gerrit.fd.io/r/c/vpp/+/46372>`_ [VECr 12]: vppinfra: do not apply VEC512 tricks for ip6
  | `46368 <https:////gerrit.fd.io/r/c/vpp/+/46368>`_ [VECr 20]: vppinfra: make vec_foreach_pointer empty-safe
  | `46352 <https:////gerrit.fd.io/r/c/vpp/+/46352>`_ [VECr 22]: vppinfra: serialize VM map page size lookup

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [Vec 63]: ip_validate: new plugin to drop packets with invalid addresses

**Akos Orban** <orbanakos2001@gmail.com>:

  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 70]: cnat: fix show cnat client showing invalid for client id
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 70]: cnat: fix show cnat translation for specific translation id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 139]: vhost: fix rxvq interrupts triggered because of race

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VeC 87]: snort: don't store snort metadata in buffer

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `46256 <https:////gerrit.fd.io/r/c/vpp/+/46256>`_ [vec 32]: crypto: openssl - check ctx alloc/init in key-add
  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VeC 110]: map: enhance map plugin to support per-vrf rules

**Anton Blazhko** <ablazhko@cisco.com>:

  | `45808 <https:////gerrit.fd.io/r/c/vpp/+/45808>`_ [Vec 33]: devices: Convert PIPE to plugin

**Aritra Basu** <aritrbas@cisco.com>:

  | `46249 <https:////gerrit.fd.io/r/c/vpp/+/46249>`_ [VeC 35]: kube-test: inherit pod MTU for memif test tap
  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [Vec 41]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VeC 41]: vperf: drop residual echo/vcl_test terminology
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VeC 48]: tcp: add TCP fast open support (RFC 7413)
  | `46167 <https:////gerrit.fd.io/r/c/vpp/+/46167>`_ [veC 52]: kube-test: retry Job finalizer cleanup conflicts
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VeC 65]: interface: enable IPv6 link state on unnumbered interfaces
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VeC 65]: vlib: fix trace flag loss when multiple pending frames share next frame
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 150]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 152]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 152]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 152]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 152]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 157]: ip6-nd: fix unicast NA handling in ND proxy

**Benoît Ganne** <bganne@cisco.com>:

  | `46117 <https:////gerrit.fd.io/r/c/vpp/+/46117>`_ [VeC 56]: vppapigen: fix vppapigen depfile without imports
  | `46087 <https:////gerrit.fd.io/r/c/vpp/+/46087>`_ [VeC 56]: cnat: wait for cnat scanner session cleanup

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [veC 72]: ikev2: add Curve25519 and Curve448 DH groups

**Dave Wallace** <dwallacelf@gmail.com>:

  | `46308 <https:////gerrit.fd.io/r/c/vpp/+/46308>`_ [vEC 13]: docs: only list release notes for supported versions
  | `46075 <https:////gerrit.fd.io/r/c/vpp/+/46075>`_ [vEC 13]: docs: update tsc vulnerability management process

**Dennis Lanov** <dennis.lanov@gmail.com>:

  | `46270 <https:////gerrit.fd.io/r/c/vpp/+/46270>`_ [VeC 33]: acl: correct interface command help

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 154]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 154]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**Florin Coras** <florin.coras@gmail.com>:

  | `46508 <https:////gerrit.fd.io/r/c/vpp/+/46508>`_ [vEC 0]: tcp: update sack scoreboard directly on cumulative acks

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VEc 0]: ipsec: IPTFS (RFC 9347) support (iptfs commit 1 of 3)
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VeC 63]: crypto: add op tracing capability
  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [Vec 103]: dpdk: tracing improvements

**GregMiller** <greg@gregmiller.co.za>:

  | `46129 <https:////gerrit.fd.io/r/c/vpp/+/46129>`_ [VeC 55]: pppoe: native per-session rx policing in pppoe-decap node
  | `46125 <https:////gerrit.fd.io/r/c/vpp/+/46125>`_ [VeC 55]: pppoe: add combined subscriber session provisioning API

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VEc 0]: sfdp: add sfdp-session-stats service
  | `46362 <https:////gerrit.fd.io/r/c/vpp/+/46362>`_ [VEc 18]: sfdp: add api sfdp_kill_session_batch
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VeC 47]: sfdp: modify tenant_index type from u16 to u32
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VeC 54]: flow: add parameter to pre-allocate global pool
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [veC 54]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VeC 54]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [veC 54]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [Vec 55]: sfdp: add verdict-testbench service
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VeC 55]: flow: add APIs to support new flow actions
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VeC 55]: flow: add flow aging support
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VeC 67]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VeC 67]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [Vec 70]: tracepath: minor refactoring to code
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VeC 91]: sfdp: fix specification of scope_index

**Hanataba Azaka** <northern.snow.x@gmail.com>:

  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [VeC 56]: cnat: make session scanner budget configurable

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `46147 <https:////gerrit.fd.io/r/c/vpp/+/46147>`_ [Vec 52]: npol: support prednat policies
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [Vec 56]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 144]: tests: reduce sleep interval in ip-neighbor age test
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 173]: crypto: unify per-thread key_data allocation

**Janik** <janik.haag@imc.com>:

  | `46122 <https:////gerrit.fd.io/r/c/vpp/+/46122>`_ [VEc 27]: build: fix make install-deps for fedora targets
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VeC 56]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VeC 56]: vcl: add regression test for ignorable flags
  | `46121 <https:////gerrit.fd.io/r/c/vpp/+/46121>`_ [VeC 56]: sasc: fix gcc uninitialized warning

**Jerome Tollet** <jtollet@cisco.com>:

  | `46465 <https:////gerrit.fd.io/r/c/vpp/+/46465>`_ [vEc 0]: rdma: add mlx5 enhanced MPW transmit path
  | `46155 <https:////gerrit.fd.io/r/c/vpp/+/46155>`_ [VEc 0]: rdma: fix verbs port selection
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VEc 0]: rdma: add mlx5 DV TSO support for raw packet tx
  | `45819 <https:////gerrit.fd.io/r/c/vpp/+/45819>`_ [VeC 33]: tcp: add TCP input GRO before input lookup
  | `45775 <https:////gerrit.fd.io/r/c/vpp/+/45775>`_ [VeC 97]: tcp: fix pure ACK incorrectly chained as GRO candidate
  | `45759 <https:////gerrit.fd.io/r/c/vpp/+/45759>`_ [VeC 97]: tcp: support chained buffers in GRO
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VeC 97]: tcp: allow selective GRO enablement
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 111]: virtio: add native plugin L2 xconnect test with QEMU

**Jiajun Liang** <3138947285@qq.com>:

  | `45677 <https:////gerrit.fd.io/r/c/vpp/+/45677>`_ [Vec 38]: linux-cp: guard PPPOX interface type and tolerate missing neighbor
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VeC 55]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VeC 55]: dpdk: log MFIB MAC replay tolerance at debug level
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [VeC 55]: rdma: steer PPPoE discovery and session flows

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [Vec 68]: ip bonding hash: inner-aware flow hash (opt-in)

**Justin Thomas** <justin@jdt.io>:

  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VeC 136]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VeC 136]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

**Klement Sekera** <ksekera@netgate.com>:

  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VeC 34]: build: include GNUInstallDirs in VPPConfig
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VeC 34]: api: add build-time python stub generation via vppapigen
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VeC 117]: vppinfra: add cast to prevent warning

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [Vec 67]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [Vec 67]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Matus Fabian** <matfabia@cisco.com>:

  | `46502 <https:////gerrit.fd.io/r/c/vpp/+/46502>`_ [vEC 0]: tls: tls_get_engine_type fix out of bounds read
  | `46283 <https:////gerrit.fd.io/r/c/vpp/+/46283>`_ [VeC 31]: iavf: add UDP segmentation offload support
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VeC 34]: iavf: add setup documentation
  | `46079 <https:////gerrit.fd.io/r/c/vpp/+/46079>`_ [veC 52]: hs-test: temporarily disable core file removal

**Maxime Peim** <maxime.peim@gmail.com>:

  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [vEc 0]: vlib: add per-thread index pool cache
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [vec 45]: dpdk: support async flow offload
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [veC 68]: docs: document build-time VPP parameters
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VeC 74]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [vec 74]: flow: add per-thread flow pool cache for multi-worker safety
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [veC 74]: dpdk: multi-thread async flow offload with per-worker caches
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VeC 147]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VeC 147]: gso: implement IPv6 extension header traversal
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 153]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 153]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 153]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 153]: policer: reject deletion of policer used by punt policing

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [veC 87]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VEc 0]: ipip: fix support for ipip6o6 from linux tunnel
  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VeC 132]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 152]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 158]: sfdp: add blacklist/whitelist to snort service

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 131]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 131]: ip6-nd: add nd-proxy all dst
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 139]: ip6: fix show ip6-ll cli if selector

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vec 74]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `46380 <https:////gerrit.fd.io/r/c/vpp/+/46380>`_ [VEc 17]: vppapigen: fix unaligned access to packed messages
  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [Vec 124]: papi: improve performance on set_errors

**Onong Tayeng** <onong.tayeng@gmail.com>:

  | `46471 <https:////gerrit.fd.io/r/c/vpp/+/46471>`_ [vEc 0]: cnat: improve flow statistics and error coverage

**Pim van Pelt** <pim@ipng.nl>:

  | `46038 <https:////gerrit.fd.io/r/c/vpp/+/46038>`_ [Vec 61]: ip6-nd: fix crash in link-local target NS
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VeC 131]: lb: Add punt feature to per-port VIPs

**Qi Zhang** <zzqqqqwq77@gmail.com>:

  | `46458 <https:////gerrit.fd.io/r/c/vpp/+/46458>`_ [vEC 1]: vlib: detect freed buffer‑chain on node dispatch for double‑free debug

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [Vec 82]: pfc: add framework for priority flow control
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VeC 94]: octeon: add PFC support

**Robert Shearman** <robertshearman@gmail.com>:

  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [vEC 12]: ip: fix adjacent packet overwrite with ip frags
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [vEC 12]: vppapigen: fix inconsistency in paths JSON
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [vEC 12]: ip: fix ip mroute bulk insertion CLI for certain inputs
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [vEC 12]: ip: fix adjacent packet overwrite with ip6 frags
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [vEC 12]: vlib: ASAN-poison unallocated buffers
  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [vEc 22]: misc: fix potential OOB read during flow hash calculations

**Samuel Benko** <sbenko@cisco.com>:

  | `46431 <https:////gerrit.fd.io/r/c/vpp/+/46431>`_ [vEC 0]: hs-test: isolate concurrent test runs
  | `46449 <https:////gerrit.fd.io/r/c/vpp/+/46449>`_ [vEC 0]: hs-test: give each test run its own CPUs
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VeC 54]: tls: propagate verify config for dtls

**Sergiy Bachynskyy** <sbachyns@cisco.com>:

  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VeC 40]: ipfix: move to a plugin

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [VEc 0]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair

**Viacheslav Zakharchenko** <vzakharc@cisco.com>:

  | `45807 <https:////gerrit.fd.io/r/c/vpp/+/45807>`_ [Vec 33]: bfd: Introduce vppinfra/callback_data based vnet notifier for FIB/ADJ notifications
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [Vec 34]: bfd: Extract to plugin

**Vladimir Lavor** <vlavor@cisco.com>:

  | `46268 <https:////gerrit.fd.io/r/c/vpp/+/46268>`_ [VeC 32]: vlib: expose error severity in stats segment

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [Vec 91]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [veC 139]: vppinfra: collect heap stats in constant time

**Vratko Polak** <vrpolak@cisco.com>:

  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vec 80]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [veC 124]: empty change for GHA(CSIT) testing

**Wei Wang** <weiwa@cisco.com>:

  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [Vec 53]: tls: tls session resumption code and host stack tests

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VeC 82]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer
  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [Vec 82]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [veC 83]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VeC 83]: vlib: fix process state format output wrapped by extra quotes
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vec 89]: vlib: pre-input node should be dispatched before input node

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [Vec 45]: vppinfra: add loongarch64 architecture support

**Yuto Suzuki** <offside.items03@icloud.com>:

  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VEc 26]: ip6-nd: support RDNSS option in IPv6 RA
  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VEc 26]: ip6-nd: update secondary RA prefixes for subnets

**jiang li** <1394788707@qq.com>:

  | `46469 <https:////gerrit.fd.io/r/c/vpp/+/46469>`_ [VEc 0]: dispatch-trace: fix SIGSEGV/SIGABRT on multi-worker handoff

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [veC 98]: vlib: fix '\' command input will causes memory out of bounds
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [Vec 139]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [Vec 139]: dns: support ipv6 server to resolve name
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VeC 140]: build rpm-packaging: make vpp rpm package for kylinV11

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 112]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [veC 60]: cnat: add scope_id to session key

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 151]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 139]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [veC 139]: lb: fix API byte order and IPv4 prefix length handling

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VeC 108]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VeC 95]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VeC 97]: tls: fix picotls partial record handling
  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [Vec 98]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [Vec 104]: session: make transport to use application's segment manager

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [A 180]: ip6-nd: support RA pfx info option with flag L&!A

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
authors          153
maintainers      42
committers       0
abandoned        1
================ ===

