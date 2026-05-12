
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Tuesday 2026-05-12, 04:47:51
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

  | `45707 <https:////gerrit.fd.io/r/c/vpp/+/45707>`_ [VECR 6]: npol: wire npol into the cnat slow-path hook mechanism

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 14]: af_xdp: add support for multi-buffer

atlantic: **Damjan Marion** <dmarion@me.com>
  | `45590 <https:////gerrit.fd.io/r/c/vpp/+/45590>`_ [VECr 2]: iavf: add L4 checksum offload on RX

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `45684 <https:////gerrit.fd.io/r/c/vpp/+/45684>`_ [VECr 4]: buffers: return values; improve debug

build: **Damjan Marion** <damarion@cisco.com>
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 3]: api: add build-time python stub generation via vppapigen
  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [VECr 10]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 6]: crypto: add op tracing capability

dev: **Damjan Marion** <damarion@cisco.com>
  | `45590 <https:////gerrit.fd.io/r/c/vpp/+/45590>`_ [VECr 2]: iavf: add L4 checksum offload on RX
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 11]: flow: single-interface-per-flow model

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45674 <https:////gerrit.fd.io/r/c/vpp/+/45674>`_ [VECr 3]: dhcp: export DHCPv6 runtime state for PPPoE observability

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [VECr 0]: misc: patch to test CI infra
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 0]: rdma: add mlx5 TSO support for raw packet tx
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 6]: sfdp: add sfdp-session-stats service

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 3]: dpdk: log MFIB MAC replay tolerance at debug level
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 11]: flow: single-interface-per-flow model
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 11]: flow: restructure vnet_flow_t for cache-line optimization
  | `45247 <https:////gerrit.fd.io/r/c/vpp/+/45247>`_ [VECr 11]: flow: encapsulate driver state into driver_data struct
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [VECr 11]: dpdk: support async flow offload
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VECr 11]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [VECr 11]: dpdk: multi-thread async flow offload with per-worker caches

fib: **Neale Ranns** <neale@graphiant.com>
  | `45732 <https:////gerrit.fd.io/r/c/vpp/+/45732>`_ [VECr 3]: fib: omit mac addr add/del when not supported
  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VECr 10]: fib: IPv4 Route Query Command Crash
  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VECr 14]: fib: compute fib entry flags from full path list

flow: **Damjan Marion** <damarion@cisco.com>
  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [VECr 6]: flow: add per-thread flow pool cache for multi-worker safety
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 11]: flow: add flow template and async range infrastructure
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 11]: flow: single-interface-per-flow model
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 11]: flow: restructure vnet_flow_t for cache-line optimization
  | `45247 <https:////gerrit.fd.io/r/c/vpp/+/45247>`_ [VECr 11]: flow: encapsulate driver state into driver_data struct

flowprobe: **Ole Troan** <otroan@employees.org>
  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [VECr 0]: flowprobe: count based sampling support

gtpu: **Hongjun Ni** <hongjun.ni@intel.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 11]: flow: single-interface-per-flow model
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 11]: flow: restructure vnet_flow_t for cache-line optimization

http: **Florin Coras** <fcoras@cisco.com>
  | `45767 <https:////gerrit.fd.io/r/c/vpp/+/45767>`_ [VECr 0]: http: h2 always unschedule connection when closing

iavf: **Damjan Marion** <damarion@cisco.com>
  | `45590 <https:////gerrit.fd.io/r/c/vpp/+/45590>`_ [VECr 2]: iavf: add L4 checksum offload on RX
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 5]: iavf: fix native TSO datapath for 1500-byte frames

ige: **Damjan Marion** <damarion@cisco.com>
  | `45590 <https:////gerrit.fd.io/r/c/vpp/+/45590>`_ [VECr 2]: iavf: add L4 checksum offload on RX

interface: **Dave Barach** <vpp@barachs.net>
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 11]: flow: add flow template and async range infrastructure
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 11]: flow: single-interface-per-flow model
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VECr 24]: interface: enable IPv6 link state on unnumbered interfaces

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 19]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45494 <https:////gerrit.fd.io/r/c/vpp/+/45494>`_ [VECr 19]: ip: fix reassembly bugs and add tests
  | `45495 <https:////gerrit.fd.io/r/c/vpp/+/45495>`_ [VECr 19]: ip: fix reassembly bugs, add extended SV reass CLI and tests
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VECr 29]: ip6-nd: support RDNSS option in IPv6 RA

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VECr 28]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VECr 29]: ip6-nd: support RDNSS option in IPv6 RA

