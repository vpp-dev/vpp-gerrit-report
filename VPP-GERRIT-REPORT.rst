
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Wednesday 2026-06-03, 06:16:12
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

  | `45846 <https:////gerrit.fd.io/r/c/vpp/+/45846>`_ [VECR 5]: quic: skip setting of ip and port in dgram hdr
  | `45891 <https:////gerrit.fd.io/r/c/vpp/+/45891>`_ [VECR 5]: quic: increase default fifo size to 512k
  | `45871 <https:////gerrit.fd.io/r/c/vpp/+/45871>`_ [VECR 11]: hs-test: filter memory leak report noise
  | `45707 <https:////gerrit.fd.io/r/c/vpp/+/45707>`_ [VECR 28]: npol: wire npol into the cnat slow-path hook mechanism

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

bonding: **Steven Luong** <sluong@cisco.com>
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 7]: ip bonding hash: inner-aware flow hash (opt-in)

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `45684 <https:////gerrit.fd.io/r/c/vpp/+/45684>`_ [VECr 26]: buffers: return values; improve debug

build: **Damjan Marion** <damarion@cisco.com>
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 18]: api: add build-time python stub generation via vppapigen

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `45882 <https:////gerrit.fd.io/r/c/vpp/+/45882>`_ [VECr 1]: cnat: guard snat policy APIs against NULL policy entry
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VECr 13]: cnat: add scope_id to session key

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 28]: crypto: add op tracing capability

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45674 <https:////gerrit.fd.io/r/c/vpp/+/45674>`_ [VECr 4]: dhcp: export DHCPv6 runtime state for PPPoE observability

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45916 <https:////gerrit.fd.io/r/c/vpp/+/45916>`_ [VECr 0]: sfdp_services: configurable non-syn fsol behavior
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 4]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 7]: ip bonding hash: inner-aware flow hash (opt-in)
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 12]: sfdp: add sfdp-session-stats service
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VECr 13]: cnat: add scope_id to session key
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 20]: rdma: add mlx5 TSO support for raw packet tx
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VECr 21]: tcp: allow selective GRO enablement

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [VECr 0]: dpdk: add support for represented port action
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VECr 0]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [VECr 0]: dpdk: support async flow offload
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 0]: flow: restructure vnet_flow_t for cache-line optimization
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 4]: dpdk: log MFIB MAC replay tolerance at debug level
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VECr 20]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VECr 20]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [VECr 21]: dpdk: multi-thread async flow offload with per-worker caches

flow: **Damjan Marion** <damarion@cisco.com>
  | `45908 <https:////gerrit.fd.io/r/c/vpp/+/45908>`_ [VECr 0]: flow: add max parameter in 'show flow entry' CLI
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 0]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 0]: flow: restructure vnet_flow_t for cache-line optimization
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VECr 20]: flow: add flow aging support
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [VECr 20]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT

gtpu: **Hongjun Ni** <hongjun.ni@intel.com>
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 0]: flow: restructure vnet_flow_t for cache-line optimization

hash: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 7]: ip bonding hash: inner-aware flow hash (opt-in)

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VECr 8]: vlib: fix process state format output wrapped by extra quotes
  | `45858 <https:////gerrit.fd.io/r/c/vpp/+/45858>`_ [VECr 14]: hsa: fix builtin echo cut-through
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VECr 19]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VECr 21]: tls: fix picotls partial record handling

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `45869 <https:////gerrit.fd.io/r/c/vpp/+/45869>`_ [VECr 6]: http: test h1 chunked put uploads
  | `45858 <https:////gerrit.fd.io/r/c/vpp/+/45858>`_ [VECr 14]: hsa: fix builtin echo cut-through

iavf: **Damjan Marion** <damarion@cisco.com>
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 11]: iavf: fix native TSO datapath

interface: **Dave Barach** <vpp@barachs.net>
  | `45850 <https:////gerrit.fd.io/r/c/vpp/+/45850>`_ [VECr 14]: interface: no-mfib table bind and create fixes

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `45913 <https:////gerrit.fd.io/r/c/vpp/+/45913>`_ [VECr 4]: ip: fix data race of fragment ID
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 7]: ip bonding hash: inner-aware flow hash (opt-in)
  | `45884 <https:////gerrit.fd.io/r/c/vpp/+/45884>`_ [VECr 10]: ip: fix IGMPv3 MR validation and parsing with aux data
  | `45845 <https:////gerrit.fd.io/r/c/vpp/+/45845>`_ [VECr 14]: ip: fix using ICMPv4 & v6 packet generator with ICMP codes
  | `45847 <https:////gerrit.fd.io/r/c/vpp/+/45847>`_ [VECr 14]: ip: increment correct ACL error counters
  | `45850 <https:////gerrit.fd.io/r/c/vpp/+/45850>`_ [VECr 14]: interface: no-mfib table bind and create fixes
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 18]: ip: svr add bit indicating fragmentation to vnet_buffer

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 28]: crypto: add op tracing capability

