
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Tuesday 2026-07-14, 04:14:43
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

  | `46259 <https:////gerrit.fd.io/r/c/vpp/+/46259>`_ [VECR 0]: hs-test: update golang version to 1.26.5

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 11]: af_xdp: add support for multi-buffer

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `45684 <https:////gerrit.fd.io/r/c/vpp/+/45684>`_ [VECr 15]: buffers: return values; improve debug
  | `46062 <https:////gerrit.fd.io/r/c/vpp/+/46062>`_ [VECr 21]: vlib: fix buffer ref_count accounting in partial clone

build: **Damjan Marion** <damarion@cisco.com>
  | `46122 <https:////gerrit.fd.io/r/c/vpp/+/46122>`_ [VECr 21]: build: fix make install-deps for fedora targets
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 27]: api: add build-time python stub generation via vppapigen

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [VECr 21]: cnat: make session scanner budget configurable

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 28]: crypto: add op tracing capability

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [VECr 0]: bfd: Extract to plugin
  | `46075 <https:////gerrit.fd.io/r/c/vpp/+/46075>`_ [VECr 3]: docs: update tsc vulnerability management process
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 5]: ipfix: move to a plugin
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 20]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VECr 19]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 20]: dpdk: log MFIB MAC replay tolerance at debug level

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `45808 <https:////gerrit.fd.io/r/c/vpp/+/45808>`_ [VECr 0]: devices: Convert PIPE to plugin

fib: **Neale Ranns** <neale@graphiant.com>
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [VECr 0]: bfd: Extract to plugin
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VECr 25]: fib: dump by src not only contributing routes

flow: **Damjan Marion** <damarion@cisco.com>
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VECr 19]: flow: add parameter to pre-allocate global pool
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VECr 20]: flow: add APIs to support new flow actions
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VECr 20]: flow: add flow aging support

flowprobe: **Ole Troan** <otroan@employees.org>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 5]: ipfix: move to a plugin

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `46234 <https:////gerrit.fd.io/r/c/vpp/+/46234>`_ [VECr 3]: quic: crypto context refactoring
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 6]: vperf: drop residual echo/vcl_test terminology
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 19]: tls: propagate verify config for dtls

interface: **Dave Barach** <vpp@barachs.net>
  | `46057 <https:////gerrit.fd.io/r/c/vpp/+/46057>`_ [VECr 27]: interface: do not increase tx error counter on admin/link down interfaces

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 5]: ipfix: move to a plugin

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VECr 25]: fib: dump by src not only contributing routes
  | `46051 <https:////gerrit.fd.io/r/c/vpp/+/46051>`_ [VECr 30]: ip: fix punt socket rx when multiple FDs are ready
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VECr 30]: ip: fix ip mroute bulk insertion CLI for certain inputs

ipfix-export: **Ole Troan** <otroan@employees.org>, **Paul Atkins** <patkins@graphiant.com>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 5]: ipfix: move to a plugin

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 28]: crypto: add op tracing capability

kube-test: **Florin Coras** <fcoras@cisco.com>
  | `46249 <https:////gerrit.fd.io/r/c/vpp/+/46249>`_ [VECr 0]: kube-test: inherit pod MTU for memif test tap
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 6]: vperf: drop residual echo/vcl_test terminology

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `46080 <https:////gerrit.fd.io/r/c/vpp/+/46080>`_ [VECr 21]: l2: fix race condition and null ptr dereference in l2fib_scan
  | `46059 <https:////gerrit.fd.io/r/c/vpp/+/46059>`_ [VECr 21]: l2: fix buffer overflow while finding next node

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [VECr 0]: bfd: Extract to plugin
  | `45808 <https:////gerrit.fd.io/r/c/vpp/+/45808>`_ [VECr 0]: devices: Convert PIPE to plugin
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 5]: ipfix: move to a plugin
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 6]: vperf: drop residual echo/vcl_test terminology
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VECr 13]: tcp: add TCP fast open support (RFC 7413)
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 20]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 27]: api: add build-time python stub generation via vppapigen
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 28]: crypto: add op tracing capability

nat: **Ole Troan** <otroan@employees.org>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 5]: ipfix: move to a plugin

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 5]: ipfix: move to a plugin

