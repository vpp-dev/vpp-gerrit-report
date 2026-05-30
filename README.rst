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
generated on Saturday 2026-05-30, 05:00:02
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

  | `45846 <https:////gerrit.fd.io/r/c/vpp/+/45846>`_ [VECR 1]: quic: skip setting of ip and port in dgram hdr
  | `45891 <https:////gerrit.fd.io/r/c/vpp/+/45891>`_ [VECR 1]: quic: increase default fifo size to 512k
  | `45871 <https:////gerrit.fd.io/r/c/vpp/+/45871>`_ [VECR 7]: hs-test: filter memory leak report noise
  | `45707 <https:////gerrit.fd.io/r/c/vpp/+/45707>`_ [VECR 24]: npol: wire npol into the cnat slow-path hook mechanism

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

bonding: **Steven Luong** <sluong@cisco.com>
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 3]: ip bonding hash: inner-aware flow hash (opt-in)

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `45684 <https:////gerrit.fd.io/r/c/vpp/+/45684>`_ [VECr 22]: buffers: return values; improve debug

build: **Damjan Marion** <damarion@cisco.com>
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 14]: api: add build-time python stub generation via vppapigen

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [VECr 0]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get
  | `45882 <https:////gerrit.fd.io/r/c/vpp/+/45882>`_ [VECr 2]: cnat: guard snat policy APIs against NULL policy entry
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VECr 9]: cnat: add scope_id to session key

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 24]: crypto: add op tracing capability

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45674 <https:////gerrit.fd.io/r/c/vpp/+/45674>`_ [VECr 0]: dhcp: export DHCPv6 runtime state for PPPoE observability

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 3]: ip bonding hash: inner-aware flow hash (opt-in)
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 8]: sfdp: add sfdp-session-stats service
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VECr 9]: cnat: add scope_id to session key
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 16]: rdma: add mlx5 TSO support for raw packet tx
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VECr 17]: tcp: allow selective GRO enablement

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 0]: dpdk: log MFIB MAC replay tolerance at debug level
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [VECr 10]: dpdk: add support for represented port action
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VECr 16]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VECr 16]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VECr 17]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [VECr 17]: dpdk: multi-thread async flow offload with per-worker caches
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [VECr 17]: dpdk: support async flow offload
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 29]: flow: restructure vnet_flow_t for cache-line optimization
  | `45247 <https:////gerrit.fd.io/r/c/vpp/+/45247>`_ [VECr 29]: flow: encapsulate driver state into driver_data struct

fib: **Neale Ranns** <neale@graphiant.com>
  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VECr 28]: fib: IPv4 Route Query Command Crash

flow: **Damjan Marion** <damarion@cisco.com>
  | `45908 <https:////gerrit.fd.io/r/c/vpp/+/45908>`_ [VECr 1]: flow: add max parameter in 'show flow entry' CLI
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VECr 16]: flow: add flow aging support
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 16]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [VECr 16]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [VECr 24]: flow: add per-thread flow pool cache for multi-worker safety
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 29]: flow: add flow template and async range infrastructure
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 29]: flow: restructure vnet_flow_t for cache-line optimization
  | `45247 <https:////gerrit.fd.io/r/c/vpp/+/45247>`_ [VECr 29]: flow: encapsulate driver state into driver_data struct

gtpu: **Hongjun Ni** <hongjun.ni@intel.com>
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 29]: flow: restructure vnet_flow_t for cache-line optimization

hash: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 3]: ip bonding hash: inner-aware flow hash (opt-in)

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VECr 3]: vlib: fix process state format output wrapped by extra quotes
  | `45858 <https:////gerrit.fd.io/r/c/vpp/+/45858>`_ [VECr 10]: hsa: fix builtin echo cut-through
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VECr 15]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VECr 17]: tls: fix picotls partial record handling

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `45869 <https:////gerrit.fd.io/r/c/vpp/+/45869>`_ [VECr 2]: http: test h1 chunked put uploads
  | `45858 <https:////gerrit.fd.io/r/c/vpp/+/45858>`_ [VECr 10]: hsa: fix builtin echo cut-through

iavf: **Damjan Marion** <damarion@cisco.com>
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 7]: iavf: fix native TSO datapath

