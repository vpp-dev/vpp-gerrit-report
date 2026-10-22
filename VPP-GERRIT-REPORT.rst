
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Thursday 2026-10-22, 06:05:28
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

  | `47221 <https:////gerrit.fd.io/r/c/vpp/+/47221>`_ [VECR 0]: hs-test: echo the picotls transfer test
  | `47218 <https:////gerrit.fd.io/r/c/vpp/+/47218>`_ [VECR 0]: vperf: count only payload in uso test-bytes tx

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `47169 <https:////gerrit.fd.io/r/c/vpp/+/47169>`_ [VECr 5]: acl: export acl_add_list
  | `47064 <https:////gerrit.fd.io/r/c/vpp/+/47064>`_ [VECr 5]: acl: add a match check callback to the lookup
  | `47058 <https:////gerrit.fd.io/r/c/vpp/+/47058>`_ [VECr 5]: acl: stop counting hash hits in a shared per-entry field

af_packet: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `47190 <https:////gerrit.fd.io/r/c/vpp/+/47190>`_ [VECr 0]: af_packet: preserve VLAN TPID when restoring stripped tags

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `47106 <https:////gerrit.fd.io/r/c/vpp/+/47106>`_ [VECr 5]: vnet: rewrite nodes to check available headroom

build: **Damjan Marion** <damarion@cisco.com>
  | `46291 <https:////gerrit.fd.io/r/c/vpp/+/46291>`_ [VECr 1]: build: add SPDK as an optional dependency
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 8]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `46753 <https:////gerrit.fd.io/r/c/vpp/+/46753>`_ [VECr 28]: cnat: prevent SNAT policy aliasing across FIBs

dev: **Damjan Marion** <damarion@cisco.com>
  | `47226 <https:////gerrit.fd.io/r/c/vpp/+/47226>`_ [VECr 0]: dev: move device counters to a separate show command
  | `47225 <https:////gerrit.fd.io/r/c/vpp/+/47225>`_ [VECr 0]: dev: use format_table for device counters

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

dispatch-trace: **Dave Barach** <vpp@barachs.net>
  | `46469 <https:////gerrit.fd.io/r/c/vpp/+/46469>`_ [VECr 0]: dispatch-trace: fix SIGSEGV on multi-worker handoff

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra
  | `46292 <https:////gerrit.fd.io/r/c/vpp/+/46292>`_ [VECr 1]: spdk: add in-process NVMe/TCP target plugin
  | `47112 <https:////gerrit.fd.io/r/c/vpp/+/47112>`_ [VECr 2]: ikev2 ipip: negotiate USE_TRANSPORT_MODE
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 8]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 8]: rdma: add mlx5 DV TSO support for raw packet tx
  | `46808 <https:////gerrit.fd.io/r/c/vpp/+/46808>`_ [VECr 16]: docs: announce libvnet visibility change
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VECr 16]: iavf: add setup documentation

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `47200 <https:////gerrit.fd.io/r/c/vpp/+/47200>`_ [VECr 1]: dpdk: fix clib file descriptor leak on admin down
  | `47213 <https:////gerrit.fd.io/r/c/vpp/+/47213>`_ [VECr 1]: dpdk: read transceiver EEPROM asynchronously, never under the barrier
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 3]: dpdk: log MFIB MAC replay tolerance at debug level
  | `46953 <https:////gerrit.fd.io/r/c/vpp/+/46953>`_ [VECr 12]: dpdk: recognise the the MANA VF as a bifurcated device
  | `46926 <https:////gerrit.fd.io/r/c/vpp/+/46926>`_ [VECr 16]: dpdk: fix QAT cryptodev AEAD sessions
  | `46939 <https:////gerrit.fd.io/r/c/vpp/+/46939>`_ [VECr 21]: dpdk: don't leak chained mbufs when multi-seg is disabled

dpdk-cryptodev: **Kai Ji** <kai.ji@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `46926 <https:////gerrit.fd.io/r/c/vpp/+/46926>`_ [VECr 16]: dpdk: fix QAT cryptodev AEAD sessions

feature: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)

fib: **Neale Ranns** <neale@graphiant.com>
  | `46959 <https:////gerrit.fd.io/r/c/vpp/+/46959>`_ [VECr 1]: linux-cp: free lcp_router_table if 0 routes and no lcp pairs only
  | `47076 <https:////gerrit.fd.io/r/c/vpp/+/47076>`_ [VECr 5]: fib: decide the glean source by the address it holds
  | `47078 <https:////gerrit.fd.io/r/c/vpp/+/47078>`_ [VECr 7]: fib: swap in the paths of a source new to the entry
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VECr 27]: fib: honor unnumbered RX interface in MFIB RPF check