pppoe: **Hongjun Ni** <hongjun.ni@intel.com>
  | `46129 <https:////gerrit.fd.io/r/c/vpp/+/46129>`_ [VECr 20]: pppoe: native per-session rx policing in pppoe-decap node
  | `46125 <https:////gerrit.fd.io/r/c/vpp/+/46125>`_ [VECr 20]: pppoe: add combined subscriber session provisioning API

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `46234 <https:////gerrit.fd.io/r/c/vpp/+/46234>`_ [VECr 3]: quic: crypto context refactoring

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `46155 <https:////gerrit.fd.io/r/c/vpp/+/46155>`_ [VECr 6]: rdma: fix verbs port selection
  | `46153 <https:////gerrit.fd.io/r/c/vpp/+/46153>`_ [VECr 11]: rdma: use striding mini-CQEs for mlx5 RQ
  | `46158 <https:////gerrit.fd.io/r/c/vpp/+/46158>`_ [VECr 13]: rdma: keep mlx5 DV completion tails in software
  | `46159 <https:////gerrit.fd.io/r/c/vpp/+/46159>`_ [VECr 14]: rdma: bound mlx5 DV chained WQEs by DS limit
  | `46154 <https:////gerrit.fd.io/r/c/vpp/+/46154>`_ [VECr 14]: rdma: support multiseg legacy RX
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [VECr 20]: rdma: steer PPPoE discovery and session flows

sasc: **Ole Troan** <otroan@employees.org>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `44342 <https:////gerrit.fd.io/r/c/vpp/+/44342>`_ [VECr 3]: sasc: improve tenant addition/deletion through CLI
  | `46121 <https:////gerrit.fd.io/r/c/vpp/+/46121>`_ [VECr 21]: sasc: fix gcc uninitialized warning

session: **Florin Coras** <fcoras@cisco.com>
  | `46234 <https:////gerrit.fd.io/r/c/vpp/+/46234>`_ [VECr 3]: quic: crypto context refactoring

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `46218 <https:////gerrit.fd.io/r/c/vpp/+/46218>`_ [VECr 5]: sfdp: improve generic timeout registration
  | `46219 <https:////gerrit.fd.io/r/c/vpp/+/46219>`_ [VECr 5]: sfdp: bump APIs to v1.0.0
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VECr 12]: sfdp: modify tenant_index type from u16 to u32

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `46218 <https:////gerrit.fd.io/r/c/vpp/+/46218>`_ [VECr 5]: sfdp: improve generic timeout registration
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VECr 12]: sfdp: modify tenant_index type from u16 to u32

sfdp_services_sample: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>
  | `46218 <https:////gerrit.fd.io/r/c/vpp/+/46218>`_ [VECr 5]: sfdp: improve generic timeout registration
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VECr 12]: sfdp: modify tenant_index type from u16 to u32

tcp: **Florin Coras** <fcoras@cisco.com>
  | `46224 <https:////gerrit.fd.io/r/c/vpp/+/46224>`_ [VECr 3]: tcp: mark gso packets during header construction
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VECr 13]: tcp: add TCP fast open support (RFC 7413)

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [VECr 0]: bfd: Extract to plugin
  | `45808 <https:////gerrit.fd.io/r/c/vpp/+/45808>`_ [VECr 0]: devices: Convert PIPE to plugin
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 5]: ipfix: move to a plugin
  | `46218 <https:////gerrit.fd.io/r/c/vpp/+/46218>`_ [VECr 5]: sfdp: improve generic timeout registration
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 6]: vperf: drop residual echo/vcl_test terminology
  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VECr 10]: vlib: add per-thread index pool cache
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 11]: af_xdp: add support for multi-buffer
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VECr 13]: tcp: add TCP fast open support (RFC 7413)
  | `46174 <https:////gerrit.fd.io/r/c/vpp/+/46174>`_ [VECr 14]: tests: enable API preload by default
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 20]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VECr 21]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VECr 21]: vcl: add regression test for ignorable flags
  | `46120 <https:////gerrit.fd.io/r/c/vpp/+/46120>`_ [VECr 21]: tests: make venv cleanup less noisy
  | `46094 <https:////gerrit.fd.io/r/c/vpp/+/46094>`_ [VECr 21]: adl: wait for ADL counters
  | `46087 <https:////gerrit.fd.io/r/c/vpp/+/46087>`_ [VECr 21]: cnat: wait for cnat scanner session cleanup
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VECr 30]: ip: fix ip mroute bulk insertion CLI for certain inputs

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 19]: tls: propagate verify config for dtls

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VECr 10]: vlib: add per-thread index pool cache
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VECr 13]: tcp: add TCP fast open support (RFC 7413)

vcl: **Florin Coras** <fcoras@cisco.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VECr 10]: vlib: add per-thread index pool cache
  | `46065 <https:////gerrit.fd.io/r/c/vpp/+/46065>`_ [VECr 27]: vlib: punt: fix buffer reference after clone