interface: **Dave Barach** <vpp@barachs.net>
  | `45850 <https:////gerrit.fd.io/r/c/vpp/+/45850>`_ [VECr 10]: interface: no-mfib table bind and create fixes
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 29]: flow: add flow template and async range infrastructure

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `45913 <https:////gerrit.fd.io/r/c/vpp/+/45913>`_ [VECr 0]: ip: fix data race of fragment ID
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 3]: ip bonding hash: inner-aware flow hash (opt-in)
  | `45884 <https:////gerrit.fd.io/r/c/vpp/+/45884>`_ [VECr 6]: ip: fix IGMPv3 MR validation and parsing with aux data
  | `45845 <https:////gerrit.fd.io/r/c/vpp/+/45845>`_ [VECr 10]: ip: fix using ICMPv4 & v6 packet generator with ICMP codes
  | `45847 <https:////gerrit.fd.io/r/c/vpp/+/45847>`_ [VECr 10]: ip: increment correct ACL error counters
  | `45850 <https:////gerrit.fd.io/r/c/vpp/+/45850>`_ [VECr 10]: interface: no-mfib table bind and create fixes
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 14]: ip: svr add bit indicating fragmentation to vnet_buffer

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 24]: crypto: add op tracing capability

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `45677 <https:////gerrit.fd.io/r/c/vpp/+/45677>`_ [VECr 0]: linux-cp: guard PPPOX interface type and tolerate missing neighbor

map: **Ole Troan** <otroan@employees.org>, **Jon Loeliger** <jdl@netgate.com>
  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VECr 30]: map: enhance map plugin to support per-vrf rules

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45876 <https:////gerrit.fd.io/r/c/vpp/+/45876>`_ [VECr 7]: gre: fix off-by-one error in TEIB sw_if_index checks
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 14]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 14]: api: add build-time python stub generation via vppapigen
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 24]: crypto: add op tracing capability
  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [VECr 28]: ip_validate: new plugin to drop packets with invalid addresses

mpls: **Neale Ranns** <neale@graphiant.com>
  | `45875 <https:////gerrit.fd.io/r/c/vpp/+/45875>`_ [VECr 7]: mpls: fix memory leak on mpls_tunnel_add_del API error

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VECr 14]: octeon: add PFC support
  | `45247 <https:////gerrit.fd.io/r/c/vpp/+/45247>`_ [VECr 29]: flow: encapsulate driver state into driver_data struct

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `45900 <https:////gerrit.fd.io/r/c/vpp/+/45900>`_ [VECr 1]: quic: quic_quicly tx improvement
  | `45857 <https:////gerrit.fd.io/r/c/vpp/+/45857>`_ [VECr 2]: quic: fix processing of coalesced packets
  | `45879 <https:////gerrit.fd.io/r/c/vpp/+/45879>`_ [VECr 2]: quic: optimize quic_quicly_udp_session_rx_packets
  | `45851 <https:////gerrit.fd.io/r/c/vpp/+/45851>`_ [VECr 2]: quic: quic_quicly_rx_packet_ctx_t decouple dgram

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [VECr 0]: rdma: steer PPPoE discovery and session flows
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 16]: rdma: add mlx5 TSO support for raw packet tx

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VECr 11]: sfdp: fix specification of scope_index
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [VECr 16]: sfdp: add verdict-testbench service
  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [VECr 17]: sfdp: async offload lookup

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 8]: sfdp: add sfdp-session-stats service
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [VECr 16]: sfdp: add verdict-testbench service
  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [VECr 17]: sfdp: async offload lookup

snort: **Damjan Marion** <damarion@cisco.com>
  | `45915 <https:////gerrit.fd.io/r/c/vpp/+/45915>`_ [VECr 0]: snort: fix wrong variable reference
  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VECr 7]: snort: don't store snort metadata in buffer