flow: **Damjan Marion** <damarion@cisco.com>
  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [VECr 2]: flow: add per-thread flow pool cache for multi-worker safety

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `47182 <https:////gerrit.fd.io/r/c/vpp/+/47182>`_ [VECr 0]: http_static: Advertise h3 support via Alt-Svc header in h1 and h2
  | `47171 <https:////gerrit.fd.io/r/c/vpp/+/47171>`_ [VECr 1]: tcp: count only acks with new sack data as dupacks

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `46723 <https:////gerrit.fd.io/r/c/vpp/+/46723>`_ [VECr 29]: hsi: wake drains when ownership changes

hsi: **Florin Coras** <fcoras@cisco.com>
  | `47026 <https:////gerrit.fd.io/r/c/vpp/+/47026>`_ [VECr 1]: hsi: expose hsi API functions for re-use
  | `46723 <https:////gerrit.fd.io/r/c/vpp/+/46723>`_ [VECr 29]: hsi: wake drains when ownership changes

http: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `47182 <https:////gerrit.fd.io/r/c/vpp/+/47182>`_ [VECr 0]: http_static: Advertise h3 support via Alt-Svc header in h1 and h2

http_static: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `47182 <https:////gerrit.fd.io/r/c/vpp/+/47182>`_ [VECr 0]: http_static: Advertise h3 support via Alt-Svc header in h1 and h2

iavf: **Damjan Marion** <damarion@cisco.com>
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VECr 16]: iavf: add setup documentation
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 25]: iavf: fix native TSO datapath

igmp: **Neale Ranns** <neale@graphiant.com>
  | `47021 <https:////gerrit.fd.io/r/c/vpp/+/47021>`_ [VECr 9]: igmp: set proxy mfib Accept on host and Forward on router

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `47214 <https:////gerrit.fd.io/r/c/vpp/+/47214>`_ [VECr 1]: ikev2: configure inbound ESP replay window
  | `47194 <https:////gerrit.fd.io/r/c/vpp/+/47194>`_ [VECr 1]: ikev2: allocate Child SA IDs without collision
  | `47112 <https:////gerrit.fd.io/r/c/vpp/+/47112>`_ [VECr 2]: ikev2 ipip: negotiate USE_TRANSPORT_MODE
  | `47186 <https:////gerrit.fd.io/r/c/vpp/+/47186>`_ [VECr 2]: ikev2: guard SA formatting without a profile
  | `47187 <https:////gerrit.fd.io/r/c/vpp/+/47187>`_ [VECr 2]: ikev2: clean up locally when delete encoding fails
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)

interface: **Dave Barach** <vpp@barachs.net>
  | `47175 <https:////gerrit.fd.io/r/c/vpp/+/47175>`_ [VECr 0]: interface: fix punt drop feature arc
  | `47213 <https:////gerrit.fd.io/r/c/vpp/+/47213>`_ [VECr 1]: dpdk: read transceiver EEPROM asynchronously, never under the barrier
  | `46749 <https:////gerrit.fd.io/r/c/vpp/+/46749>`_ [VECr 1]: pppoeclient: fix orphan TX nodes and shared rename
  | `46651 <https:////gerrit.fd.io/r/c/vpp/+/46651>`_ [VECr 3]: vnet: keep deleted interface node names unique

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 19]: ip6: fix Pad1 off-by-one in hop-by-hop option pars

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `47102 <https:////gerrit.fd.io/r/c/vpp/+/47102>`_ [VECr 0]: ip6-nd: do not learn an NA for one of our own addresses
  | `47177 <https:////gerrit.fd.io/r/c/vpp/+/47177>`_ [VECr 2]: ip: parse the output-arc IPv6 header in sv-reass update
  | `47172 <https:////gerrit.fd.io/r/c/vpp/+/47172>`_ [VECr 4]: ip: clear l4_hdr_truncated bit in ip4 sv-reass
  | `47173 <https:////gerrit.fd.io/r/c/vpp/+/47173>`_ [VECr 4]: ip: tolerate a NULL total_ip_payload_length in sv-reass lock
  | `47106 <https:////gerrit.fd.io/r/c/vpp/+/47106>`_ [VECr 5]: vnet: rewrite nodes to check available headroom
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 19]: ip6: fix Pad1 off-by-one in hop-by-hop option pars
  | `46920 <https:////gerrit.fd.io/r/c/vpp/+/46920>`_ [VECr 22]: ip: stop forwarding the Ethernet trailer
  | `46051 <https:////gerrit.fd.io/r/c/vpp/+/46051>`_ [VECr 29]: ip: fix punt socket rx when multiple FDs are ready
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [VECr 29]: ip: fix adjacent packet overwrite with ip6 frags
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VECr 29]: ip: fix adjacent packet overwrite with ip frags
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VECr 29]: ip: fix ip mroute bulk insertion CLI for certain inputs

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `47102 <https:////gerrit.fd.io/r/c/vpp/+/47102>`_ [VECr 0]: ip6-nd: do not learn an NA for one of our own addresses
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VECr 22]: ip6-nd: enforce on-link source validation for RS neighbor learning