kube-test: **Florin Coras** <fcoras@cisco.com>
  | `45951 <https:////gerrit.fd.io/r/c/vpp/+/45951>`_ [VECr 0]: kube-test: bound kubectl rollout status to avoid 30m hangs

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `45677 <https:////gerrit.fd.io/r/c/vpp/+/45677>`_ [VECr 1]: linux-cp: guard PPPOX interface type and tolerate missing neighbor

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45950 <https:////gerrit.fd.io/r/c/vpp/+/45950>`_ [VECr 0]: misc: fix checkstyle for clang-format 19
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 4]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45876 <https:////gerrit.fd.io/r/c/vpp/+/45876>`_ [VECr 11]: gre: fix off-by-one error in TEIB sw_if_index checks
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 18]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 18]: api: add build-time python stub generation via vppapigen
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 28]: crypto: add op tracing capability

mpls: **Neale Ranns** <neale@graphiant.com>
  | `45875 <https:////gerrit.fd.io/r/c/vpp/+/45875>`_ [VECr 11]: mpls: fix memory leak on mpls_tunnel_add_del API error

mss_clamp: **Miklos Tirpak** <miklos.tirpak@emnify.com>
  | `45948 <https:////gerrit.fd.io/r/c/vpp/+/45948>`_ [VECr 0]: mss_clamp: fix missing TCP header length validations

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VECr 18]: octeon: add PFC support

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `45900 <https:////gerrit.fd.io/r/c/vpp/+/45900>`_ [VECr 5]: quic: quic_quicly tx improvement
  | `45857 <https:////gerrit.fd.io/r/c/vpp/+/45857>`_ [VECr 6]: quic: fix processing of coalesced packets
  | `45879 <https:////gerrit.fd.io/r/c/vpp/+/45879>`_ [VECr 6]: quic: optimize quic_quicly_udp_session_rx_packets
  | `45851 <https:////gerrit.fd.io/r/c/vpp/+/45851>`_ [VECr 6]: quic: quic_quicly_rx_packet_ctx_t decouple dgram

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [VECr 4]: rdma: steer PPPoE discovery and session flows
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 20]: rdma: add mlx5 TSO support for raw packet tx

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VECr 15]: sfdp: fix specification of scope_index
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [VECr 20]: sfdp: add verdict-testbench service

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `45916 <https:////gerrit.fd.io/r/c/vpp/+/45916>`_ [VECr 0]: sfdp_services: configurable non-syn fsol behavior
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 12]: sfdp: add sfdp-session-stats service
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [VECr 20]: sfdp: add verdict-testbench service

snort: **Damjan Marion** <damarion@cisco.com>
  | `45915 <https:////gerrit.fd.io/r/c/vpp/+/45915>`_ [VECr 4]: snort: fix wrong variable reference
  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VECr 11]: snort: don't store snort metadata in buffer

tcp: **Florin Coras** <fcoras@cisco.com>
  | `45948 <https:////gerrit.fd.io/r/c/vpp/+/45948>`_ [VECr 0]: mss_clamp: fix missing TCP header length validations
  | `45881 <https:////gerrit.fd.io/r/c/vpp/+/45881>`_ [VECr 11]: tcp: avoid empty buffers for unsent segments
  | `45775 <https:////gerrit.fd.io/r/c/vpp/+/45775>`_ [VECr 21]: tcp: fix pure ACK incorrectly chained as GRO candidate
  | `45759 <https:////gerrit.fd.io/r/c/vpp/+/45759>`_ [VECr 21]: tcp: support chained buffers in GRO
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VECr 21]: tcp: allow selective GRO enablement

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `45948 <https:////gerrit.fd.io/r/c/vpp/+/45948>`_ [VECr 0]: mss_clamp: fix missing TCP header length validations
  | `45916 <https:////gerrit.fd.io/r/c/vpp/+/45916>`_ [VECr 0]: sfdp_services: configurable non-syn fsol behavior
  | `45937 <https:////gerrit.fd.io/r/c/vpp/+/45937>`_ [VECr 1]: tracepath: add api to dump trace paths
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 4]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45913 <https:////gerrit.fd.io/r/c/vpp/+/45913>`_ [VECr 4]: ip: fix data race of fragment ID
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 7]: ip bonding hash: inner-aware flow hash (opt-in)
  | `45884 <https:////gerrit.fd.io/r/c/vpp/+/45884>`_ [VECr 10]: ip: fix IGMPv3 MR validation and parsing with aux data
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 12]: sfdp: add sfdp-session-stats service
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VECr 13]: cnat: add scope_id to session key
  | `45847 <https:////gerrit.fd.io/r/c/vpp/+/45847>`_ [VECr 14]: ip: increment correct ACL error counters
  | `45850 <https:////gerrit.fd.io/r/c/vpp/+/45850>`_ [VECr 14]: interface: no-mfib table bind and create fixes
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VECr 15]: sfdp: fix specification of scope_index
  | `45837 <https:////gerrit.fd.io/r/c/vpp/+/45837>`_ [VECr 19]: tests: add suffix to failed_test file
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VECr 19]: tls: add ALPN negotiation support

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 6]: tls: propagate verify config for dtls
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VECr 19]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VECr 21]: tls: fix picotls partial record handling