tcp: **Florin Coras** <fcoras@cisco.com>
  | `45881 <https:////gerrit.fd.io/r/c/vpp/+/45881>`_ [VECr 7]: tcp: avoid empty buffers for unsent segments
  | `45775 <https:////gerrit.fd.io/r/c/vpp/+/45775>`_ [VECr 17]: tcp: fix pure ACK incorrectly chained as GRO candidate
  | `45759 <https:////gerrit.fd.io/r/c/vpp/+/45759>`_ [VECr 17]: tcp: support chained buffers in GRO
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VECr 17]: tcp: allow selective GRO enablement

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45913 <https:////gerrit.fd.io/r/c/vpp/+/45913>`_ [VECr 0]: ip: fix data race of fragment ID
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 3]: ip bonding hash: inner-aware flow hash (opt-in)
  | `45884 <https:////gerrit.fd.io/r/c/vpp/+/45884>`_ [VECr 6]: ip: fix IGMPv3 MR validation and parsing with aux data
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 8]: sfdp: add sfdp-session-stats service
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VECr 9]: cnat: add scope_id to session key
  | `45847 <https:////gerrit.fd.io/r/c/vpp/+/45847>`_ [VECr 10]: ip: increment correct ACL error counters
  | `45850 <https:////gerrit.fd.io/r/c/vpp/+/45850>`_ [VECr 10]: interface: no-mfib table bind and create fixes
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VECr 11]: sfdp: fix specification of scope_index
  | `45837 <https:////gerrit.fd.io/r/c/vpp/+/45837>`_ [VECr 15]: tests: add suffix to failed_test file
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VECr 15]: tls: add ALPN negotiation support
  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VECr 30]: map: enhance map plugin to support per-vrf rules

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 2]: tls: propagate verify config for dtls
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VECr 15]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VECr 17]: tls: fix picotls partial record handling

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VECr 3]: vlib: fix process state format output wrapped by extra quotes

vpp: **Dave Barach** <vpp@barachs.net>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 8]: sfdp: add sfdp-session-stats service

vppapigen: **Ole Troan** <otroan@employees.org>
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 14]: api: add build-time python stub generation via vppapigen
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VECr 28]: vppapigen: fix inconsistency in paths JSON

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VECr 2]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer
  | `45852 <https:////gerrit.fd.io/r/c/vpp/+/45852>`_ [VECr 7]: vppinfra: error for out of range integer during unformat
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [VECr 17]: dpdk: support async flow offload

vxlan: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 29]: flow: restructure vnet_flow_t for cache-line optimization

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akos Orban** <orbanakos2001@gmail.com>:

  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 94]: cnat: fix show cnat translation for specific translation id
  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 94]: cnat: fix show cnat client showing invalid for client id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 59]: vhost: fix rxvq interrupts triggered because of race

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 128]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [VeC 156]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Aritra Basu** <aritrbas@cisco.com>:

  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [VEc 3]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VeC 38]: vlib: fix trace flag loss when multiple pending frames share next frame
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VeC 42]: interface: enable IPv6 link state on unnumbered interfaces
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 70]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 72]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 72]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 72]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 72]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 78]: ip6-nd: fix unicast NA handling in ND proxy

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 156]: pnat: do not disable pnat on rule deletion

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [vEC 28]: ikev2: add Curve25519 and Curve448 DH groups

**Dave Wallace** <dwallacelf@gmail.com>:

  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [vEC 2]: misc: patch to test CI infra

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 74]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 74]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [VEc 23]: dpdk: tracing improvements

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `45564 <https:////gerrit.fd.io/r/c/vpp/+/45564>`_ [Vec 31]: sfdp: add api enum for timeouts
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [Vec 95]: sfdp: modify tenant_index type from u16 to u32
  | `44474 <https:////gerrit.fd.io/r/c/vpp/+/44474>`_ [Vec 142]: sasc: fix tenant_index overlap in sasc_buffer

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `45696 <https:////gerrit.fd.io/r/c/vpp/+/45696>`_ [VEc 0]: cnat: make cnat pluggable

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 64]: tests: reduce sleep interval in ip-neighbor age test
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 93]: crypto: unify per-thread key_data allocation

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 112]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 112]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 112]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 112]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 31]: virtio: add native plugin L2 xconnect test with QEMU
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VeC 32]: af_xdp: add support for multi-buffer

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 114]: vppapigen: fix json build error

**Justin Thomas** <justin@jdt.io>:

  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VeC 56]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VeC 56]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

**Klement Sekera** <ksekera@netgate.com>:

  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VeC 37]: vppinfra: add cast to prevent warning

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [VEc 1]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route
  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [VEc 2]: ipip: add mp2p ipip tunnel