vperf: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `46234 <https:////gerrit.fd.io/r/c/vpp/+/46234>`_ [VECr 3]: quic: crypto context refactoring
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VECr 21]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VECr 21]: vcl: add regression test for ignorable flags

vpp: **Dave Barach** <vpp@barachs.net>
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [VECr 0]: bfd: Extract to plugin
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 20]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

vppapigen: **Ole Troan** <otroan@employees.org>
  | `46117 <https:////gerrit.fd.io/r/c/vpp/+/46117>`_ [VECr 21]: vppapigen: fix vppapigen depfile without imports
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 27]: api: add build-time python stub generation via vppapigen

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `46066 <https:////gerrit.fd.io/r/c/vpp/+/46066>`_ [VECr 27]: vppinfra: fifo: do not resize vector down to 0

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [VEc 28]: ip_validate: new plugin to drop packets with invalid addresses

**Akos Orban** <orbanakos2001@gmail.com>:

  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 35]: cnat: fix show cnat client showing invalid for client id
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 35]: cnat: fix show cnat translation for specific translation id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 104]: vhost: fix rxvq interrupts triggered because of race

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VeC 52]: snort: don't store snort metadata in buffer

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 173]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `46256 <https:////gerrit.fd.io/r/c/vpp/+/46256>`_ [vEC 0]: crypto: openssl - check ctx alloc/init in key-add
  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VeC 75]: map: enhance map plugin to support per-vrf rules

**Aritra Basu** <aritrbas@cisco.com>:

  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [VEc 6]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `46167 <https:////gerrit.fd.io/r/c/vpp/+/46167>`_ [vEC 17]: kube-test: retry Job finalizer cleanup conflicts
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VeC 31]: interface: enable IPv6 link state on unnumbered interfaces
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VeC 31]: vlib: fix trace flag loss when multiple pending frames share next frame
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 115]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 117]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 117]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 117]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 117]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 122]: ip6-nd: fix unicast NA handling in ND proxy

**Benoît Ganne** <bganne@cisco.com>:

  | `46182 <https:////gerrit.fd.io/r/c/vpp/+/46182>`_ [VEc 3]: buffers: fix pool allocation on small pages

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [veC 37]: ikev2: add Curve25519 and Curve448 DH groups

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 119]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 119]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [Vec 68]: dpdk: tracing improvements

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [vEC 19]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [vEC 19]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [VEc 20]: sfdp: add verdict-testbench service
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VeC 32]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VeC 32]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [Vec 35]: tracepath: minor refactoring to code
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VeC 53]: sfdp: add sfdp-session-stats service
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VeC 56]: sfdp: fix specification of scope_index

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `46147 <https:////gerrit.fd.io/r/c/vpp/+/46147>`_ [VEc 17]: npol: support prednat policies
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [VEc 21]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 109]: tests: reduce sleep interval in ip-neighbor age test
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 138]: crypto: unify per-thread key_data allocation

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 157]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 157]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 157]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 157]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VEc 4]: rdma: add mlx5 DV TSO support for raw packet tx
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VEc 14]: iavf: fix native TSO datapath
  | `45775 <https:////gerrit.fd.io/r/c/vpp/+/45775>`_ [VeC 62]: tcp: fix pure ACK incorrectly chained as GRO candidate
  | `45759 <https:////gerrit.fd.io/r/c/vpp/+/45759>`_ [VeC 62]: tcp: support chained buffers in GRO
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VeC 62]: tcp: allow selective GRO enablement
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 76]: virtio: add native plugin L2 xconnect test with QEMU

**Jiajun Liang** <3138947285@qq.com>:

  | `45677 <https:////gerrit.fd.io/r/c/vpp/+/45677>`_ [VEc 3]: linux-cp: guard PPPOX interface type and tolerate missing neighbor

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [Vec 33]: ip bonding hash: inner-aware flow hash (opt-in)

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 159]: vppapigen: fix json build error

**Justin Thomas** <justin@jdt.io>:

  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VeC 101]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VeC 101]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

