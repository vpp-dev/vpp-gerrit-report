#################
VPP-GERRIT-REPORT
#################

VPP Gerrit Report categorizes the state of the gerrit.fd.io review queue.  Each gerrit change is labeled with the following status:

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
    - No unresolved comments
    - Review incomplete (Code-Review < +1)
    - 23 days since last update

The report generator sorts the gerrit changes into three categories based on the state and the person or group required to perform the next action:

- Committers:
  Status [VECR xx]: Gerrit Changes that have been verified, are not expired, no unresolved comments, & approved by a maintainer.
  Action: A committer should do a final review and submit the change or provide comment(s).

- Maintainers:
  Status [VECr]: Gerrit Changes that have been verified, are not expired, no unresolved comments, & not reviewed
  Action: The Maintainer should do a code review

- Authors:
  Status <other>: Gerrit Changes that are either not verified, expired, or comments not resolved
  Action: Author should rebase the change, fix verification errors, and/or resolve comments to move the status to [VECr]# Gerrit open patches processing tool

Here is the latest VPP Gerrit Report:
-------------------------------------

==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Friday 2026-06-19, 06:29:48
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

  | `45707 <https:////gerrit.fd.io/r/c/vpp/+/45707>`_ [VECR 0]: npol: wire npol into the cnat slow-path hook mechanism
  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VECR 10]: cnat: fix show cnat client showing invalid for client id
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VECR 10]: cnat: fix show cnat translation for specific translation id

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 1]: af_xdp: add support for multi-buffer

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `46064 <https:////gerrit.fd.io/r/c/vpp/+/46064>`_ [VECr 2]: vlib: buffer: fix null ptr dereference
  | `46062 <https:////gerrit.fd.io/r/c/vpp/+/46062>`_ [VECr 2]: vlib: fix buffer ref_count accounting in partial clone
  | `45684 <https:////gerrit.fd.io/r/c/vpp/+/45684>`_ [VECr 3]: buffers: return values; improve debug
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VECr 7]: vlib: ASAN-poison unallocated buffers

build: **Damjan Marion** <damarion@cisco.com>
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 2]: api: add build-time python stub generation via vppapigen
  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VECr 6]: build: include GNUInstallDirs in VPPConfig
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VECr 14]: dpdk: install default jump-to-group-1 rule for mlx5

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [VECr 3]: cnat: make session scanner budget configurable

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 3]: crypto: add op tracing capability

dev: **Damjan Marion** <damarion@cisco.com>
  | `46060 <https:////gerrit.fd.io/r/c/vpp/+/46060>`_ [VECr 2]: dev: hold worker thread barrier during port stop
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 7]: flow: implement VNET_FLOW_ACTION_COUNT operation

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 28]: sfdp: add sfdp-session-stats service

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VECr 7]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VECr 7]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 7]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VECr 14]: dpdk: install default jump-to-group-1 rule for mlx5

fib: **Neale Ranns** <neale@graphiant.com>
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VECr 0]: fib: dump by src not only contributing routes

flow: **Damjan Marion** <damarion@cisco.com>
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 0]: flow: add flow template and async range infrastructure
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VECr 7]: flow: add APIs to support new flow actions
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VECr 7]: flow: add parameter to pre-allocate global pool
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 7]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VECr 7]: flow: add flow aging support
  | `45908 <https:////gerrit.fd.io/r/c/vpp/+/45908>`_ [VECr 16]: flow: add max parameter in 'show flow entry' CLI

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [VECr 0]: tls: tls session resumption code and host stack tests
  | `46039 <https:////gerrit.fd.io/r/c/vpp/+/46039>`_ [VECr 0]: http: handling of fifo memory pressure
  | `46076 <https:////gerrit.fd.io/r/c/vpp/+/46076>`_ [VECr 1]: hs-test: fix suite and test names
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 7]: tls: propagate verify config for dtls
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VECr 24]: vlib: fix process state format output wrapped by extra quotes

http: **Florin Coras** <fcoras@cisco.com>
  | `46039 <https:////gerrit.fd.io/r/c/vpp/+/46039>`_ [VECr 0]: http: handling of fifo memory pressure

iavf: **Damjan Marion** <damarion@cisco.com>
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 27]: iavf: fix native TSO datapath