**Matthew Smith** <mgsmith@netgate.com>:

  | `45732 <https:////gerrit.fd.io/r/c/vpp/+/45732>`_ [VEc 0]: fib: omit mac addr add/del when not supported

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [vEc 0]: flow: single-interface-per-flow model
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VeC 67]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VeC 67]: gso: implement IPv6 extension header traversal
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 73]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 73]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 73]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 73]: policer: reject deletion of policer used by punt policing

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [vEC 7]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 170]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VeC 52]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 72]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 78]: sfdp: add blacklist/whitelist to snort service
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 101]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 105]: pg: Guard against non‑monotonic time and negative accumulator
  | `44426 <https:////gerrit.fd.io/r/c/vpp/+/44426>`_ [VeC 140]: virtio: add the check if MAC feature is negotiated

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 118]: iouring: Add io_uring plugin to allow polling usage of io_uring

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 51]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 51]: ip6-nd: add nd-proxy all dst
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 59]: ip6: fix show ip6-ll cli if selector
  | `44903 <https:////gerrit.fd.io/r/c/vpp/+/44903>`_ [VeC 95]: vxlan: reset next_dpo on delete
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 100]: ip6-nd: support RA pfx info option with flag L&!A

**Ole Troan** <otroan@employees.org>:

  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [Vec 44]: papi: improve performance on set_errors

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 119]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 121]: fix: correct fixstyle in session_sdl command function

**Pim van Pelt** <pim@ipng.nl>:

  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VeC 51]: lb: Add punt feature to per-port VIPs

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [VEc 2]: pfc: add framework for priority flow control

**Samuel Benko** <sbenko@cisco.com>:

  | `45766 <https:////gerrit.fd.io/r/c/vpp/+/45766>`_ [vEC 2]: hs-test: add dtls crl reject allow test

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [veC 59]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [VeC 154]: linux-cp: fix cleanup of special routes
  | `44241 <https:////gerrit.fd.io/r/c/vpp/+/44241>`_ [Vec 162]: linux-cp: on remove do cleanup for all fibs
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VeC 177]: fib: dump by src not only contributing routes

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [VEc 11]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [veC 59]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44575 <https:////gerrit.fd.io/r/c/vpp/+/44575>`_ [VeC 140]: fib: add interface-rx dpo mpls support
  | `44574 <https:////gerrit.fd.io/r/c/vpp/+/44574>`_ [VeC 140]: fib: fix stale interface-rx dpo fib after deag/lookup
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 140]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 140]: nat: speedup nat44-ed vrf table lookups
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 140]: nat: fix nat44-ed address removal from fib
  | `44563 <https:////gerrit.fd.io/r/c/vpp/+/44563>`_ [veC 141]: ip: fix DSCP CS7 value
  | `44568 <https:////gerrit.fd.io/r/c/vpp/+/44568>`_ [VeC 141]: vxlan: add default dscp value config for vxlan encap
  | `44567 <https:////gerrit.fd.io/r/c/vpp/+/44567>`_ [VeC 141]: udp: add default dscp value config for udp encap
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 141]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 141]: fib: fix udp encap mp-safe ops and id validation
  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 141]: fib: avoid loadbalance dpo node path polarisation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 141]: vlib: mark cli quit command as mp_safe

**Vratko Polak** <vrpolak@cisco.com>:

  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vEc 0]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [veC 44]: empty change for GHA(CSIT) testing

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 156]: ip-neighbor: ARP/NA per-interface counter improvements

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [VEc 2]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [vEC 3]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vEc 9]: vlib: pre-input node should be dispatched before input node

**echo** <614699596@qq.com>:

  | `45348 <https:////gerrit.fd.io/r/c/vpp/+/45348>`_ [VeC 63]: bpf_trace_filter: fix bpf_expr memory leak on error path

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 108]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [vEC 18]: vlib: fix '\' command input will causes memory out of bounds
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [Vec 59]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [Vec 59]: dns: support ipv6 server to resolve name
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VeC 60]: build rpm-packaging: make vpp rpm package for kylinV11
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 113]: docs: Python apis examples

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 32]: fib: compute fib entry flags from full path list

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 71]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 59]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [veC 59]: lb: fix API byte order and IPv4 prefix length handling
  | `44207 <https:////gerrit.fd.io/r/c/vpp/+/44207>`_ [VeC 153]: lb: fix incorrect byte order conversion for vip port display

**steven luong** <sluong@cisco.com>:

  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [VEc 18]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [VEc 24]: session: make transport to use application's segment manager
  | `44569 <https:////gerrit.fd.io/r/c/vpp/+/44569>`_ [VeC 141]: vppinfra: clib_time_verify_frequency may cause time jump

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 123]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 123]: l2: fix null pointer access in l2-efp-filter

**yewtow** <offside.items03@icloud.com>:

  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VeC 46]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VeC 47]: ip6-nd: support RDNSS option in IPv6 RA

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
authors          109
maintainers      64
committers       4
abandoned        0
================ ===