ipfix-export: **Ole Troan** <otroan@employees.org>, **Paul Atkins** <patkins@graphiant.com>
  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [VECr 0]: flowprobe: count based sampling support

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 6]: crypto: add op tracing capability

kube-test: **Florin Coras** <fcoras@cisco.com>
  | `45768 <https:////gerrit.fd.io/r/c/vpp/+/45768>`_ [VECr 0]: kube-test: update latest CalicoVPP release to v3.32.0

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `45487 <https:////gerrit.fd.io/r/c/vpp/+/45487>`_ [VECr 26]: lb: Allow setting weight on AS
  | `45428 <https:////gerrit.fd.io/r/c/vpp/+/45428>`_ [VECr 27]: lb: API bugfix

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `45677 <https:////gerrit.fd.io/r/c/vpp/+/45677>`_ [VECr 3]: linux-cp: guard PPPOX interface type and tolerate missing neighbor

lldp: **Klement Sekera** <klement.sekera@gmail.com>
  | `45672 <https:////gerrit.fd.io/r/c/vpp/+/45672>`_ [VECr 4]: lldp: invalid type for macaddr management address

map: **Ole Troan** <otroan@employees.org>, **Jon Loeliger** <jdl@netgate.com>
  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VECr 12]: map: enhance map plugin to support per-vrf rules

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 3]: api: add build-time python stub generation via vppapigen
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 6]: crypto: add op tracing capability
  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [VECr 10]: ip_validate: new plugin to drop packets with invalid addresses
  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [VECr 10]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 19]: ip: svr add bit indicating fragmentation to vnet_buffer

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VECr 0]: octeon: add PFC support
  | `45590 <https:////gerrit.fd.io/r/c/vpp/+/45590>`_ [VECr 2]: iavf: add L4 checksum offload on RX
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 11]: flow: single-interface-per-flow model
  | `45247 <https:////gerrit.fd.io/r/c/vpp/+/45247>`_ [VECr 11]: flow: encapsulate driver state into driver_data struct

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `45502 <https:////gerrit.fd.io/r/c/vpp/+/45502>`_ [VECr 30]: ping: set LOCALLY_ORIGINATED flag on cli-initiated ping packets.

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 0]: rdma: add mlx5 TSO support for raw packet tx
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [VECr 3]: rdma: steer PPPoE discovery and session flows

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 6]: sfdp: add sfdp-session-stats service

snort: **Damjan Marion** <damarion@cisco.com>
  | `45727 <https:////gerrit.fd.io/r/c/vpp/+/45727>`_ [VECr 3]: snort: fix daq instance enumeration

tcp: **Florin Coras** <fcoras@cisco.com>
  | `45759 <https:////gerrit.fd.io/r/c/vpp/+/45759>`_ [VECr 0]: tcp: support chained buffers in GRO

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [VECr 0]: flowprobe: count based sampling support
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 6]: sfdp: add sfdp-session-stats service
  | `45696 <https:////gerrit.fd.io/r/c/vpp/+/45696>`_ [VECr 6]: cnat: make cnat pluggable
  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VECr 12]: map: enhance map plugin to support per-vrf rules
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VECr 13]: virtio: add native plugin L2 xconnect test with QEMU
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 14]: af_xdp: add support for multi-buffer
  | `45494 <https:////gerrit.fd.io/r/c/vpp/+/45494>`_ [VECr 19]: ip: fix reassembly bugs and add tests
  | `45495 <https:////gerrit.fd.io/r/c/vpp/+/45495>`_ [VECr 19]: ip: fix reassembly bugs, add extended SV reass CLI and tests
  | `45487 <https:////gerrit.fd.io/r/c/vpp/+/45487>`_ [VECr 26]: lb: Allow setting weight on AS
  | `45428 <https:////gerrit.fd.io/r/c/vpp/+/45428>`_ [VECr 27]: lb: API bugfix
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VECr 29]: ip6-nd: support RDNSS option in IPv6 RA

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 0]: tls: propagate verify config for dtls

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VECr 14]: fib: compute fib entry flags from full path list

vcl: **Florin Coras** <fcoras@cisco.com>
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [VECr 0]: misc: patch to test CI infra

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VECr 20]: vlib: fix trace flag loss when multiple pending frames share next frame