ipip: **Ole Troan** <otroan@employees.org>
  | `47112 <https:////gerrit.fd.io/r/c/vpp/+/47112>`_ [VECr 2]: ikev2 ipip: negotiate USE_TRANSPORT_MODE

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `47191 <https:////gerrit.fd.io/r/c/vpp/+/47191>`_ [VECr 0]: l2: report flushed MACs refreshed by traffic

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `46526 <https:////gerrit.fd.io/r/c/vpp/+/46526>`_ [VECr 16]: lb: fix NAT66 UDP/IPv6 checksum zero-fold
  | `46901 <https:////gerrit.fd.io/r/c/vpp/+/46901>`_ [VECr 22]: lb: prefetch sticky buckets four packets ahead

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `46959 <https:////gerrit.fd.io/r/c/vpp/+/46959>`_ [VECr 1]: linux-cp: free lcp_router_table if 0 routes and no lcp pairs only
  | `46492 <https:////gerrit.fd.io/r/c/vpp/+/46492>`_ [VECr 2]: linux-cp: don't copy an unknown link speed to the host tap
  | `47120 <https:////gerrit.fd.io/r/c/vpp/+/47120>`_ [VECr 2]: linux-cp: do not unlock an mfib for MPLS tables
  | `47001 <https:////gerrit.fd.io/r/c/vpp/+/47001>`_ [VECr 5]: linux-cp: add qinq linux to vpp support
  | `46937 <https:////gerrit.fd.io/r/c/vpp/+/46937>`_ [VECr 21]: linux-cp: only drop a table reference for routes lcp installed

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `47202 <https:////gerrit.fd.io/r/c/vpp/+/47202>`_ [VECr 0]: vppinfra: add foreach_clib_dt_property_string macro
  | `46292 <https:////gerrit.fd.io/r/c/vpp/+/46292>`_ [VECr 1]: spdk: add in-process NVMe/TCP target plugin
  | `46749 <https:////gerrit.fd.io/r/c/vpp/+/46749>`_ [VECr 1]: pppoeclient: fix orphan TX nodes and shared rename
  | `46991 <https:////gerrit.fd.io/r/c/vpp/+/46991>`_ [VECr 3]: pppoeclient: echo relay tag and accept PADS without AC-Cookie
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46992 <https:////gerrit.fd.io/r/c/vpp/+/46992>`_ [VECr 3]: pppoeclient: keep control-plane work off workers and pin session VLAN
  | `46993 <https:////gerrit.fd.io/r/c/vpp/+/46993>`_ [VECr 3]: pppoeclient: bind the learned VLAN on the main thread
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 8]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `46927 <https:////gerrit.fd.io/r/c/vpp/+/46927>`_ [VECr 21]: crypto: fix fixed-tag AEAD validation
  | `46442 <https:////gerrit.fd.io/r/c/vpp/+/46442>`_ [VECr 26]: vnet: install missing vnet headers

mpls: **Neale Ranns** <neale@graphiant.com>
  | `47106 <https:////gerrit.fd.io/r/c/vpp/+/47106>`_ [VECr 5]: vnet: rewrite nodes to check available headroom

mss_clamp: **Miklos Tirpak** <miklos.tirpak@emnify.com>
  | `47217 <https:////gerrit.fd.io/r/c/vpp/+/47217>`_ [VECr 0]: mss_clamp: fix IPv4 vector MSS interface

nat: **Ole Troan** <otroan@employees.org>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `46493 <https:////gerrit.fd.io/r/c/vpp/+/46493>`_ [VECr 2]: nat: forward unmatched output-feature flows when there is no pool
  | `46487 <https:////gerrit.fd.io/r/c/vpp/+/46487>`_ [VECr 20]: nat: look up address-only static mappings with protocol 0

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 19]: ip6: fix Pad1 off-by-one in hop-by-hop option pars

policer: **Neale Ranns** <neale@graphiant.com>, **Maxime Peim** <maxime.peim@gmail.com>
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VECr 0]: policer: reject deletion of policer used by punt policing

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `46315 <https:////gerrit.fd.io/r/c/vpp/+/46315>`_ [VECr 17]: quic: quic_quicly add uso support

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [VECr 3]: rdma: steer PPPoE discovery and session flows
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 8]: rdma: add mlx5 DV TSO support for raw packet tx
  | `46465 <https:////gerrit.fd.io/r/c/vpp/+/46465>`_ [VECr 8]: rdma: add mlx5 enhanced MPW with optional inline

