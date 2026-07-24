
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Friday 2026-07-24, 04:28:32
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

  | `46286 <https:////gerrit.fd.io/r/c/vpp/+/46286>`_ [VECR 0]: hs-test: switch vcl and echo suites to tap

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

abf: **Neale Ranns** <neale@graphiant.com>
  | `46339 <https:////gerrit.fd.io/r/c/vpp/+/46339>`_ [VECr 0]: abf: reject attachment to a non-existent policy instead of asserting

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `46270 <https:////gerrit.fd.io/r/c/vpp/+/46270>`_ [VECr 8]: acl: correct interface command help

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `46182 <https:////gerrit.fd.io/r/c/vpp/+/46182>`_ [VECr 0]: buffers: fix pool allocation on small pages

build: **Damjan Marion** <damarion@cisco.com>
  | `46182 <https:////gerrit.fd.io/r/c/vpp/+/46182>`_ [VECr 0]: buffers: fix pool allocation on small pages
  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VECr 9]: build: include GNUInstallDirs in VPPConfig
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 9]: api: add build-time python stub generation via vppapigen

dev: **Damjan Marion** <damarion@cisco.com>
  | `46282 <https:////gerrit.fd.io/r/c/vpp/+/46282>`_ [VECr 6]: dev: advertise TX UDP GSO

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra
  | `46308 <https:////gerrit.fd.io/r/c/vpp/+/46308>`_ [VECr 0]: docs: only list release notes for supported versions
  | `46182 <https:////gerrit.fd.io/r/c/vpp/+/46182>`_ [VECr 0]: buffers: fix pool allocation on small pages
  | `45819 <https:////gerrit.fd.io/r/c/vpp/+/45819>`_ [VECr 8]: tcp: add TCP input GRO before input lookup
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VECr 9]: iavf: add setup documentation
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 15]: ipfix: move to a plugin
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 30]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `46340 <https:////gerrit.fd.io/r/c/vpp/+/46340>`_ [VECr 0]: dpdk: namespace interface xstats
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VECr 29]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 30]: dpdk: log MFIB MAC replay tolerance at debug level

fib: **Neale Ranns** <neale@graphiant.com>
  | `46338 <https:////gerrit.fd.io/r/c/vpp/+/46338>`_ [VECr 0]: fib: tolerate a NULL rewrite in vnet_rewrite_for_sw_interface

flow: **Damjan Marion** <damarion@cisco.com>
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 0]: flow: add flow template and async range infrastructure
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VECr 29]: flow: add parameter to pre-allocate global pool
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VECr 30]: flow: add APIs to support new flow actions
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VECr 30]: flow: add flow aging support

flowprobe: **Ole Troan** <otroan@employees.org>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 15]: ipfix: move to a plugin

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `46313 <https:////gerrit.fd.io/r/c/vpp/+/46313>`_ [VECr 0]: udp: use dense destination port tables
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 16]: vperf: drop residual echo/vcl_test terminology
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 29]: tls: propagate verify config for dtls

iavf: **Damjan Marion** <damarion@cisco.com>
  | `46271 <https:////gerrit.fd.io/r/c/vpp/+/46271>`_ [VECr 6]: iavf: fix iavf_tx_fill_ctx_desc ph buf seg fault
  | `46283 <https:////gerrit.fd.io/r/c/vpp/+/46283>`_ [VECr 6]: iavf: add UDP segmentation offload support
  | `46261 <https:////gerrit.fd.io/r/c/vpp/+/46261>`_ [VECr 6]: iavf: fix rx queue max_pkt_size value set on init
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VECr 9]: iavf: add setup documentation

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `45811 <https:////gerrit.fd.io/r/c/vpp/+/45811>`_ [VECr 3]: ipip: move to a plugin

interface: **Dave Barach** <vpp@barachs.net>
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 0]: flow: add flow template and async range infrastructure

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 15]: ipfix: move to a plugin

ipfix-export: **Ole Troan** <otroan@employees.org>, **Paul Atkins** <patkins@graphiant.com>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 15]: ipfix: move to a plugin

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45811 <https:////gerrit.fd.io/r/c/vpp/+/45811>`_ [VECr 3]: ipip: move to a plugin