vpp: **Dave Barach** <vpp@barachs.net>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 6]: sfdp: add sfdp-session-stats service

vppapigen: **Ole Troan** <otroan@employees.org>
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 3]: api: add build-time python stub generation via vppapigen
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VECr 10]: vppapigen: fix inconsistency in paths JSON

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `45669 <https:////gerrit.fd.io/r/c/vpp/+/45669>`_ [VECr 4]: vppinfra: support high NUMA node IDs in discovery
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [VECr 11]: dpdk: support async flow offload
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VECr 19]: vppinfra: add cast to prevent warning

vxlan: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 11]: flow: single-interface-per-flow model
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 11]: flow: restructure vnet_flow_t for cache-line optimization

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Aarnav JP** <ajp@marvell.com>:

  | `45195 <https:////gerrit.fd.io/r/c/vpp/+/45195>`_ [VEc 4]: octeon: ensure 64KB alignment for BAR mappings

**Akos Orban** <orbanakos2001@gmail.com>:

  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 76]: cnat: fix show cnat translation for specific translation id
  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 76]: cnat: fix show cnat client showing invalid for client id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 41]: vhost: fix rxvq interrupts triggered because of race

**Alok Mishra** <almishra@marvell.com>:

  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [VeC 31]: tm: add 'mark_flow' action for traffic management
  | `42257 <https:////gerrit.fd.io/r/c/vpp/+/42257>`_ [VeC 63]: octeon: implement hardware traffic management

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 110]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [VeC 138]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Aritra Basu** <aritrbas@cisco.com>:

  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [VEc 0]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 52]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 54]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 54]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 54]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 54]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 60]: ip6-nd: fix unicast NA handling in ND proxy

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 138]: pnat: do not disable pnat on rule deletion

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [vEC 10]: ikev2: add Curve25519 and Curve448 DH groups

**Duncan Eastoe** <duncaneastoe+github@gmail.com>:

  | `45042 <https:////gerrit.fd.io/r/c/vpp/+/45042>`_ [VeC 54]: stats: stat_segment_ls_r() only return NULL on error
  | `45043 <https:////gerrit.fd.io/r/c/vpp/+/45043>`_ [VeC 54]: stats: don't leak regcomp() allocated memory

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 56]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 56]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [VEc 5]: dpdk: tracing improvements

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `45660 <https:////gerrit.fd.io/r/c/vpp/+/45660>`_ [VEc 0]: sfdp: fix FIN with payload in l4-lifecycle
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [vEC 0]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [vEC 6]: dpdk: add support for represented port action
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [vEC 10]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [vEC 10]: flow: add flow aging support
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [vEC 10]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [vEC 10]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [vEC 10]: sfdp: add verdict-testbench service
  | `45564 <https:////gerrit.fd.io/r/c/vpp/+/45564>`_ [VEc 13]: sfdp: add api enum for timeouts
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [Vec 77]: sfdp: modify tenant_index type from u16 to u32
  | `44474 <https:////gerrit.fd.io/r/c/vpp/+/44474>`_ [Vec 124]: sasc: fix tenant_index overlap in sasc_buffer

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 46]: tests: reduce sleep interval in ip-neighbor age test
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 75]: crypto: unify per-thread key_data allocation

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 94]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 94]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 94]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 94]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [vEC 0]: tcp: allow selective GRO enablement
  | `45101 <https:////gerrit.fd.io/r/c/vpp/+/45101>`_ [VEc 0]: sfdp: guard packet bit shifts in lookup

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 96]: vppapigen: fix json build error

**Justin Thomas** <justin@jdt.io>:

  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VeC 38]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VeC 38]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [VEc 5]: ipip: add mp2p ipip tunnel

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VeC 49]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VeC 49]: gso: implement IPv6 extension header traversal
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 55]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 55]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 55]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 55]: policer: reject deletion of policer used by punt policing

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 152]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VeC 34]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 54]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 60]: sfdp: add blacklist/whitelist to snort service
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 83]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 87]: pg: Guard against non‑monotonic time and negative accumulator
  | `44426 <https:////gerrit.fd.io/r/c/vpp/+/44426>`_ [VeC 122]: virtio: add the check if MAC feature is negotiated

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 100]: iouring: Add io_uring plugin to allow polling usage of io_uring

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 33]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 33]: ip6-nd: add nd-proxy all dst
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 41]: ip6: fix show ip6-ll cli if selector
  | `44903 <https:////gerrit.fd.io/r/c/vpp/+/44903>`_ [VeC 77]: vxlan: reset next_dpo on delete
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 82]: ip6-nd: support RA pfx info option with flag L&!A

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vEC 0]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [VEc 26]: papi: improve performance on set_errors

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 101]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 103]: fix: correct fixstyle in session_sdl command function