interface: **Dave Barach** <vpp@barachs.net>
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 0]: flow: add flow template and async range infrastructure
  | `46057 <https:////gerrit.fd.io/r/c/vpp/+/46057>`_ [VECr 2]: interface: do not increase tx error counter on admin/link down interfaces
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VECr 6]: interface: enable IPv6 link state on unnumbered interfaces
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 7]: flow: implement VNET_FLOW_ACTION_COUNT operation

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VECr 0]: fib: dump by src not only contributing routes
  | `46051 <https:////gerrit.fd.io/r/c/vpp/+/46051>`_ [VECr 5]: ip: fix punt socket rx when multiple FDs are ready
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VECr 5]: ip: fix ip mroute bulk insertion CLI for certain inputs
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VECr 15]: ip: fix adjacent packet overwrite with ip frags
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [VECr 15]: ip: fix adjacent packet overwrite with ip6 frags

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `46074 <https:////gerrit.fd.io/r/c/vpp/+/46074>`_ [VECr 2]: ipsec: fix incorrect return types
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 3]: crypto: add op tracing capability

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `46080 <https:////gerrit.fd.io/r/c/vpp/+/46080>`_ [VECr 1]: l2: refetch client registration before send in l2fib_scan
  | `46059 <https:////gerrit.fd.io/r/c/vpp/+/46059>`_ [VECr 3]: l2: fix buffer overflow while finding next node

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 2]: api: add build-time python stub generation via vppapigen
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 3]: crypto: add op tracing capability
  | `45961 <https:////gerrit.fd.io/r/c/vpp/+/45961>`_ [VECr 6]: hsa: handle vperf client session closes/resets
  | `45858 <https:////gerrit.fd.io/r/c/vpp/+/45858>`_ [VECr 6]: hsa: fix builtin cut-through

npol: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Hedi Bouattour** <hedibouattour2010@gmail.com>
  | `46046 <https:////gerrit.fd.io/r/c/vpp/+/46046>`_ [VECr 6]: npol: fix interface name parsing

pvti: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `45956 <https:////gerrit.fd.io/r/c/vpp/+/45956>`_ [VECr 10]: pvti: fix adjacent packet overwrite with very big packets

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [VECr 0]: rdma: steer PPPoE discovery and session flows

session: **Florin Coras** <fcoras@cisco.com>
  | `46086 <https:////gerrit.fd.io/r/c/vpp/+/46086>`_ [VECr 0]: session: avoid rx evts after disconnect notification

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 28]: sfdp: add sfdp-session-stats service

snort: **Damjan Marion** <damarion@cisco.com>
  | `45915 <https:////gerrit.fd.io/r/c/vpp/+/45915>`_ [VECr 7]: snort: fix wrong variable reference
  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VECr 27]: snort: don't store snort metadata in buffer

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46072 <https:////gerrit.fd.io/r/c/vpp/+/46072>`_ [VECr 0]: tests: add USE_SMT to allocate logical CPUs, not whole cores
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45917 <https:////gerrit.fd.io/r/c/vpp/+/45917>`_ [VECr 0]: linux-cp: mcast ospf test
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 1]: af_xdp: add support for multi-buffer
  | `45837 <https:////gerrit.fd.io/r/c/vpp/+/45837>`_ [VECr 3]: tests: add suffix to failed_test file
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VECr 5]: ip: fix ip mroute bulk insertion CLI for certain inputs
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VECr 7]: vlib: ASAN-poison unallocated buffers
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 28]: sfdp: add sfdp-session-stats service

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [VECr 0]: tls: tls session resumption code and host stack tests
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 7]: tls: propagate verify config for dtls

vcl: **Florin Coras** <fcoras@cisco.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46065 <https:////gerrit.fd.io/r/c/vpp/+/46065>`_ [VECr 2]: vlib: punt: fix buffer reference after clone
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VECr 6]: vlib: fix trace flag loss when multiple pending frames share next frame
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VECr 24]: vlib: fix process state format output wrapped by extra quotes

vperf: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [VECr 0]: tls: tls session resumption code and host stack tests

vpp: **Dave Barach** <vpp@barachs.net>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 28]: sfdp: add sfdp-session-stats service

vppapigen: **Ole Troan** <otroan@employees.org>
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 2]: api: add build-time python stub generation via vppapigen

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `46066 <https:////gerrit.fd.io/r/c/vpp/+/46066>`_ [VECr 2]: vppinfra: fifo: do not resize vector down to 0
  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VECr 22]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [VEc 3]: ip_validate: new plugin to drop packets with invalid addresses

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 79]: vhost: fix rxvq interrupts triggered because of race