kube-test: **Florin Coras** <fcoras@cisco.com>
  | `46249 <https:////gerrit.fd.io/r/c/vpp/+/46249>`_ [VECr 10]: kube-test: inherit pod MTU for memif test tap
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 16]: vperf: drop residual echo/vcl_test terminology

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `46298 <https:////gerrit.fd.io/r/c/vpp/+/46298>`_ [VECr 1]: vperf: validate udp datagrams before echo
  | `45811 <https:////gerrit.fd.io/r/c/vpp/+/45811>`_ [VECr 3]: ipip: move to a plugin
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 9]: api: add build-time python stub generation via vppapigen
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 15]: ipfix: move to a plugin
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 16]: vperf: drop residual echo/vcl_test terminology
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VECr 23]: tcp: add TCP fast open support (RFC 7413)
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 30]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

nat: **Ole Troan** <otroan@employees.org>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 15]: ipfix: move to a plugin

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 15]: ipfix: move to a plugin

pppoe: **Hongjun Ni** <hongjun.ni@intel.com>
  | `46129 <https:////gerrit.fd.io/r/c/vpp/+/46129>`_ [VECr 30]: pppoe: native per-session rx policing in pppoe-decap node
  | `46125 <https:////gerrit.fd.io/r/c/vpp/+/46125>`_ [VECr 30]: pppoe: add combined subscriber session provisioning API

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `46315 <https:////gerrit.fd.io/r/c/vpp/+/46315>`_ [VECr 0]: quic: quic_quicly add uso support

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `46155 <https:////gerrit.fd.io/r/c/vpp/+/46155>`_ [VECr 16]: rdma: fix verbs port selection
  | `46153 <https:////gerrit.fd.io/r/c/vpp/+/46153>`_ [VECr 21]: rdma: use striding mini-CQEs for mlx5 RQ
  | `46158 <https:////gerrit.fd.io/r/c/vpp/+/46158>`_ [VECr 23]: rdma: keep mlx5 DV completion tails in software
  | `46159 <https:////gerrit.fd.io/r/c/vpp/+/46159>`_ [VECr 24]: rdma: bound mlx5 DV chained WQEs by DS limit
  | `46154 <https:////gerrit.fd.io/r/c/vpp/+/46154>`_ [VECr 24]: rdma: support multiseg legacy RX
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [VECr 30]: rdma: steer PPPoE discovery and session flows

sasc: **Ole Troan** <otroan@employees.org>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `44342 <https:////gerrit.fd.io/r/c/vpp/+/44342>`_ [VECr 13]: sasc: improve tenant addition/deletion through CLI

session: **Florin Coras** <fcoras@cisco.com>
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 1]: udp: add segmentation offload support
  | `46309 <https:////gerrit.fd.io/r/c/vpp/+/46309>`_ [VECr 1]: session: wake queue process on state changes

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VECr 22]: sfdp: modify tenant_index type from u16 to u32

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VECr 22]: sfdp: modify tenant_index type from u16 to u32

sfdp_services_sample: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VECr 22]: sfdp: modify tenant_index type from u16 to u32

tcp: **Florin Coras** <fcoras@cisco.com>
  | `46311 <https:////gerrit.fd.io/r/c/vpp/+/46311>`_ [VECr 1]: tcp: handle retransmitted SYN-ACK in TIME-WAIT
  | `45819 <https:////gerrit.fd.io/r/c/vpp/+/45819>`_ [VECr 8]: tcp: add TCP input GRO before input lookup
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VECr 23]: tcp: add TCP fast open support (RFC 7413)

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46339 <https:////gerrit.fd.io/r/c/vpp/+/46339>`_ [VECr 0]: abf: reject attachment to a non-existent policy instead of asserting
  | `46338 <https:////gerrit.fd.io/r/c/vpp/+/46338>`_ [VECr 0]: fib: tolerate a NULL rewrite in vnet_rewrite_for_sw_interface
  | `46182 <https:////gerrit.fd.io/r/c/vpp/+/46182>`_ [VECr 0]: buffers: fix pool allocation on small pages
  | `46309 <https:////gerrit.fd.io/r/c/vpp/+/46309>`_ [VECr 1]: session: wake queue process on state changes
  | `45811 <https:////gerrit.fd.io/r/c/vpp/+/45811>`_ [VECr 3]: ipip: move to a plugin
  | `46120 <https:////gerrit.fd.io/r/c/vpp/+/46120>`_ [VECr 7]: tests: make venv cleanup less noisy
  | `46268 <https:////gerrit.fd.io/r/c/vpp/+/46268>`_ [VECr 7]: vlib: expose error severity in stats segment
  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VECr 15]: ipfix: move to a plugin
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 16]: vperf: drop residual echo/vcl_test terminology
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VECr 23]: tcp: add TCP fast open support (RFC 7413)
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 30]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 29]: tls: propagate verify config for dtls