tracepath: **Hadi Rayan Al-Sandid** <halsandi@cisco.com>
  | `45937 <https:////gerrit.fd.io/r/c/vpp/+/45937>`_ [VECr 1]: tracepath: add api to dump trace paths

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VECr 8]: vlib: fix process state format output wrapped by extra quotes

vpp: **Dave Barach** <vpp@barachs.net>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 4]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 12]: sfdp: add sfdp-session-stats service

vppapigen: **Ole Troan** <otroan@employees.org>
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VECr 18]: api: add build-time python stub generation via vppapigen

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [VECr 0]: dpdk: support async flow offload
  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VECr 6]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer
  | `45852 <https:////gerrit.fd.io/r/c/vpp/+/45852>`_ [VECr 11]: vppinfra: error for out of range integer during unformat

vxlan: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 0]: flow: restructure vnet_flow_t for cache-line optimization

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [VeC 32]: ip_validate: new plugin to drop packets with invalid addresses

**Akos Orban** <orbanakos2001@gmail.com>:

  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 98]: cnat: fix show cnat translation for specific translation id
  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 98]: cnat: fix show cnat client showing invalid for client id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 63]: vhost: fix rxvq interrupts triggered because of race

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 132]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VeC 34]: map: enhance map plugin to support per-vrf rules

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [VeC 160]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Aritra Basu** <aritrbas@cisco.com>:

  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [VEc 1]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VeC 42]: vlib: fix trace flag loss when multiple pending frames share next frame
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VeC 46]: interface: enable IPv6 link state on unnumbered interfaces
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 74]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 76]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 76]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 76]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 76]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 82]: ip6-nd: fix unicast NA handling in ND proxy

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 160]: pnat: do not disable pnat on rule deletion

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [vEC 1]: ikev2: add Curve25519 and Curve448 DH groups

**Dave Wallace** <dwallacelf@gmail.com>:

  | `45874 <https:////gerrit.fd.io/r/c/vpp/+/45874>`_ [vEC 0]: vrrp: fix heap buffer overflow in packet trace path
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [vEC 0]: misc: patch to test CI infra
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [vEC 6]: misc: patch to test CI infra

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 78]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 78]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [VEc 27]: dpdk: tracing improvements

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `45564 <https:////gerrit.fd.io/r/c/vpp/+/45564>`_ [Vec 35]: sfdp: add api enum for timeouts
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [Vec 99]: sfdp: modify tenant_index type from u16 to u32
  | `44474 <https:////gerrit.fd.io/r/c/vpp/+/44474>`_ [Vec 146]: sasc: fix tenant_index overlap in sasc_buffer

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [VEc 1]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get
  | `45696 <https:////gerrit.fd.io/r/c/vpp/+/45696>`_ [VEc 4]: cnat: make cnat pluggable

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 68]: tests: reduce sleep interval in ip-neighbor age test
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 97]: crypto: unify per-thread key_data allocation

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 116]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 116]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 116]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 116]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 35]: virtio: add native plugin L2 xconnect test with QEMU
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VeC 36]: af_xdp: add support for multi-buffer

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 118]: vppapigen: fix json build error

**Justin Thomas** <justin@jdt.io>:

  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VeC 60]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VeC 60]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

**Klement Sekera** <ksekera@netgate.com>:

  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VeC 41]: vppinfra: add cast to prevent warning

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [VEc 5]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route
  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [VEc 6]: ipip: add mp2p ipip tunnel

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45247 <https:////gerrit.fd.io/r/c/vpp/+/45247>`_ [vEC 0]: flow: encapsulate driver state into driver_data struct
  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [VEc 0]: flow: add per-thread flow pool cache for multi-worker safety
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VEc 0]: flow: add flow template and async range infrastructure
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VeC 71]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VeC 71]: gso: implement IPv6 extension header traversal
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 77]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 77]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 77]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 77]: policer: reject deletion of policer used by punt policing

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [vEC 11]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 174]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VeC 56]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 76]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 82]: sfdp: add blacklist/whitelist to snort service
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 105]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 109]: pg: Guard against non‑monotonic time and negative accumulator
  | `44426 <https:////gerrit.fd.io/r/c/vpp/+/44426>`_ [VeC 144]: virtio: add the check if MAC feature is negotiated

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 122]: iouring: Add io_uring plugin to allow polling usage of io_uring

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 55]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 55]: ip6-nd: add nd-proxy all dst
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 63]: ip6: fix show ip6-ll cli if selector
  | `44903 <https:////gerrit.fd.io/r/c/vpp/+/44903>`_ [VeC 99]: vxlan: reset next_dpo on delete
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 104]: ip6-nd: support RA pfx info option with flag L&!A

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [VEc 0]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [Vec 48]: papi: improve performance on set_errors

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 124]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 125]: fix: correct fixstyle in session_sdl command function