**Pim van Pelt** <pim@ipng.nl>:

  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VeC 33]: lb: Add punt feature to per-port VIPs

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [vEC 0]: pfc: add framework for priority flow control

**Samuel Benko** <sbenko@cisco.com>:

  | `45766 <https:////gerrit.fd.io/r/c/vpp/+/45766>`_ [vEC 0]: hs-test: add dtls crl reject allow test
  | `45722 <https:////gerrit.fd.io/r/c/vpp/+/45722>`_ [VEc 0]: hs-test: add app-namespace VCL echo tests

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [veC 41]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [VeC 136]: linux-cp: fix cleanup of special routes
  | `44241 <https:////gerrit.fd.io/r/c/vpp/+/44241>`_ [Vec 144]: linux-cp: on remove do cleanup for all fibs
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VeC 159]: fib: dump by src not only contributing routes

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [Vec 47]: tm: add tm framework for hw traffic management

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [veC 41]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44575 <https:////gerrit.fd.io/r/c/vpp/+/44575>`_ [VeC 122]: fib: add interface-rx dpo mpls support
  | `44574 <https:////gerrit.fd.io/r/c/vpp/+/44574>`_ [VeC 122]: fib: fix stale interface-rx dpo fib after deag/lookup
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 122]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 122]: nat: speedup nat44-ed vrf table lookups
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 122]: nat: fix nat44-ed address removal from fib
  | `44563 <https:////gerrit.fd.io/r/c/vpp/+/44563>`_ [veC 123]: ip: fix DSCP CS7 value
  | `44568 <https:////gerrit.fd.io/r/c/vpp/+/44568>`_ [VeC 123]: vxlan: add default dscp value config for vxlan encap
  | `44567 <https:////gerrit.fd.io/r/c/vpp/+/44567>`_ [VeC 123]: udp: add default dscp value config for udp encap
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 123]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 123]: fib: fix udp encap mp-safe ops and id validation
  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 123]: fib: avoid loadbalance dpo node path polarisation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 123]: vlib: mark cli quit command as mp_safe

**Vratko Polak** <vrpolak@cisco.com>:

  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [VEc 0]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [vEC 26]: empty change for GHA(CSIT) testing

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 138]: ip-neighbor: ARP/NA per-interface counter improvements

**echo** <614699596@qq.com>:

  | `45348 <https:////gerrit.fd.io/r/c/vpp/+/45348>`_ [VeC 45]: bpf_trace_filter: fix bpf_expr memory leak on error path

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 90]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [vEC 0]: vlib: fix '\' command input will causes memory out of bounds
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [Vec 41]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [Vec 41]: dns: support ipv6 server to resolve name
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VeC 42]: build rpm-packaging: make vpp rpm package for kylinV11
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 95]: docs: Python apis examples

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VEc 0]: cnat: add scope_id to session key

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 53]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 41]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [veC 41]: lb: fix API byte order and IPv4 prefix length handling
  | `44207 <https:////gerrit.fd.io/r/c/vpp/+/44207>`_ [VeC 135]: lb: fix incorrect byte order conversion for vip port display

**steven luong** <sluong@cisco.com>:

  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [VEc 0]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [VEc 6]: session: make transport to use application's segment manager
  | `44569 <https:////gerrit.fd.io/r/c/vpp/+/44569>`_ [VeC 123]: vppinfra: clib_time_verify_frequency may cause time jump

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 105]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 105]: l2: fix null pointer access in l2-efp-filter

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**Damjan Marion** <dmarion@0xa5.net>:

  | `44092 <https:////gerrit.fd.io/r/c/vpp/+/44092>`_ [A 180]: ipsec: precompute payload and payload length adjustments

**ruici wang** <964491902@qq.com>:

  | `44100 <https:////gerrit.fd.io/r/c/vpp/+/44100>`_ [A 180]: ipsec: prevent use of deleted keys in async mode

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
authors          110
maintainers      51
committers       1
abandoned        2
================ ===