**Klement Sekera** <ksekera@netgate.com>:

  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VeC 31]: build: include GNUInstallDirs in VPPConfig
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VeC 59]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VeC 82]: vppinfra: add cast to prevent warning

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [Vec 32]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [Vec 32]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Matus Fabian** <matfabia@cisco.com>:

  | `46079 <https:////gerrit.fd.io/r/c/vpp/+/46079>`_ [vEC 17]: hs-test: temporarily disable core file removal

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VEc 5]: flow: add flow template and async range infrastructure
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [vEc 10]: dpdk: support async flow offload
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [veC 33]: docs: document build-time VPP parameters
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VeC 39]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [vec 39]: flow: add per-thread flow pool cache for multi-worker safety
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [veC 39]: dpdk: multi-thread async flow offload with per-worker caches
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VeC 112]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VeC 112]: gso: implement IPv6 extension header traversal
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 118]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 118]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 118]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 118]: policer: reject deletion of policer used by punt policing

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [veC 52]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VeC 97]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 117]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 123]: sfdp: add blacklist/whitelist to snort service
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 146]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 150]: pg: Guard against non‑monotonic time and negative accumulator

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 163]: iouring: Add io_uring plugin to allow polling usage of io_uring

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 96]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 96]: ip6-nd: add nd-proxy all dst
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 104]: ip6: fix show ip6-ll cli if selector
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 145]: ip6-nd: support RA pfx info option with flag L&!A

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vec 39]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [Vec 89]: papi: improve performance on set_errors

**Onong Tayeng** <onong.tayeng@gmail.com>:

  | `46217 <https:////gerrit.fd.io/r/c/vpp/+/46217>`_ [vEC 4]: npol: export flow decision counters

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 164]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 166]: fix: correct fixstyle in session_sdl command function

**Pim van Pelt** <pim@ipng.nl>:

  | `46038 <https:////gerrit.fd.io/r/c/vpp/+/46038>`_ [VEc 26]: ip6-nd: fix crash in link-local target NS
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VeC 96]: lb: Add punt feature to per-port VIPs

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [Vec 47]: pfc: add framework for priority flow control
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VeC 59]: octeon: add PFC support

**Robert Shearman** <robertshearman@gmail.com>:

  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VeC 32]: vlib: ASAN-poison unallocated buffers
  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [Vec 34]: misc: fix potential OOB read during flow hash calculations
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VeC 40]: ip: fix adjacent packet overwrite with ip frags
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [VeC 40]: ip: fix adjacent packet overwrite with ip6 frags
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VeC 73]: vppapigen: fix inconsistency in paths JSON

**Shuzo Ichiyoshi** <deadcafe.beef@gmail.com>:

  | `46179 <https:////gerrit.fd.io/r/c/vpp/+/46179>`_ [vEC 5]: tcp: mark half-open done before deferred cleanup
  | `46176 <https:////gerrit.fd.io/r/c/vpp/+/46176>`_ [vEC 11]: session: cache process-wide CPU time for workers
  | `46178 <https:////gerrit.fd.io/r/c/vpp/+/46178>`_ [vEC 13]: session: validate app for async connect RPC
  | `46180 <https:////gerrit.fd.io/r/c/vpp/+/46180>`_ [vEC 14]: session: check event collector lookups

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [vEC 25]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [vEC 25]: linux-cp: fix cleanup of special routes

**Viacheslav Zakharchenko** <vzakharc@cisco.com>:

  | `45807 <https:////gerrit.fd.io/r/c/vpp/+/45807>`_ [VEc 3]: bfd: Introduce vppinfra/callback_data based vnet notifier for FIB/ADJ notifications

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [Vec 56]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [veC 104]: vppinfra: collect heap stats in constant time

**Vratko Polak** <vrpolak@cisco.com>:

  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vec 45]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [veC 89]: empty change for GHA(CSIT) testing

**Wei Wang** <weiwa@cisco.com>:

  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [VEc 18]: tls: tls session resumption code and host stack tests

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VeC 47]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer
  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [Vec 47]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [veC 48]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VeC 48]: vlib: fix process state format output wrapped by extra quotes
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vec 54]: vlib: pre-input node should be dispatched before input node

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [VEc 10]: vppinfra: add loongarch64 architecture support

**Yuto Suzuki** <offside.items03@icloud.com>:

  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VEc 24]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VEc 24]: ip6-nd: support RDNSS option in IPv6 RA

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 153]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [veC 63]: vlib: fix '\' command input will causes memory out of bounds
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [Vec 104]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [Vec 104]: dns: support ipv6 server to resolve name
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VeC 105]: build rpm-packaging: make vpp rpm package for kylinV11
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 158]: docs: Python apis examples

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 77]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [vEC 25]: cnat: add scope_id to session key

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 116]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 104]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [veC 104]: lb: fix API byte order and IPv4 prefix length handling

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VeC 73]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VeC 60]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VeC 62]: tls: fix picotls partial record handling
  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [Vec 63]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [Vec 69]: session: make transport to use application's segment manager

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 168]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 168]: l2: fix null pointer access in l2-efp-filter

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
authors          131
maintainers      53
committers       1
abandoned        0
================ ===