udp: **Florin Coras** <fcoras@cisco.com>
  | `46313 <https:////gerrit.fd.io/r/c/vpp/+/46313>`_ [VECr 0]: udp: use dense destination port tables
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 1]: udp: add segmentation offload support

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `46313 <https:////gerrit.fd.io/r/c/vpp/+/46313>`_ [VECr 0]: udp: use dense destination port tables
  | `46311 <https:////gerrit.fd.io/r/c/vpp/+/46311>`_ [VECr 1]: tcp: handle retransmitted SYN-ACK in TIME-WAIT
  | `46305 <https:////gerrit.fd.io/r/c/vpp/+/46305>`_ [VECr 1]: vppinfra: make sparse vector lookup zero-safe
  | `46309 <https:////gerrit.fd.io/r/c/vpp/+/46309>`_ [VECr 1]: session: wake queue process on state changes
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VECr 23]: tcp: add TCP fast open support (RFC 7413)

vcl: **Florin Coras** <fcoras@cisco.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46182 <https:////gerrit.fd.io/r/c/vpp/+/46182>`_ [VECr 0]: buffers: fix pool allocation on small pages
  | `46268 <https:////gerrit.fd.io/r/c/vpp/+/46268>`_ [VECr 7]: vlib: expose error severity in stats segment

vpp: **Dave Barach** <vpp@barachs.net>
  | `46182 <https:////gerrit.fd.io/r/c/vpp/+/46182>`_ [VECr 0]: buffers: fix pool allocation on small pages
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 30]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

vppapigen: **Ole Troan** <otroan@employees.org>
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 9]: api: add build-time python stub generation via vppapigen

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `46305 <https:////gerrit.fd.io/r/c/vpp/+/46305>`_ [VECr 1]: vppinfra: make sparse vector lookup zero-safe

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [Vec 38]: ip_validate: new plugin to drop packets with invalid addresses

**Akos Orban** <orbanakos2001@gmail.com>:

  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 45]: cnat: fix show cnat client showing invalid for client id
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 45]: cnat: fix show cnat translation for specific translation id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 114]: vhost: fix rxvq interrupts triggered because of race

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VeC 62]: snort: don't store snort metadata in buffer

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `46256 <https:////gerrit.fd.io/r/c/vpp/+/46256>`_ [vEc 7]: crypto: openssl - check ctx alloc/init in key-add
  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VeC 85]: map: enhance map plugin to support per-vrf rules

**Anton Blazhko** <ablazhko@cisco.com>:

  | `45808 <https:////gerrit.fd.io/r/c/vpp/+/45808>`_ [VEc 8]: devices: Convert PIPE to plugin

**Aritra Basu** <aritrbas@cisco.com>:

  | `46265 <https:////gerrit.fd.io/r/c/vpp/+/46265>`_ [vEC 9]: vcl: add vls_unregister_vcl_worker for explicit worker teardown
  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [VEc 16]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `46167 <https:////gerrit.fd.io/r/c/vpp/+/46167>`_ [vEC 27]: kube-test: retry Job finalizer cleanup conflicts
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VeC 41]: interface: enable IPv6 link state on unnumbered interfaces
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VeC 41]: vlib: fix trace flag loss when multiple pending frames share next frame
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 125]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 127]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 127]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 127]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 127]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 133]: ip6-nd: fix unicast NA handling in ND proxy

**Benoît Ganne** <bganne@cisco.com>:

  | `46117 <https:////gerrit.fd.io/r/c/vpp/+/46117>`_ [VeC 31]: vppapigen: fix vppapigen depfile without imports
  | `46094 <https:////gerrit.fd.io/r/c/vpp/+/46094>`_ [VeC 31]: adl: wait for ADL counters
  | `46087 <https:////gerrit.fd.io/r/c/vpp/+/46087>`_ [VeC 31]: cnat: wait for cnat scanner session cleanup

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [veC 47]: ikev2: add Curve25519 and Curve448 DH groups

**Dave Wallace** <dwallacelf@gmail.com>:

  | `46075 <https:////gerrit.fd.io/r/c/vpp/+/46075>`_ [vEC 7]: docs: update tsc vulnerability management process

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 129]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 129]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45684 <https:////gerrit.fd.io/r/c/vpp/+/45684>`_ [VEc 3]: buffers: return values; improve debug
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VeC 38]: crypto: add op tracing capability
  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [Vec 78]: dpdk: tracing improvements

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [vEC 29]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [vEC 29]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [VEc 30]: sfdp: add verdict-testbench service
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VeC 42]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VeC 42]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [Vec 45]: tracepath: minor refactoring to code
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VeC 63]: sfdp: add sfdp-session-stats service
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VeC 66]: sfdp: fix specification of scope_index