**Alexander Maltsev** <keltar.gw@gmail.com>:

  | `45801 <https:////gerrit.fd.io/r/c/vpp/+/45801>`_ [VEc 0]: session: read-lock segment manager in fifo tuning

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 148]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VeC 50]: map: enhance map plugin to support per-vrf rules

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [VeC 176]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Aritra Basu** <aritrbas@cisco.com>:

  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VEc 2]: tcp: add TCP fast open support (RFC 7413)
  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [VEc 3]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 90]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 92]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 92]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 92]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 92]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 98]: ip6-nd: fix unicast NA handling in ND proxy

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 176]: pnat: do not disable pnat on rule deletion

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [vEC 13]: ikev2: add Curve25519 and Curve448 DH groups

**Dave Wallace** <dwallacelf@gmail.com>:

  | `46075 <https:////gerrit.fd.io/r/c/vpp/+/46075>`_ [VEc 0]: docs: update tsc vulnerability management process

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 94]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 94]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [Vec 43]: dpdk: tracing improvements

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `44474 <https:////gerrit.fd.io/r/c/vpp/+/44474>`_ [VEc 1]: sasc: fix tenant_index overlap in sasc_buffer
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [vEC 7]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [VEc 7]: sfdp: add verdict-testbench service
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [vEC 7]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [VEc 10]: tracepath: minor refactoring to code
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VeC 31]: sfdp: fix specification of scope_index
  | `45564 <https:////gerrit.fd.io/r/c/vpp/+/45564>`_ [Vec 51]: sfdp: add api enum for timeouts
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [Vec 115]: sfdp: modify tenant_index type from u16 to u32

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [VEc 10]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get

**Ivan Ivanets** <iivanets@cisco.com>:

  | `46044 <https:////gerrit.fd.io/r/c/vpp/+/46044>`_ [vEC 7]: vcl: guard QUIC connection close error-code
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 84]: tests: reduce sleep interval in ip-neighbor age test
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 113]: crypto: unify per-thread key_data allocation

**Janik** <janik.haag@imc.com>:

  | `46082 <https:////gerrit.fd.io/r/c/vpp/+/46082>`_ [vEC 0]: vcl: allow polling connect() on nonblocking socket
  | `46083 <https:////gerrit.fd.io/r/c/vpp/+/46083>`_ [vEc 0]: vcl: strip ignorable flags

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 132]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 132]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 132]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 132]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VeC 36]: rdma: add mlx5 TSO support for raw packet tx
  | `45775 <https:////gerrit.fd.io/r/c/vpp/+/45775>`_ [VeC 37]: tcp: fix pure ACK incorrectly chained as GRO candidate
  | `45759 <https:////gerrit.fd.io/r/c/vpp/+/45759>`_ [VeC 37]: tcp: support chained buffers in GRO
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VeC 37]: tcp: allow selective GRO enablement
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 51]: virtio: add native plugin L2 xconnect test with QEMU

**Jiajun Liang** <3138947285@qq.com>:

  | `45677 <https:////gerrit.fd.io/r/c/vpp/+/45677>`_ [vEC 0]: linux-cp: guard PPPOX interface type and tolerate missing neighbor
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [vEC 0]: dpdk: log MFIB MAC replay tolerance at debug level
  | `45674 <https:////gerrit.fd.io/r/c/vpp/+/45674>`_ [vEC 0]: dhcp: export DHCPv6 runtime state for PPPoE observability

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VEc 8]: ip bonding hash: inner-aware flow hash (opt-in)

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 134]: vppapigen: fix json build error

**Justin Thomas** <justin@jdt.io>:

  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VeC 76]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VeC 76]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

**Klement Sekera** <ksekera@netgate.com>:

  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VeC 34]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VeC 57]: vppinfra: add cast to prevent warning

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [VEc 7]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [VEc 8]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Matus Fabian** <matfabia@cisco.com>:

  | `46079 <https:////gerrit.fd.io/r/c/vpp/+/46079>`_ [vEC 1]: hs-test: temporarily disable core file removal

**Maxime Peim** <maxime.peim@gmail.com>:

  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VEc 1]: vlib: add per-thread pool cache primitive
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [vEC 8]: docs: document build-time VPP parameters
  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [vEc 14]: flow: add per-thread flow pool cache for multi-worker safety
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [vEC 14]: dpdk: support async flow offload
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [vEC 14]: dpdk: multi-thread async flow offload with per-worker caches
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VeC 87]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VeC 87]: gso: implement IPv6 extension header traversal
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 93]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 93]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 93]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 93]: policer: reject deletion of policer used by punt policing

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [vEC 27]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VeC 72]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 92]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 98]: sfdp: add blacklist/whitelist to snort service
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 121]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 125]: pg: Guard against non‑monotonic time and negative accumulator
  | `44426 <https:////gerrit.fd.io/r/c/vpp/+/44426>`_ [VeC 160]: virtio: add the check if MAC feature is negotiated

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 138]: iouring: Add io_uring plugin to allow polling usage of io_uring

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 71]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 71]: ip6-nd: add nd-proxy all dst
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 79]: ip6: fix show ip6-ll cli if selector
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 120]: ip6-nd: support RA pfx info option with flag L&!A

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vEc 14]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [Vec 64]: papi: improve performance on set_errors

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 140]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 141]: fix: correct fixstyle in session_sdl command function