**Pim van Pelt** <pim@ipng.nl>:

  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VeC 55]: lb: Add punt feature to per-port VIPs

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [VEc 6]: pfc: add framework for priority flow control

**Robert Shearman** <robertshearman@gmail.com>:

  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VeC 32]: vppapigen: fix inconsistency in paths JSON

**Samuel Benko** <sbenko@cisco.com>:

  | `45766 <https:////gerrit.fd.io/r/c/vpp/+/45766>`_ [vEC 6]: hs-test: add dtls crl reject allow test

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `45917 <https:////gerrit.fd.io/r/c/vpp/+/45917>`_ [VEc 0]: linux-cp: mcast ospf test
  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [veC 63]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [VeC 158]: linux-cp: fix cleanup of special routes
  | `44241 <https:////gerrit.fd.io/r/c/vpp/+/44241>`_ [Vec 166]: linux-cp: on remove do cleanup for all fibs

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [VEc 15]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [veC 63]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44575 <https:////gerrit.fd.io/r/c/vpp/+/44575>`_ [VeC 144]: fib: add interface-rx dpo mpls support
  | `44574 <https:////gerrit.fd.io/r/c/vpp/+/44574>`_ [VeC 144]: fib: fix stale interface-rx dpo fib after deag/lookup
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 144]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 144]: nat: speedup nat44-ed vrf table lookups
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 144]: nat: fix nat44-ed address removal from fib
  | `44563 <https:////gerrit.fd.io/r/c/vpp/+/44563>`_ [veC 145]: ip: fix DSCP CS7 value
  | `44568 <https:////gerrit.fd.io/r/c/vpp/+/44568>`_ [VeC 145]: vxlan: add default dscp value config for vxlan encap
  | `44567 <https:////gerrit.fd.io/r/c/vpp/+/44567>`_ [VeC 145]: udp: add default dscp value config for udp encap
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 145]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 145]: fib: fix udp encap mp-safe ops and id validation
  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 145]: fib: avoid loadbalance dpo node path polarisation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 145]: vlib: mark cli quit command as mp_safe

**Vratko Polak** <vrpolak@cisco.com>:

  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vEc 4]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [veC 48]: empty change for GHA(CSIT) testing

**Wayne Morrison** <wmorrison@netgate.com>:

  | `45949 <https:////gerrit.fd.io/r/c/vpp/+/45949>`_ [vEC 0]: lldp: extend data returned by lldp-dump API

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 160]: ip-neighbor: ARP/NA per-interface counter improvements

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [VEc 6]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [vEC 7]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vEc 13]: vlib: pre-input node should be dispatched before input node

**echo** <614699596@qq.com>:

  | `45348 <https:////gerrit.fd.io/r/c/vpp/+/45348>`_ [VeC 68]: bpf_trace_filter: fix bpf_expr memory leak on error path

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 112]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [vEC 22]: vlib: fix '\' command input will causes memory out of bounds
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [Vec 63]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [Vec 63]: dns: support ipv6 server to resolve name
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VeC 64]: build rpm-packaging: make vpp rpm package for kylinV11
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 117]: docs: Python apis examples

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 37]: fib: compute fib entry flags from full path list

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 75]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 63]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [veC 63]: lb: fix API byte order and IPv4 prefix length handling
  | `44207 <https:////gerrit.fd.io/r/c/vpp/+/44207>`_ [VeC 157]: lb: fix incorrect byte order conversion for vip port display

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VeC 32]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [VEc 22]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [VEc 28]: session: make transport to use application's segment manager
  | `44569 <https:////gerrit.fd.io/r/c/vpp/+/44569>`_ [VeC 145]: vppinfra: clib_time_verify_frequency may cause time jump

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 127]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 127]: l2: fix null pointer access in l2-efp-filter

**yewtow** <offside.items03@icloud.com>:

  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VeC 50]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VeC 51]: ip6-nd: support RDNSS option in IPv6 RA

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
authors          119
maintainers      60
committers       4
abandoned        0
================ ===