**Hanataba Azaka** <northern.snow.x@gmail.com>:

  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [VeC 31]: cnat: make session scanner budget configurable

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `46147 <https:////gerrit.fd.io/r/c/vpp/+/46147>`_ [VEc 27]: npol: support prednat policies
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [Vec 31]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 119]: tests: reduce sleep interval in ip-neighbor age test
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 148]: crypto: unify per-thread key_data allocation

**Janik** <janik.haag@imc.com>:

  | `46122 <https:////gerrit.fd.io/r/c/vpp/+/46122>`_ [VEc 2]: build: fix make install-deps for fedora targets
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VeC 31]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VeC 31]: vcl: add regression test for ignorable flags
  | `46121 <https:////gerrit.fd.io/r/c/vpp/+/46121>`_ [VeC 31]: sasc: fix gcc uninitialized warning

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 167]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 167]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 167]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 167]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VEc 3]: af_xdp: add support for multi-buffer
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VEc 14]: rdma: add mlx5 DV TSO support for raw packet tx
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VEc 24]: iavf: fix native TSO datapath
  | `45775 <https:////gerrit.fd.io/r/c/vpp/+/45775>`_ [VeC 72]: tcp: fix pure ACK incorrectly chained as GRO candidate
  | `45759 <https:////gerrit.fd.io/r/c/vpp/+/45759>`_ [VeC 72]: tcp: support chained buffers in GRO
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VeC 72]: tcp: allow selective GRO enablement
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 86]: virtio: add native plugin L2 xconnect test with QEMU

**Jiajun Liang** <3138947285@qq.com>:

  | `45677 <https:////gerrit.fd.io/r/c/vpp/+/45677>`_ [VEc 13]: linux-cp: guard PPPOX interface type and tolerate missing neighbor

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [Vec 43]: ip bonding hash: inner-aware flow hash (opt-in)

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 169]: vppapigen: fix json build error

**Justin Thomas** <justin@jdt.io>:

  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VeC 111]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VeC 111]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

**Klement Sekera** <ksekera@netgate.com>:

  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VeC 69]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VeC 92]: vppinfra: add cast to prevent warning

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [Vec 42]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [Vec 42]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Matus Fabian** <matfabia@cisco.com>:

  | `46079 <https:////gerrit.fd.io/r/c/vpp/+/46079>`_ [vEC 27]: hs-test: temporarily disable core file removal

**Maxime Peim** <maxime.peim@gmail.com>:

  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VEc 1]: vlib: add per-thread index pool cache
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [vEc 20]: dpdk: support async flow offload
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [veC 43]: docs: document build-time VPP parameters
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VeC 49]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [vec 49]: flow: add per-thread flow pool cache for multi-worker safety
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [veC 49]: dpdk: multi-thread async flow offload with per-worker caches
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VeC 122]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VeC 122]: gso: implement IPv6 extension header traversal
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 128]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 128]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 128]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 128]: policer: reject deletion of policer used by punt policing

**Miroslav Miklus** <miroslav.miklus@pantheon.tech>:

  | `46276 <https:////gerrit.fd.io/r/c/vpp/+/46276>`_ [vEC 2]: wireguard: remove barrier from keypair rotation
  | `46277 <https:////gerrit.fd.io/r/c/vpp/+/46277>`_ [vEC 7]: wireguard: add rekey and index churn test
  | `46275 <https:////gerrit.fd.io/r/c/vpp/+/46275>`_ [vEC 7]: wireguard: use bihash for sender index table

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [veC 62]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VeC 107]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 127]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 133]: sfdp: add blacklist/whitelist to snort service
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 156]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 160]: pg: Guard against non‑monotonic time and negative accumulator

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 173]: iouring: Add io_uring plugin to allow polling usage of io_uring

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 106]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 106]: ip6-nd: add nd-proxy all dst
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 114]: ip6: fix show ip6-ll cli if selector
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 155]: ip6-nd: support RA pfx info option with flag L&!A

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vec 49]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [Vec 99]: papi: improve performance on set_errors

**Onong Tayeng** <onong.tayeng@gmail.com>:

  | `46217 <https:////gerrit.fd.io/r/c/vpp/+/46217>`_ [vEC 14]: npol: export flow decision counters

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 174]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 176]: fix: correct fixstyle in session_sdl command function

**Pim van Pelt** <pim@ipng.nl>:

  | `46038 <https:////gerrit.fd.io/r/c/vpp/+/46038>`_ [Vec 36]: ip6-nd: fix crash in link-local target NS
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VeC 106]: lb: Add punt feature to per-port VIPs

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [Vec 57]: pfc: add framework for priority flow control
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VeC 69]: octeon: add PFC support

