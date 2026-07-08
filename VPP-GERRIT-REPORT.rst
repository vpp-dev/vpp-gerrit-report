
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Wednesday 2026-07-08, 04:29:14
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

  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VECR 29]: cnat: fix show cnat client showing invalid for client id
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VECR 29]: cnat: fix show cnat translation for specific translation id

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 5]: af_xdp: add support for multi-buffer

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `46182 <https:////gerrit.fd.io/r/c/vpp/+/46182>`_ [VECr 0]: buffers: fix pool allocation on small pages
  | `45684 <https:////gerrit.fd.io/r/c/vpp/+/45684>`_ [VECr 9]: buffers: return values; improve debug
  | `46062 <https:////gerrit.fd.io/r/c/vpp/+/46062>`_ [VECr 15]: vlib: fix buffer ref_count accounting in partial clone
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VECr 26]: vlib: ASAN-poison unallocated buffers

build: **Damjan Marion** <damarion@cisco.com>
  | `46122 <https:////gerrit.fd.io/r/c/vpp/+/46122>`_ [VECr 15]: build: fix make install-deps for fedora targets
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 21]: api: add build-time python stub generation via vppapigen
  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VECr 25]: build: include GNUInstallDirs in VPPConfig

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [VECr 15]: cnat: make session scanner budget configurable

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 22]: crypto: add op tracing capability

dev: **Damjan Marion** <damarion@cisco.com>
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 26]: flow: implement VNET_FLOW_ACTION_COUNT operation

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45674 <https:////gerrit.fd.io/r/c/vpp/+/45674>`_ [VECr 14]: dhcp: export DHCPv6 runtime state for PPPoE observability

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 1]: rdma: add mlx5 DV TSO support for raw packet tx
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 2]: ipfix-export: move to a plugin
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 14]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `46140 <https:////gerrit.fd.io/r/c/vpp/+/46140>`_ [VECr 8]: dpdk: set int_unmaskable for ice driver
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VECr 13]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 14]: dpdk: log MFIB MAC replay tolerance at debug level
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VECr 26]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 26]: flow: implement VNET_FLOW_ACTION_COUNT operation

fib: **Neale Ranns** <neale@graphiant.com>
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VECr 19]: fib: dump by src not only contributing routes

flow: **Damjan Marion** <damarion@cisco.com>
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VECr 13]: flow: add parameter to pre-allocate global pool
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VECr 14]: flow: add APIs to support new flow actions
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VECr 14]: flow: add flow aging support
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 26]: flow: implement VNET_FLOW_ACTION_COUNT operation

flowprobe: **Ole Troan** <otroan@employees.org>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 2]: ipfix-export: move to a plugin

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 0]: vperf: drop residual echo/vcl_test terminology
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 13]: tls: propagate verify config for dtls

interface: **Dave Barach** <vpp@barachs.net>
  | `46057 <https:////gerrit.fd.io/r/c/vpp/+/46057>`_ [VECr 21]: interface: do not increase tx error counter on admin/link down interfaces
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VECr 25]: interface: enable IPv6 link state on unnumbered interfaces
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 26]: flow: implement VNET_FLOW_ACTION_COUNT operation

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 2]: ipfix-export: move to a plugin

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VECr 19]: fib: dump by src not only contributing routes
  | `46051 <https:////gerrit.fd.io/r/c/vpp/+/46051>`_ [VECr 24]: ip: fix punt socket rx when multiple FDs are ready
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VECr 24]: ip: fix ip mroute bulk insertion CLI for certain inputs

ipfix-export: **Ole Troan** <otroan@employees.org>, **Paul Atkins** <patkins@graphiant.com>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 2]: ipfix-export: move to a plugin

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 22]: crypto: add op tracing capability

kube-test: **Florin Coras** <fcoras@cisco.com>
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 0]: vperf: drop residual echo/vcl_test terminology

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `46080 <https:////gerrit.fd.io/r/c/vpp/+/46080>`_ [VECr 15]: l2: fix race condition and null ptr dereference in l2fib_scan
  | `46059 <https:////gerrit.fd.io/r/c/vpp/+/46059>`_ [VECr 15]: l2: fix buffer overflow while finding next node

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `45677 <https:////gerrit.fd.io/r/c/vpp/+/45677>`_ [VECr 14]: linux-cp: guard PPPOX interface type and tolerate missing neighbor

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 0]: vperf: drop residual echo/vcl_test terminology
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 2]: ipfix-export: move to a plugin
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VECr 7]: tcp: add TCP fast open support (RFC 7413)
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 14]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 21]: api: add build-time python stub generation via vppapigen
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 22]: crypto: add op tracing capability