session: **Florin Coras** <fcoras@cisco.com>
  | `47224 <https:////gerrit.fd.io/r/c/vpp/+/47224>`_ [VECr 0]: session: fix rx enq of chained buffers
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 17]: udp: add segmentation offload support

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `47100 <https:////gerrit.fd.io/r/c/vpp/+/47100>`_ [VECr 6]: sfdp: add sfdp status API
  | `46952 <https:////gerrit.fd.io/r/c/vpp/+/46952>`_ [VECr 20]: sfdp: add/del tenant notification callbacks

snort: **Damjan Marion** <damarion@cisco.com>
  | `47231 <https:////gerrit.fd.io/r/c/vpp/+/47231>`_ [VECr 0]: snort: consume the enqueue event before clearing interrupt_pending

tcp: **Florin Coras** <fcoras@cisco.com>
  | `47171 <https:////gerrit.fd.io/r/c/vpp/+/47171>`_ [VECr 1]: tcp: count only acks with new sack data as dupacks

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `47227 <https:////gerrit.fd.io/r/c/vpp/+/47227>`_ [VECr 0]: l2: test stale MAC refresh events
  | `46579 <https:////gerrit.fd.io/r/c/vpp/+/46579>`_ [VECr 0]: misc: patch to test maketest action timeout
  | `46963 <https:////gerrit.fd.io/r/c/vpp/+/46963>`_ [VECr 0]: tests: fix fragment_rfc791/fragment_rfc8200 bugs
  | `47190 <https:////gerrit.fd.io/r/c/vpp/+/47190>`_ [VECr 0]: af_packet: preserve VLAN TPID when restoring stripped tags
  | `47191 <https:////gerrit.fd.io/r/c/vpp/+/47191>`_ [VECr 0]: l2: report flushed MACs refreshed by traffic
  | `47175 <https:////gerrit.fd.io/r/c/vpp/+/47175>`_ [VECr 0]: interface: fix punt drop feature arc
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VECr 0]: policer: reject deletion of policer used by punt policing
  | `47217 <https:////gerrit.fd.io/r/c/vpp/+/47217>`_ [VECr 0]: mss_clamp: fix IPv4 vector MSS interface
  | `47102 <https:////gerrit.fd.io/r/c/vpp/+/47102>`_ [VECr 0]: ip6-nd: do not learn an NA for one of our own addresses
  | `47214 <https:////gerrit.fd.io/r/c/vpp/+/47214>`_ [VECr 1]: ikev2: configure inbound ESP replay window
  | `46959 <https:////gerrit.fd.io/r/c/vpp/+/46959>`_ [VECr 1]: linux-cp: free lcp_router_table if 0 routes and no lcp pairs only
  | `47194 <https:////gerrit.fd.io/r/c/vpp/+/47194>`_ [VECr 1]: ikev2: allocate Child SA IDs without collision
  | `47171 <https:////gerrit.fd.io/r/c/vpp/+/47171>`_ [VECr 1]: tcp: count only acks with new sack data as dupacks
  | `46493 <https:////gerrit.fd.io/r/c/vpp/+/46493>`_ [VECr 2]: nat: forward unmatched output-feature flows when there is no pool
  | `47112 <https:////gerrit.fd.io/r/c/vpp/+/47112>`_ [VECr 2]: ikev2 ipip: negotiate USE_TRANSPORT_MODE
  | `47120 <https:////gerrit.fd.io/r/c/vpp/+/47120>`_ [VECr 2]: linux-cp: do not unlock an mfib for MPLS tables
  | `46651 <https:////gerrit.fd.io/r/c/vpp/+/46651>`_ [VECr 3]: vnet: keep deleted interface node names unique
  | `46991 <https:////gerrit.fd.io/r/c/vpp/+/46991>`_ [VECr 3]: pppoeclient: echo relay tag and accept PADS without AC-Cookie
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46966 <https:////gerrit.fd.io/r/c/vpp/+/46966>`_ [VECr 4]: ikev2: guard unassigned profiles in SA status
  | `47076 <https:////gerrit.fd.io/r/c/vpp/+/47076>`_ [VECr 5]: fib: decide the glean source by the address it holds
  | `47001 <https:////gerrit.fd.io/r/c/vpp/+/47001>`_ [VECr 5]: linux-cp: add qinq linux to vpp support
  | `47100 <https:////gerrit.fd.io/r/c/vpp/+/47100>`_ [VECr 6]: sfdp: add sfdp status API
  | `46728 <https:////gerrit.fd.io/r/c/vpp/+/46728>`_ [VECr 7]: ipsec: IPTFS (RFC 9347) unit tests
  | `47078 <https:////gerrit.fd.io/r/c/vpp/+/47078>`_ [VECr 7]: fib: swap in the paths of a source new to the entry
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 8]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `47021 <https:////gerrit.fd.io/r/c/vpp/+/47021>`_ [VECr 9]: igmp: set proxy mfib Accept on host and Forward on router
  | `47020 <https:////gerrit.fd.io/r/c/vpp/+/47020>`_ [VECr 12]: tests: skip parameterized_class base classes in discovery
  | `46995 <https:////gerrit.fd.io/r/c/vpp/+/46995>`_ [VECr 12]: tests: improve return type consistency
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 19]: ip6: fix Pad1 off-by-one in hop-by-hop option pars
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VECr 22]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `46920 <https:////gerrit.fd.io/r/c/vpp/+/46920>`_ [VECr 22]: ip: stop forwarding the Ethernet trailer
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VECr 27]: fib: honor unnumbered RX interface in MFIB RPF check
  | `46753 <https:////gerrit.fd.io/r/c/vpp/+/46753>`_ [VECr 28]: cnat: prevent SNAT policy aliasing across FIBs
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VECr 29]: ip: fix ip mroute bulk insertion CLI for certain inputs