**Pim van Pelt** <pim@ipng.nl>:

  | `46038 <https:////gerrit.fd.io/r/c/vpp/+/46038>`_ [VEc 1]: ip6-nd: fix crash in link-local target NS
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VeC 71]: lb: Add punt feature to per-port VIPs

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [VEc 22]: pfc: add framework for priority flow control
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VeC 34]: octeon: add PFC support

**Robert Shearman** <robertshearman@gmail.com>:

  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [VEc 9]: misc: fix potential OOB read during flow hash calculations
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VeC 48]: vppapigen: fix inconsistency in paths JSON

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [vEC 0]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [vEC 0]: linux-cp: fix cleanup of special routes

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [Vec 31]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [veC 79]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44575 <https:////gerrit.fd.io/r/c/vpp/+/44575>`_ [VeC 160]: fib: add interface-rx dpo mpls support
  | `44574 <https:////gerrit.fd.io/r/c/vpp/+/44574>`_ [VeC 160]: fib: fix stale interface-rx dpo fib after deag/lookup
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 160]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 160]: nat: speedup nat44-ed vrf table lookups
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 160]: nat: fix nat44-ed address removal from fib
  | `44563 <https:////gerrit.fd.io/r/c/vpp/+/44563>`_ [veC 161]: ip: fix DSCP CS7 value
  | `44568 <https:////gerrit.fd.io/r/c/vpp/+/44568>`_ [VeC 161]: vxlan: add default dscp value config for vxlan encap
  | `44567 <https:////gerrit.fd.io/r/c/vpp/+/44567>`_ [VeC 161]: udp: add default dscp value config for udp encap
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 161]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 161]: fib: fix udp encap mp-safe ops and id validation
  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 161]: fib: avoid loadbalance dpo node path polarisation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 161]: vlib: mark cli quit command as mp_safe

**Vratko Polak** <vrpolak@cisco.com>:

  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vEc 20]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [veC 64]: empty change for GHA(CSIT) testing

**Wayne Morrison** <wmorrison@netgate.com>:

  | `45949 <https:////gerrit.fd.io/r/c/vpp/+/45949>`_ [VEc 6]: lldp: extend data returned by lldp-dump API

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 176]: ip-neighbor: ARP/NA per-interface counter improvements

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [VEc 22]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [vEC 23]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vEc 29]: vlib: pre-input node should be dispatched before input node

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [VEc 3]: vppinfra: add loongarch64 architecture support

**echo** <614699596@qq.com>:

  | `45348 <https:////gerrit.fd.io/r/c/vpp/+/45348>`_ [VeC 84]: bpf_trace_filter: fix bpf_expr memory leak on error path

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 128]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [veC 38]: vlib: fix '\' command input will causes memory out of bounds
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [Vec 79]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [Vec 79]: dns: support ipv6 server to resolve name
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VeC 80]: build rpm-packaging: make vpp rpm package for kylinV11
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 133]: docs: Python apis examples

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 53]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [vEC 0]: cnat: add scope_id to session key

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 91]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 79]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [veC 79]: lb: fix API byte order and IPv4 prefix length handling
  | `44207 <https:////gerrit.fd.io/r/c/vpp/+/44207>`_ [VeC 173]: lb: fix incorrect byte order conversion for vip port display

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VeC 48]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VeC 35]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VeC 37]: tls: fix picotls partial record handling
  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [Vec 38]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [Vec 44]: session: make transport to use application's segment manager
  | `44569 <https:////gerrit.fd.io/r/c/vpp/+/44569>`_ [VeC 161]: vppinfra: clib_time_verify_frequency may cause time jump

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 143]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 143]: l2: fix null pointer access in l2-efp-filter

**yewtow** <offside.items03@icloud.com>:

  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VeC 66]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VeC 67]: ip6-nd: support RDNSS option in IPv6 RA

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
authors          135
maintainers      53
committers       3
abandoned        0
================ ===