nat: **Ole Troan** <otroan@employees.org>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 2]: ipfix-export: move to a plugin

pppoe: **Hongjun Ni** <hongjun.ni@intel.com>
  | `46129 <https:////gerrit.fd.io/r/c/vpp/+/46129>`_ [VECr 14]: pppoe: native per-session rx policing in pppoe-decap node
  | `46125 <https:////gerrit.fd.io/r/c/vpp/+/46125>`_ [VECr 14]: pppoe: add combined subscriber session provisioning API

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `46155 <https:////gerrit.fd.io/r/c/vpp/+/46155>`_ [VECr 0]: rdma: fix verbs port selection
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 1]: rdma: add mlx5 DV TSO support for raw packet tx
  | `46153 <https:////gerrit.fd.io/r/c/vpp/+/46153>`_ [VECr 5]: rdma: use striding mini-CQEs for mlx5 RQ
  | `46158 <https:////gerrit.fd.io/r/c/vpp/+/46158>`_ [VECr 7]: rdma: keep mlx5 DV completion tails in software
  | `46159 <https:////gerrit.fd.io/r/c/vpp/+/46159>`_ [VECr 8]: rdma: bound mlx5 DV chained WQEs by DS limit
  | `46154 <https:////gerrit.fd.io/r/c/vpp/+/46154>`_ [VECr 8]: rdma: support multiseg legacy RX
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [VECr 14]: rdma: steer PPPoE discovery and session flows

sasc: **Ole Troan** <otroan@employees.org>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `46121 <https:////gerrit.fd.io/r/c/vpp/+/46121>`_ [VECr 15]: sasc: fix gcc uninitialized warning

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VECr 6]: sfdp: modify tenant_index type from u16 to u32

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VECr 6]: sfdp: modify tenant_index type from u16 to u32

sfdp_services_sample: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VECr 6]: sfdp: modify tenant_index type from u16 to u32

tcp: **Florin Coras** <fcoras@cisco.com>
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VECr 7]: tcp: add TCP fast open support (RFC 7413)

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 0]: vperf: drop residual echo/vcl_test terminology
  | `46182 <https:////gerrit.fd.io/r/c/vpp/+/46182>`_ [VECr 0]: buffers: fix pool allocation on small pages
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 2]: ipfix-export: move to a plugin
  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VECr 4]: vlib: add per-thread index pool cache
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 5]: af_xdp: add support for multi-buffer
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VECr 7]: tcp: add TCP fast open support (RFC 7413)
  | `46174 <https:////gerrit.fd.io/r/c/vpp/+/46174>`_ [VECr 8]: tests: enable API preload by default
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 14]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VECr 15]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VECr 15]: vcl: add regression test for ignorable flags
  | `46120 <https:////gerrit.fd.io/r/c/vpp/+/46120>`_ [VECr 15]: tests: make venv cleanup less noisy
  | `46094 <https:////gerrit.fd.io/r/c/vpp/+/46094>`_ [VECr 15]: adl: wait for ADL counters
  | `46087 <https:////gerrit.fd.io/r/c/vpp/+/46087>`_ [VECr 15]: cnat: wait for cnat scanner session cleanup
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VECr 24]: ip: fix ip mroute bulk insertion CLI for certain inputs
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VECr 26]: vlib: ASAN-poison unallocated buffers

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 13]: tls: propagate verify config for dtls

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VECr 4]: vlib: add per-thread index pool cache
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VECr 7]: tcp: add TCP fast open support (RFC 7413)

vcl: **Florin Coras** <fcoras@cisco.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VECr 4]: vlib: add per-thread index pool cache
  | `46161 <https:////gerrit.fd.io/r/c/vpp/+/46161>`_ [VECr 11]: vlib: fix timed event data parameter
  | `46065 <https:////gerrit.fd.io/r/c/vpp/+/46065>`_ [VECr 21]: vlib: punt: fix buffer reference after clone
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VECr 25]: vlib: fix trace flag loss when multiple pending frames share next frame

vperf: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VECr 15]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VECr 15]: vcl: add regression test for ignorable flags

vpp: **Dave Barach** <vpp@barachs.net>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 14]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

vppapigen: **Ole Troan** <otroan@employees.org>
  | `46117 <https:////gerrit.fd.io/r/c/vpp/+/46117>`_ [VECr 15]: vppapigen: fix vppapigen depfile without imports
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 21]: api: add build-time python stub generation via vppapigen

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `46066 <https:////gerrit.fd.io/r/c/vpp/+/46066>`_ [VECr 21]: vppinfra: fifo: do not resize vector down to 0

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [VEc 22]: ip_validate: new plugin to drop packets with invalid addresses

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 98]: vhost: fix rxvq interrupts triggered because of race

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VeC 46]: snort: don't store snort metadata in buffer

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 167]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VeC 69]: map: enhance map plugin to support per-vrf rules