udp: **Florin Coras** <fcoras@cisco.com>
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 17]: udp: add segmentation offload support

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `47224 <https:////gerrit.fd.io/r/c/vpp/+/47224>`_ [VECr 0]: session: fix rx enq of chained buffers
  | `47227 <https:////gerrit.fd.io/r/c/vpp/+/47227>`_ [VECr 0]: l2: test stale MAC refresh events
  | `47171 <https:////gerrit.fd.io/r/c/vpp/+/47171>`_ [VECr 1]: tcp: count only acks with new sack data as dupacks
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)
  | `47078 <https:////gerrit.fd.io/r/c/vpp/+/47078>`_ [VECr 7]: fib: swap in the paths of a source new to the entry
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 19]: ip6: fix Pad1 off-by-one in hop-by-hop option pars
  | `46927 <https:////gerrit.fd.io/r/c/vpp/+/46927>`_ [VECr 21]: crypto: fix fixed-tag AEAD validation

vapi: **Ole Troan** <otroan@employees.org>
  | `46905 <https:////gerrit.fd.io/r/c/vpp/+/46905>`_ [VECr 23]: vapi: mark unregistered vl_msg_ids invalid in the lookup table

vcl: **Florin Coras** <fcoras@cisco.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `47230 <https:////gerrit.fd.io/r/c/vpp/+/47230>`_ [VECr 0]: vppinfra: add coherent physmem allocation

vpp: **Dave Barach** <vpp@barachs.net>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46900 <https:////gerrit.fd.io/r/c/vpp/+/46900>`_ [VECr 20]: vpp: vpp/vnet/main.c fix parsing vpp option and improve description of usage

vppapigen: **Ole Troan** <otroan@employees.org>
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VECr 7]: vppapigen: fix inconsistency in paths JSON

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `47202 <https:////gerrit.fd.io/r/c/vpp/+/47202>`_ [VECr 0]: vppinfra: add foreach_clib_dt_property_string macro
  | `47229 <https:////gerrit.fd.io/r/c/vpp/+/47229>`_ [VECr 0]: vppinfra: add word wrapping helpers
  | `47230 <https:////gerrit.fd.io/r/c/vpp/+/47230>`_ [VECr 0]: vppinfra: add coherent physmem allocation
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VECr 1]: vppinfra: add cast to prevent warning
  | `47188 <https:////gerrit.fd.io/r/c/vpp/+/47188>`_ [VECr 2]: vppinfra: use unsigned CPU feature masks

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `46491 <https:////gerrit.fd.io/r/c/vpp/+/46491>`_ [VECr 2]: wireguard: fix coverity issue 313640

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [Vec 128]: ip_validate: new plugin to drop packets with invalid addresses

**Akos Orban** <orbanakos2001@gmail.com>:

  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 135]: cnat: fix show cnat client showing invalid for client id
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 135]: cnat: fix show cnat translation for specific translation id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `46481 <https:////gerrit.fd.io/r/c/vpp/+/46481>`_ [VeC 43]: acl: add callback hooks for list add/del
  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 51]: vhost: fix rxvq interrupts triggered because of race

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VeC 152]: snort: don't store snort metadata in buffer

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `46256 <https:////gerrit.fd.io/r/c/vpp/+/46256>`_ [vec 97]: crypto: openssl - check ctx alloc/init in key-add
  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VeC 175]: map: enhance map plugin to support per-vrf rules

**Anton Blazhko** <ablazhko@cisco.com>:

  | `45808 <https:////gerrit.fd.io/r/c/vpp/+/45808>`_ [VEc 14]: devices: Convert PIPE to plugin