**Ram Subramanian** <ram@meter.com>:

  | `46080 <https:////gerrit.fd.io/r/c/vpp/+/46080>`_ [VeC 31]: l2: fix race condition and null ptr dereference in l2fib_scan
  | `46059 <https:////gerrit.fd.io/r/c/vpp/+/46059>`_ [VeC 31]: l2: fix buffer overflow while finding next node
  | `46062 <https:////gerrit.fd.io/r/c/vpp/+/46062>`_ [VeC 31]: vlib: fix buffer ref_count accounting in partial clone
  | `46066 <https:////gerrit.fd.io/r/c/vpp/+/46066>`_ [VeC 37]: vppinfra: fifo: do not resize vector down to 0
  | `46065 <https:////gerrit.fd.io/r/c/vpp/+/46065>`_ [VeC 37]: vlib: punt: fix buffer reference after clone
  | `46057 <https:////gerrit.fd.io/r/c/vpp/+/46057>`_ [VeC 37]: interface: do not increase tx error counter on admin/link down interfaces

**Robert Shearman** <robertshearman@gmail.com>:

  | `46051 <https:////gerrit.fd.io/r/c/vpp/+/46051>`_ [VeC 40]: ip: fix punt socket rx when multiple FDs are ready
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VeC 40]: ip: fix ip mroute bulk insertion CLI for certain inputs
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VeC 42]: vlib: ASAN-poison unallocated buffers
  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [Vec 44]: misc: fix potential OOB read during flow hash calculations
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VeC 50]: ip: fix adjacent packet overwrite with ip frags
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [VeC 50]: ip: fix adjacent packet overwrite with ip6 frags
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VeC 83]: vppapigen: fix inconsistency in paths JSON

**Shuzo Ichiyoshi** <deadcafe.beef@gmail.com>:

  | `46179 <https:////gerrit.fd.io/r/c/vpp/+/46179>`_ [vEC 15]: tcp: mark half-open done before deferred cleanup
  | `46176 <https:////gerrit.fd.io/r/c/vpp/+/46176>`_ [vEC 21]: session: cache process-wide CPU time for workers
  | `46178 <https:////gerrit.fd.io/r/c/vpp/+/46178>`_ [vEC 23]: session: validate app for async connect RPC
  | `46180 <https:////gerrit.fd.io/r/c/vpp/+/46180>`_ [vEC 24]: session: check event collector lookups

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VeC 35]: fib: dump by src not only contributing routes
  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [veC 35]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [veC 35]: linux-cp: fix cleanup of special routes

**Viacheslav Zakharchenko** <vzakharc@cisco.com>:

  | `45807 <https:////gerrit.fd.io/r/c/vpp/+/45807>`_ [VEc 8]: bfd: Introduce vppinfra/callback_data based vnet notifier for FIB/ADJ notifications
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [VEc 9]: bfd: Extract to plugin

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [Vec 66]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [veC 114]: vppinfra: collect heap stats in constant time

**Vratko Polak** <vrpolak@cisco.com>:

  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vec 55]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [veC 99]: empty change for GHA(CSIT) testing

**Wei Wang** <weiwa@cisco.com>:

  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [VEc 28]: tls: tls session resumption code and host stack tests

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VeC 57]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer
  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [Vec 57]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [veC 58]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VeC 58]: vlib: fix process state format output wrapped by extra quotes
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vec 64]: vlib: pre-input node should be dispatched before input node

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [VEc 20]: vppinfra: add loongarch64 architecture support

**Yuto Suzuki** <offside.items03@icloud.com>:

  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VEc 1]: ip6-nd: support RDNSS option in IPv6 RA
  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VEc 1]: ip6-nd: update secondary RA prefixes for subnets

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 163]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [veC 73]: vlib: fix '\' command input will causes memory out of bounds
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [Vec 114]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [Vec 114]: dns: support ipv6 server to resolve name
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VeC 115]: build rpm-packaging: make vpp rpm package for kylinV11
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 168]: docs: Python apis examples

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 87]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [veC 35]: cnat: add scope_id to session key

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 126]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 114]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [veC 114]: lb: fix API byte order and IPv4 prefix length handling

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VeC 83]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VeC 70]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VeC 72]: tls: fix picotls partial record handling
  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [Vec 73]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [Vec 79]: session: make transport to use application's segment manager

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 178]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 178]: l2: fix null pointer access in l2-efp-filter

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
authors          155
maintainers      47
committers       1
abandoned        0
================ ===