**Aritra Basu** <aritrbas@cisco.com>:

  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [VEc 0]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `46167 <https:////gerrit.fd.io/r/c/vpp/+/46167>`_ [vEC 11]: kube-test: retry Job finalizer cleanup conflicts
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 109]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 111]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 111]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 111]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 111]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 117]: ip6-nd: fix unicast NA handling in ND proxy

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [veC 31]: ikev2: add Curve25519 and Curve448 DH groups

**Dave Wallace** <dwallacelf@gmail.com>:

  | `46075 <https:////gerrit.fd.io/r/c/vpp/+/46075>`_ [vEc 4]: docs: update tsc vulnerability management process

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 113]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 113]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [Vec 62]: dpdk: tracing improvements

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `46218 <https:////gerrit.fd.io/r/c/vpp/+/46218>`_ [vEc 0]: sfdp: improve generic timeout registration
  | `46219 <https:////gerrit.fd.io/r/c/vpp/+/46219>`_ [vEC 0]: sfdp: bump APIs to v1.0.0
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [vEC 13]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [vEC 13]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [VEc 14]: sfdp: add verdict-testbench service
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [VEc 29]: tracepath: minor refactoring to code
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VeC 47]: sfdp: add sfdp-session-stats service
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VeC 50]: sfdp: fix specification of scope_index

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `46147 <https:////gerrit.fd.io/r/c/vpp/+/46147>`_ [VEc 11]: npol: support prednat policies
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [VEc 15]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 103]: tests: reduce sleep interval in ip-neighbor age test
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 132]: crypto: unify per-thread key_data allocation

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 151]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 151]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 151]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 151]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `46222 <https:////gerrit.fd.io/r/c/vpp/+/46222>`_ [vEC 0]: tcp: guard gso payload length calculation
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VEc 8]: iavf: fix native TSO datapath
  | `45775 <https:////gerrit.fd.io/r/c/vpp/+/45775>`_ [VeC 56]: tcp: fix pure ACK incorrectly chained as GRO candidate
  | `45759 <https:////gerrit.fd.io/r/c/vpp/+/45759>`_ [VeC 56]: tcp: support chained buffers in GRO
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VeC 56]: tcp: allow selective GRO enablement
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 70]: virtio: add native plugin L2 xconnect test with QEMU

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VEc 27]: ip bonding hash: inner-aware flow hash (opt-in)

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 153]: vppapigen: fix json build error

**Justin Thomas** <justin@jdt.io>:

  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VeC 95]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VeC 95]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

**Klement Sekera** <ksekera@netgate.com>:

  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VeC 53]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VeC 76]: vppinfra: add cast to prevent warning

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [VEc 26]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [VEc 26]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Matus Fabian** <matfabia@cisco.com>:

  | `46079 <https:////gerrit.fd.io/r/c/vpp/+/46079>`_ [vEC 11]: hs-test: temporarily disable core file removal

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [vEc 4]: dpdk: support async flow offload
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VEc 12]: flow: add flow template and async range infrastructure
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [vEC 27]: docs: document build-time VPP parameters
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VeC 33]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [vec 33]: flow: add per-thread flow pool cache for multi-worker safety
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [veC 33]: dpdk: multi-thread async flow offload with per-worker caches
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VeC 106]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VeC 106]: gso: implement IPv6 extension header traversal
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 112]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 112]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 112]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 112]: policer: reject deletion of policer used by punt policing

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [veC 46]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VeC 91]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 111]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 117]: sfdp: add blacklist/whitelist to snort service
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 140]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 144]: pg: Guard against non‑monotonic time and negative accumulator
  | `44426 <https:////gerrit.fd.io/r/c/vpp/+/44426>`_ [VeC 179]: virtio: add the check if MAC feature is negotiated

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 157]: iouring: Add io_uring plugin to allow polling usage of io_uring

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 90]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 90]: ip6-nd: add nd-proxy all dst
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 98]: ip6: fix show ip6-ll cli if selector
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 139]: ip6-nd: support RA pfx info option with flag L&!A

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vec 33]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [Vec 83]: papi: improve performance on set_errors

**Onong Tayeng** <onong.tayeng@gmail.com>:

  | `46217 <https:////gerrit.fd.io/r/c/vpp/+/46217>`_ [vEC 0]: npol: export flow decision counters

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 158]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 160]: fix: correct fixstyle in session_sdl command function