**Aritra Basu** <aritrbas@cisco.com>:

  | `46541 <https:////gerrit.fd.io/r/c/vpp/+/46541>`_ [vEC 0]: tests: preserve LD_PRELOAD across stdbuf on uutils (Rust)
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [vEC 27]: ip6-nd: enforce on-link source validation for ND learning
  | `46809 <https:////gerrit.fd.io/r/c/vpp/+/46809>`_ [VeC 34]: cnat: skip output SNAT for unsupported protocols
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 40]: ip6-nd: fix unicast NA handling in ND proxy
  | `46593 <https:////gerrit.fd.io/r/c/vpp/+/46593>`_ [VeC 50]: tests: bypass http/https proxy in test curl invocations
  | `46530 <https:////gerrit.fd.io/r/c/vpp/+/46530>`_ [VeC 62]: gha: skip build/test verify jobs for docs-only changes
  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [Vec 106]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VeC 113]: tcp: add TCP fast open support (RFC 7413)
  | `46167 <https:////gerrit.fd.io/r/c/vpp/+/46167>`_ [veC 117]: kube-test: retry Job finalizer cleanup conflicts
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VeC 131]: interface: enable IPv6 link state on unnumbered interfaces
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VeC 131]: vlib: fix trace flag loss when multiple pending frames share next frame

**Benoît Ganne** <bganne@cisco.com>:

  | `46368 <https:////gerrit.fd.io/r/c/vpp/+/46368>`_ [VeC 85]: vppinfra: make vec_foreach_pointer empty-safe
  | `46117 <https:////gerrit.fd.io/r/c/vpp/+/46117>`_ [VeC 121]: vppapigen: fix vppapigen depfile without imports
  | `46087 <https:////gerrit.fd.io/r/c/vpp/+/46087>`_ [VeC 121]: cnat: wait for cnat scanner session cleanup

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [veC 138]: ikev2: add Curve25519 and Curve448 DH groups

**Dennis Lanov** <dennis.lanov@gmail.com>:

  | `46270 <https:////gerrit.fd.io/r/c/vpp/+/46270>`_ [VeC 98]: acl: correct interface command help

**Florin Coras** <florin.coras@gmail.com>:

  | `46687 <https:////gerrit.fd.io/r/c/vpp/+/46687>`_ [veC 50]: vppinfra: avoid duplicate rbtree custom comparison

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [veC 46]: crypto: add op tracing capability
  | `45699 <https:////gerrit.fd.io/r/c/vpp/+/45699>`_ [VeC 75]: dpdk: buffer bug fixes
  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [Vec 168]: dpdk: tracing improvements

**Gopalakrishnan Subramani** <gsubramani@idirect.net>:

  | `47023 <https:////gerrit.fd.io/r/c/vpp/+/47023>`_ [vEC 12]: igmp: set proxy mfib Accept on host and Forward on router

**GregMiller** <greg@gregmiller.co.za>:

  | `46129 <https:////gerrit.fd.io/r/c/vpp/+/46129>`_ [VeC 120]: pppoe: native per-session rx policing in pppoe-decap node
  | `46125 <https:////gerrit.fd.io/r/c/vpp/+/46125>`_ [VeC 120]: pppoe: add combined subscriber session provisioning API

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VEc 15]: sfdp: add sfdp-session-stats service
  | `46588 <https:////gerrit.fd.io/r/c/vpp/+/46588>`_ [veC 51]: sfdp_services: various sfdp nat improvements
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VeC 112]: sfdp: modify tenant_index type from u16 to u32
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VeC 119]: flow: add parameter to pre-allocate global pool
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [veC 119]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VeC 119]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [veC 119]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [Vec 120]: sfdp: add verdict-testbench service
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VeC 120]: flow: add APIs to support new flow actions
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VeC 120]: flow: add flow aging support
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VeC 132]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VeC 132]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [Vec 135]: tracepath: minor refactoring to code
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VeC 156]: sfdp: fix specification of scope_index

**Hanataba Azaka** <northern.snow.x@gmail.com>:

  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [VeC 121]: cnat: make session scanner budget configurable

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `46147 <https:////gerrit.fd.io/r/c/vpp/+/46147>`_ [Vec 117]: npol: support prednat policies
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [Vec 121]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get

**Ivan Shvedunov** <ishvedunov@netgate.com>:

  | `47116 <https:////gerrit.fd.io/r/c/vpp/+/47116>`_ [vEC 5]: fib: populate the glean on source reactivation

**Janik** <janik.haag@imc.com>:

  | `46122 <https:////gerrit.fd.io/r/c/vpp/+/46122>`_ [Vec 92]: build: fix make install-deps for fedora targets
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VeC 121]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VeC 121]: vcl: add regression test for ignorable flags
  | `46121 <https:////gerrit.fd.io/r/c/vpp/+/46121>`_ [VeC 121]: sasc: fix gcc uninitialized warning

**Jerome Tollet** <jtollet@cisco.com>:

  | `46636 <https:////gerrit.fd.io/r/c/vpp/+/46636>`_ [VeC 47]: tests: avoid repeated pg barriers awaiting capture
  | `46719 <https:////gerrit.fd.io/r/c/vpp/+/46719>`_ [VeC 48]: tests: avoid iperf preexec deadlocks
  | `46720 <https:////gerrit.fd.io/r/c/vpp/+/46720>`_ [VeC 48]: tests: make qemu network lock recoverable

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [Vec 133]: ip bonding hash: inner-aware flow hash (opt-in)

**Kai Ji** <kai.ji@intel.com>:

  | `46925 <https:////gerrit.fd.io/r/c/vpp/+/46925>`_ [VEc 12]: crypto: fix engine registration and async dispatch

**Keith Spinney** <kspinney@cisco.com>:

  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [vEC 16]: lb: add NAT6_NOPORT encap type
  | `46525 <https:////gerrit.fd.io/r/c/vpp/+/46525>`_ [VEc 16]: fib: barrier-protect fib_path_list_destroy()

**Klement Sekera** <ksekera@netgate.com>:

  | `46789 <https:////gerrit.fd.io/r/c/vpp/+/46789>`_ [vEC 12]: test: wait for handoff queues to drain before reading a capture
  | `46788 <https:////gerrit.fd.io/r/c/vpp/+/46788>`_ [VeC 37]: vlib: add show handoff pending CLI
  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VeC 99]: build: include GNUInstallDirs in VPPConfig
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VeC 99]: api: add build-time python stub generation via vppapigen

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [Vec 132]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [Vec 132]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [vec 110]: dpdk: support async flow offload
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [veC 133]: docs: document build-time VPP parameters
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VeC 139]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [veC 139]: dpdk: multi-thread async flow offload with per-worker caches

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [VeC 36]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 61]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [Vec 65]: ipip: fix support for ipip6o6 from linux tunnel

**Mykyta Demusenko** <mdemusen@cisco.com>:

  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VeC 42]: teib: move the TEIB implementation to a plugin
  | `46602 <https:////gerrit.fd.io/r/c/vpp/+/46602>`_ [Vec 42]: teib: narrow the C API and add a vnet-owned service boundary
  | `46724 <https:////gerrit.fd.io/r/c/vpp/+/46724>`_ [Vec 42]: teib: add tests for the TEIB API

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 40]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 40]: ip6-nd: add nd-proxy all dst

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vec 139]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `46982 <https:////gerrit.fd.io/r/c/vpp/+/46982>`_ [vEC 16]: papi: read stats scalars and gauges when they are accessed
  | `46511 <https:////gerrit.fd.io/r/c/vpp/+/46511>`_ [veC 48]: stats: add directory command to vpp_get_stats
  | `46434 <https:////gerrit.fd.io/r/c/vpp/+/46434>`_ [VeC 75]: vlib: fix log2 histogram overflow bin writing past the bin vector
  | `46380 <https:////gerrit.fd.io/r/c/vpp/+/46380>`_ [Vec 82]: vppapigen: fix unaligned access to packed messages

**Onong Tayeng** <onong.tayeng@gmail.com>:

  | `46726 <https:////gerrit.fd.io/r/c/vpp/+/46726>`_ [VEc 28]: cnat: clear stale default SNAT policy pointer
  | `46752 <https:////gerrit.fd.io/r/c/vpp/+/46752>`_ [Vec 36]: cnat: update cnat plugin documentation
  | `46471 <https:////gerrit.fd.io/r/c/vpp/+/46471>`_ [Vec 40]: cnat: improve flow statistics and error coverage

**Pavlo Piatakov** <ppiatako@cisco.com>:

  | `46760 <https:////gerrit.fd.io/r/c/vpp/+/46760>`_ [VeC 42]: cnat: do not count unsupported IP protocols as session alloc failure

**Pawel Szymanski** <pawel.szymanski@intel.com>:

  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VEc 8]: build: Changes in makefiles to enabe build on FreeBSD

**Peter Morrow** <pdmorrow@gmail.com>:

  | `46954 <https:////gerrit.fd.io/r/c/vpp/+/46954>`_ [VEc 9]: vlib: leave a MANA VF down when taking its netvsc device

**Pierre Pfister** <pierre@meter.com>:

  | `46858 <https:////gerrit.fd.io/r/c/vpp/+/46858>`_ [VEc 9]: vlib: resume a process once per suspension

**Poornima Kandhade** <poornika@cisco.com>:

  | `46424 <https:////gerrit.fd.io/r/c/vpp/+/46424>`_ [vEC 1]: sfdp: add lifecycle records to session stats ring

**Qi Zhang** <zzqqqqwq77@gmail.com>:

  | `46458 <https:////gerrit.fd.io/r/c/vpp/+/46458>`_ [veC 52]: vlib: detect freed buffer‑chain on node dispatch for double‑free debug
  | `46643 <https:////gerrit.fd.io/r/c/vpp/+/46643>`_ [veC 52]: vnet: fix double-free in bcast fragment reassembly

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [Vec 147]: pfc: add framework for priority flow control
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VeC 159]: octeon: add PFC support