**Pim van Pelt** <pim@ipng.nl>:

  | `46038 <https:////gerrit.fd.io/r/c/vpp/+/46038>`_ [VEc 20]: ip6-nd: fix crash in link-local target NS
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VeC 90]: lb: Add punt feature to per-port VIPs

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [Vec 41]: pfc: add framework for priority flow control
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VeC 53]: octeon: add PFC support

**Robert Shearman** <robertshearman@gmail.com>:

  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [VEc 28]: misc: fix potential OOB read during flow hash calculations
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VeC 34]: ip: fix adjacent packet overwrite with ip frags
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [VeC 34]: ip: fix adjacent packet overwrite with ip6 frags
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VeC 67]: vppapigen: fix inconsistency in paths JSON

**Samuel Benko** <sbenko@cisco.com>:

  | `46188 <https:////gerrit.fd.io/r/c/vpp/+/46188>`_ [vEC 5]: gha: enable MW parallel HST jobs

**Shuzo Ichiyoshi** <deadcafe.beef@gmail.com>:

  | `46176 <https:////gerrit.fd.io/r/c/vpp/+/46176>`_ [vEC 5]: session: cache process-wide CPU time for workers
  | `46179 <https:////gerrit.fd.io/r/c/vpp/+/46179>`_ [vEC 7]: tcp: mark half-open done before deferred cleanup
  | `46178 <https:////gerrit.fd.io/r/c/vpp/+/46178>`_ [vEC 7]: session: validate app for async connect RPC
  | `46180 <https:////gerrit.fd.io/r/c/vpp/+/46180>`_ [vEC 8]: session: check event collector lookups

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [vEC 19]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [vEC 19]: linux-cp: fix cleanup of special routes

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [Vec 50]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [veC 98]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44575 <https:////gerrit.fd.io/r/c/vpp/+/44575>`_ [VeC 179]: fib: add interface-rx dpo mpls support
  | `44574 <https:////gerrit.fd.io/r/c/vpp/+/44574>`_ [VeC 179]: fib: fix stale interface-rx dpo fib after deag/lookup
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 179]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 179]: nat: speedup nat44-ed vrf table lookups
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 179]: nat: fix nat44-ed address removal from fib

**Vratko Polak** <vrpolak@cisco.com>:

  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vec 39]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [veC 83]: empty change for GHA(CSIT) testing

**Wayne Morrison** <wmorrison@netgate.com>:

  | `45949 <https:////gerrit.fd.io/r/c/vpp/+/45949>`_ [VEc 13]: lldp: extend data returned by lldp-dump API

**Wei Wang** <weiwa@cisco.com>:

  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [VEc 12]: tls: tls session resumption code and host stack tests

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VeC 41]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer
  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [Vec 41]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [veC 42]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VeC 42]: vlib: fix process state format output wrapped by extra quotes
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vec 48]: vlib: pre-input node should be dispatched before input node

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [VEc 4]: vppinfra: add loongarch64 architecture support

**Yuto Suzuki** <offside.items03@icloud.com>:

  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VEc 18]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VEc 18]: ip6-nd: support RDNSS option in IPv6 RA

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 147]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [veC 57]: vlib: fix '\' command input will causes memory out of bounds
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [Vec 98]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [Vec 98]: dns: support ipv6 server to resolve name
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VeC 99]: build rpm-packaging: make vpp rpm package for kylinV11
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 152]: docs: Python apis examples

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 71]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [vEC 19]: cnat: add scope_id to session key

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 110]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 98]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [veC 98]: lb: fix API byte order and IPv4 prefix length handling

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VeC 67]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VeC 54]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VeC 56]: tls: fix picotls partial record handling
  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [Vec 57]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [Vec 63]: session: make transport to use application's segment manager

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 162]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 162]: l2: fix null pointer access in l2-efp-filter

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44563 <https:////gerrit.fd.io/r/c/vpp/+/44563>`_ [A 180]: ip: fix DSCP CS7 value
  | `44568 <https:////gerrit.fd.io/r/c/vpp/+/44568>`_ [A 180]: vxlan: add default dscp value config for vxlan encap
  | `44567 <https:////gerrit.fd.io/r/c/vpp/+/44567>`_ [A 180]: udp: add default dscp value config for udp encap
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [A 180]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [A 180]: fib: fix udp encap mp-safe ops and id validation
  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [A 180]: fib: avoid loadbalance dpo node path polarisation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [A 180]: vlib: mark cli quit command as mp_safe

**steven luong** <sluong@cisco.com>:

  | `44569 <https:////gerrit.fd.io/r/c/vpp/+/44569>`_ [A 180]: vppinfra: clib_time_verify_frequency may cause time jump

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
authors          130
maintainers      56
committers       2
abandoned        8
================ ===