**Robert Shearman** <robertshearman@gmail.com>:

  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VEc 2]: vlib: ASAN-poison unallocated buffers
  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [vec 87]: misc: fix potential OOB read during flow hash calculations

**Samuel Benko** <sbenko@cisco.com>:

  | `47219 <https:////gerrit.fd.io/r/c/vpp/+/47219>`_ [VEc 0]: vperf: fix builtin server echo stall
  | `47220 <https:////gerrit.fd.io/r/c/vpp/+/47220>`_ [VEc 0]: vperf: check echoed stream bytes on client
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VeC 119]: tls: propagate verify config for dtls

**Sergiy Bachynskyy** <sbachyns@cisco.com>:

  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VeC 105]: ipfix: move to a plugin

**Shuzo Ichiyoshi** <deadcafe.beef@gmail.com>:

  | `46180 <https:////gerrit.fd.io/r/c/vpp/+/46180>`_ [VeC 78]: session: check event collector lookups
  | `46355 <https:////gerrit.fd.io/r/c/vpp/+/46355>`_ [VeC 85]: ip: fix fragmentation with negative buffer offset
  | `46178 <https:////gerrit.fd.io/r/c/vpp/+/46178>`_ [VeC 85]: session: validate app for async connect RPC
  | `46352 <https:////gerrit.fd.io/r/c/vpp/+/46352>`_ [VeC 87]: vppinfra: serialize VM map page size lookup
  | `46341 <https:////gerrit.fd.io/r/c/vpp/+/46341>`_ [VeC 89]: hsa: make TLS client CLI MP-safe
  | `46311 <https:////gerrit.fd.io/r/c/vpp/+/46311>`_ [VeC 91]: tcp: handle retransmitted SYN-ACK in TIME-WAIT

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [Vec 35]: fib: dump by src not only contributing routes

**Suresh Sundararaman** <suresh.serc@gmail.com>:

  | `46516 <https:////gerrit.fd.io/r/c/vpp/+/46516>`_ [vEC 2]: misc: surs patch to test CI infra
  | `46529 <https:////gerrit.fd.io/r/c/vpp/+/46529>`_ [VeC 62]: docs: Get the VPP Source

**Taran Dwivedula** <taran184@gmail.com>:

  | `46486 <https:////gerrit.fd.io/r/c/vpp/+/46486>`_ [VEc 0]: fib ethernet: honour ethernet-output features on L2 adjacencies

**Viacheslav Zakharchenko** <vzakharc@cisco.com>:

  | `45807 <https:////gerrit.fd.io/r/c/vpp/+/45807>`_ [Vec 98]: bfd: Introduce vppinfra/callback_data based vnet notifier for FIB/ADJ notifications
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [Vec 99]: bfd: Extract to plugin

**Vladimir Lavor** <vlavor@cisco.com>:

  | `46268 <https:////gerrit.fd.io/r/c/vpp/+/46268>`_ [VeC 97]: vlib: expose error severity in stats segment

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [Vec 156]: flowprobe: count based sampling support

**Vratko Polak** <vrpolak@cisco.com>:

  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VeC 33]: buffers: make natural layout always default
  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vec 145]: sfdp_services: add basic support for time-wait

**Wei Wang** <weiwa@cisco.com>:

  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [Vec 118]: tls: tls session resumption code and host stack tests

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VeC 147]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer
  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [Vec 147]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [veC 148]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VeC 149]: vlib: fix process state format output wrapped by extra quotes
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vec 154]: vlib: pre-input node should be dispatched before input node

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [Vec 110]: vppinfra: add loongarch64 architecture support

**Yuto Suzuki** <offside.items03@icloud.com>:

  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VEc 22]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VEc 22]: ip6-nd: support RDNSS option in IPv6 RA

**juhua yin** <ameliayin1990@gmail.com>:

  | `46828 <https:////gerrit.fd.io/r/c/vpp/+/46828>`_ [VEc 28]: dpdk: fix change mac address of the member failed

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [veC 163]: vlib: fix '\' command input will causes memory out of bounds

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 178]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [vEC 16]: cnat: add scope_id to session key
  | `46546 <https:////gerrit.fd.io/r/c/vpp/+/46546>`_ [VeC 59]: vlib: re-base the timing wheel when arming an empty wheel

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VeC 173]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [VEc 0]: vcl: fix crash when closing listener with pending accepts
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VeC 160]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VeC 162]: tls: fix picotls partial record handling
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [Vec 169]: session: make transport to use application's segment manager

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
authors          137
maintainers      94
committers       2
abandoned        0
================ ===

